from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# MySQL connection config
conn = pymysql.connect(
    host="dev-aws-ug-workshop-demo.canaphmx8rjr.us-east-1.rds.amazonaws.com",
    user="awsadmin",
    password="|w6UppSla4YFdTRwOJMM_qX*aoW2",
    db="aws_ug_ensenada",
    cursorclass=pymysql.cursors.DictCursor
)

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json
    try:
        with conn.cursor() as cursor:
            # Insert user
            sql_user = "INSERT INTO users (name, age) VALUES (%s, %s)"
            cursor.execute(sql_user, (data["name"], data["age"]))
            user_id = cursor.lastrowid

            # Insert career
            career = data["career"]
            sql_career = """
                INSERT INTO careers (user_id, title, industry, experience_years)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql_career, (user_id, career["title"], career["industry"], career["experience_years"]))

            # Insert skills
            for skill in data.get("skills", []):
                sql_skill = "INSERT INTO skills (user_id, skill, level) VALUES (%s, %s, %s)"
                cursor.execute(sql_skill, (user_id, skill["skill"], skill["level"]))

            # Insert hobbies
            for hobby in data.get("hobbies", []):
                sql_hobby = "INSERT INTO hobbies (user_id, hobby) VALUES (%s, %s)"
                cursor.execute(sql_hobby, (user_id, hobby))

            conn.commit()
            return jsonify({"message": "User added", "user_id": user_id}), 201

    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500


@app.route("/get_users", methods=["GET"])
def get_users():
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()

            # Join career, skills, hobbies
            for user in users:
                user_id = user["user_id"]

                # Career
                cursor.execute("SELECT * FROM careers WHERE user_id = %s", (user_id,))
                career = cursor.fetchone()
                user["career"] = career if career else {}

                # Skills
                cursor.execute("SELECT skill, level FROM skills WHERE user_id = %s", (user_id,))
                skills = cursor.fetchall()
                user["skills"] = skills

                # Hobbies
                cursor.execute("SELECT hobby FROM hobbies WHERE user_id = %s", (user_id,))
                hobbies = cursor.fetchall()
                user["hobbies"] = [h["hobby"] for h in hobbies]

            return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
            conn.commit()
            return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)

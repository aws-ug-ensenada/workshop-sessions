from flask import Flask, request, jsonify
import boto3
import uuid
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure AWS DynamoDB
session = boto3.Session(profile_name="personal")
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('aws-ug-ensenada-demo')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    user_id = str(uuid.uuid4())

    item = {
        'user_id': user_id,
        'name': data['name'],
        'age': data['age'],
        'career': data['career'],  # Nested JSON
        'skills': data.get('skills', []),  # Optional List
        'hobbies': data.get('hobbies', [])  # Optional List
    }

    table.put_item(Item=item)
    return jsonify({'message': 'User added', 'user_id': user_id})

@app.route('/get_users', methods=['GET'])
def get_users():
    response = table.scan()
    return jsonify(response['Items'])

@app.route("/delete_user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        response = table.delete_item(Key={"user_id": user_id})  # Corrected key name
        return jsonify({"message": "User deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

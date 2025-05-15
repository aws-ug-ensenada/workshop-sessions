from db import get_connection
import mysql.connector
from mysql.connector import Error
import sys

def initialize_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            );
        """)

        cursor.execute("INSERT INTO items (name) VALUES ('Apple'), ('Banana'), ('Cherry');")
        conn.commit()

        cursor.close()
        conn.close()
        print("✅ Database initialized successfully!")

    except mysql.connector.InterfaceError as ie:
        print("❌ Could not connect to the database. Please check your network and credentials.")
        print(f"Error: {ie}")
        sys.exit(1)

    except mysql.connector.Error as err:
        print("❌ MySQL Error occurred.")
        print(f"Error: {err}")
        sys.exit(1)

    except Exception as e:
        print("❌ An unexpected error occurred.")
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    initialize_db()

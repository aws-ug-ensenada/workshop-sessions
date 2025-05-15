from db import get_connection
import mysql.connector
from mysql.connector import Error
import sys

def initialize_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Drop old table if it exists
        cursor.execute("DROP TABLE IF EXISTS items;")

        # Create new users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                full_name VARCHAR(255) NOT NULL
            );
        """)

        # Insert AWS User Group Ensenada members
        users = [
            "Addy",
            "Alejandro Renato Leon Lomeli",
            "Alejandro Velazquez",
            "alfredevvv",
            "Alonso Parasxidis Moreno",
            "Aylin Gallegos",
            "Brayan Ivan",
            "Daniel",
            "Daniel Solano",
            "David Eduardo Ferreira",
            "David Jimenez Rodriguez",
            "diego.quiros",
            "diego198mayo",
            "duranzavala",
            "eliel.ontiveros",
            "Emanuel solis",
            "Fernando Haro",
            "Fiorella",
            "Gerardo Velez",
            "Ivan Duarte Patiño",
            "Jesus Miguel Armenta Garzon",
            "Joel Ernesto Lopez Verdugo",
            "Jorge V",
            "José Luna",
            "karen.garcia17",
            "Lariza.Covarrubias",
            "leonel120lgr",
            "leonelriverasal",
            "Igonzalez85",
            "Manuel Rubio",
            "Mariana Salazar",
            "mario.valenzuela50",
            "ozkarxbox",
            "Pedro Walle",
            "rivas.andrea",
            "Salvador Reyes",
            "Sergio Burguer",
            "Teresa Rivas"
        ]

        cursor.executemany("INSERT INTO users (full_name) VALUES (%s)", [(name,) for name in users])
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

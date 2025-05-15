from db import get_connection

def initialize_db():
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
    print("Database initialized!")

if __name__ == "__main__":
    initialize_db()

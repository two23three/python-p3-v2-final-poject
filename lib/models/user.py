from models.__init__ import CONN, CURSOR
import sqlite3


class User:
    @classmethod
    def register_user(cls, username, password):
        try:
            CURSOR.execute("""
                INSERT INTO users (username, password)
                VALUES (?, ?)
            """, (username, password))
            CONN.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Username already exists. Please choose a different username.")

    @classmethod
    def login(cls, username, password):
        # Check if there are any users in the database
        if not cls.get_all():
            print("No users found. Please register first.")
            return False

        # Proceed with login if users exist
        CURSOR.execute("""
            SELECT id FROM users
            WHERE username = ? AND password = ?
        """, (username, password))
        user_id = CURSOR.fetchone()
        if user_id:
            print("Login successful.")
            return True
        else:
            print("Invalid username or password.")
            return False

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT id, username, password FROM users")
        rows = CURSOR.fetchall()
        return rows
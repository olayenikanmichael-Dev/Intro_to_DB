# MySQLServer.py

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database in MySQL."""
    connection = None
    cursor = None
    try:
        # 1. Connect to MySQL server (no database specified yet)
        connection = mysql.connector.connect(
            host='localhost',       
            user='pounds',    
            password='olawunmi' 
        )

        if connection.is_connected():
            print(" Connected to MySQL server")

        cursor = connection.cursor()
        # 2. Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f" Error while connecting to MySQL: {e}")

    finally:
        # 3. Close cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print(" MySQL connection closed")

# Main execution
if __name__ == "__main__":
    create_database()

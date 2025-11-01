import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        print("Trying to connect...")
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="11092003",  # replace with your actual password
            database="shopsmart_db",
            port=3306
        )

        if connection.is_connected():
            print("✅ Successfully connected to MySQL database")
            return connection

    except Error as e:
        print("❌ Error while connecting to MySQL:", e)
        return None
    
get_connection()
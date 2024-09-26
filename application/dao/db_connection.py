# dao/db_connection.py

import mysql.connector
from mysql.connector import Error

class DBConnection:
    def __init__(self):
        self.host = 'localhost'
        self.database = 'le_prix_goncourt'
        self.user = 'root'  # Remplace par ton utilisateur
        self.password = ''  # Remplace par ton mot de passe

    def connect(self):
        """Establishes a connection to the MySQL database."""
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if connection.is_connected():
                print("Connected to MySQL database")
                return connection
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
            return None

    def close(self, connection):
        """Closes the given connection."""
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

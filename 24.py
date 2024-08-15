import sqlite3
class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print(f"Connected to SQLite database: {self.db_file}")
        except sqlite3.Error as e:
            print(f"Error connecting to SQLite database: {e}")

    def execute_query(self, query):
        try:
            if self.connection:
                self.cursor.execute(query)
                self.connection.commit()
                print("Query executed successfully")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

# Example usage:
db = Database('example.db')

# Execute a query
db.execute_query("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data
db.execute_query("INSERT INTO users (name, age) VALUES ('Alice', 30)")

# Close the database connection
db.close()
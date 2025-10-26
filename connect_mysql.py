import mysql.connector

# Connect to MySQL database
library_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prizylink330@",
    database="library_db"  # Make sure this DB exists in MySQL
)

print(" Connected successfully to MySQL Server version:", library_db.server_info)


import mysql.connector

# Connect to MySQL
library_db = mysql.connector.connect(
    host="localhost",
    user="root",             # your MySQL username
    password="Prizylink330@",  # your MySQL password
)

cursor = library_db.cursor()

# Create database if it doesn’t exist
cursor.execute("CREATE DATABASE IF NOT EXISTS library_db")
cursor.execute("USE library_db")

# Create the books table with title and author
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL
)
""")

#  Insert a record into the books table
cursor.execute("INSERT INTO books (title, author) VALUES (%s, %s)",
               ("Pride and Prejudice", "Jane Austen"))

#  Commit the transaction
library_db.commit()

#  Fetch all books and print
cursor.execute("SELECT * FROM books")
for book in cursor.fetchall():
    print(book)

#  Close connection
cursor.close()
library_db.close()

print("✅ Book inserted successfully and displayed above!")


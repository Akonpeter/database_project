import mysql.connector

library_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Prizylink330@",
    database="library_db")


cursor = library_db.cursor()

# Create a table named `customers` (if it doesn't exist)

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE
)
""")

print("Table created successfully!")

# Insert some customer data
sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
val = ("John Doe", "john.doe@example.com")
cursor.execute(sql, val)
library_db.commit()

print(cursor.rowcount, "record(s) inserted.")

val = ("Jane Smith", "jane.smith@example.com")
cursor.execute(sql, val)
library_db.commit()

print(cursor.rowcount, "record(s) inserted.")

# Read all customer data
cursor.execute("SELECT * FROM customers")
result = cursor.fetchall()

print("Customers:")
for row in result:
  print(row)

# Update a customer's email
sql = "UPDATE customers SET email = %s WHERE id = %s"
val = ("updated.email@example.com", 1)
cursor.execute(sql, val)
library_db.commit()

print(cursor.rowcount, "record(s) updated.")

# Read the updated customer data
cursor.execute("SELECT * FROM customers WHERE id = 1")
result = cursor.fetchone()

print("Updated customer:")
print(result)

# Delete a customer
sql = "DELETE FROM customers WHERE id = 2"
cursor.execute(sql)
library_db.commit()

print(cursor.rowcount, "record(s) deleted.")

# Close connections
cursor.close()
library_db.close()

print("Database connection closed.")

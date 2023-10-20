
import mysql.connector

database = mysql.connector.connect(
    host = 'localhost' ,
    user = 'root',
    passwd= 'Sandy@123'
)


# prepare a cursor project

cursorObject = database.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE users")

print("All Done ")


# we can delete this file , its only for connection
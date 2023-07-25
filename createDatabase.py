import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Babu6654",
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE testdb")

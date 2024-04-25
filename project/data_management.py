import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="db_username",
    passwd="db_password",
    db="db_name"
)

print(mydb)
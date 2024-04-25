import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="FREE-SPIRIT",
    passwd="1234",
    db="test"
)

print(mydb)
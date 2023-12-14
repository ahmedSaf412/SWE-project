import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost',
    user='root',
    passwd='root'
)

cursorObject = dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE DepDB")

print("All Done")


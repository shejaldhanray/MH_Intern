#Create Connection
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="it@123",
  database="MHTECHIN"
)

print(mydb)
mycursor = mydb.cursor()

#Creating a Database
mycursor.execute("CREATE DATABASE MHTECHIN")


#Check if Database Exists
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)
  
#Creating a Table
mycursor.execute("CREATE TABLE Task2 (nameIntern VARCHAR(255), ID VARCHAR(255))")

#Check if Table Exists
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
  
  
#Insert Into Table 
sql = "INSERT INTO Task2 (nameIntern, ID) VALUES (%s, %s)"
val = ("shejal", "8")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")




#Select From a Table
mycursor.execute("SELECT * FROM Task2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
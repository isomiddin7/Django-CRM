# Install Mysql on your computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'isomiddin.rahimov20020704'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a databse
cursorObject.execute("CREATE DATABASE isomiddin")
print("All Done!")
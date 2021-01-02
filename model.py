# PyBase
# Author: Dmitrii Iakimchuk

# The 'Model' part of the MVC structure. This part is responsible for working with the data structure

# Importing a package to connect to a MySQL database
import mysql.connector

# Creating a connection
mydb = mysql.connector.connect(host="localhost", user="root", passwd="password",
                               database='testdb',
                               auth_plugin='mysql_native_password')
# Creating a cursor
mycursor = mydb.cursor()


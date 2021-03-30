import sqlite3
from sqlite3 import Error

def insertData(connection, sqlCommand):
	"""
	Inserts data from the sqlCommand statement

	###Arguments###
		connection: Connection object created with conn
		sqlCommand: SQL-Statement to insert data from

	###Returns###
		none
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(sqlCommand)
	except Error as e:
		file = open("logfile.txt", "a")
		file.write("\n\nError while inserting data:\n"+e+"\n\n")
		file.close()
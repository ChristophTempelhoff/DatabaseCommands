import sqlite3
from sqlite3 import Error

def createTable(connection, sqlCommand):
	"""
	Creates a table from the sqlCommand statement

	###Arguments###
		connection: Connection object created with conn
		sqlCommand: SQL-Statement to create the table from

	###Returns###
		none
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(sqlCommand)
	except Error as e:
		file = open("logfile.txt", "a")
		file.write("\n\nError while creating tables:\n"+e+"\n\n")
		file.close()
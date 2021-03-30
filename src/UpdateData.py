import sqlite3
from sqlite3 import Error

def updateData(connection, sqlCommand):
	"""
	Updates data from the sqlCommand statement

	###Arguments###
		connection: Connection object created with conn
		sqlCommand: SQL-Statement to update data from

	###Returns###
		none
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(sqlCommand)
	except Error as e:
		file = open("logfile.txt", "a")
		file.write("\n\nError while updating data:\n"+e+"\n\n")
		file.close()
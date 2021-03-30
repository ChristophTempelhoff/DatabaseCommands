import sqlite3
from sqlite3 import Error

def deleteData(connection, sqlCommand):
	"""
	Deletes data from the sqlCommand statement

	###Arguments###
		connection: Connection object created with conn
		sqlCommand: SQL-Statement to delete data from

	###Returns###
		none
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(sqlCommand)
	except Error as e:
		file = open("logfile.txt", "a")
		file.write("\n\nError while deleting data:\n"+e+"\n\n")
		file.close()
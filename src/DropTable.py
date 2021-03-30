import sqlite3
from sqlite3 import Error

def dropTable(connection, sqlCommand):
	"""
	Drops a table from the sqlCommand statement

	###Arguments###
		connection: Connection object created with conn
		sqlCommand: SQL-Statement to drop the table from

	###Returns###
		none
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(sqlCommand)
	except Error as e:
		file = open("logfile.txt", "a")
		file.write("\n\nError while dropping tables:\n"+e+"\n\n")
		file.close()
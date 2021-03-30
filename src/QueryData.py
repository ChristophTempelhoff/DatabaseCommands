import sqlite3
from sqlite3 import Error

def queryData(connection, sqlCommand):
	"""
	Querys data from the sqlCommand statement

	###Arguments###
		connection: Connection object created with conn
		sqlCommand: SQL-Statement to insert data from

	###Returns###
		rows: An 2darray which consists of all rows in your table
	"""
	try:
		cursor = connection.cursor()
		cursor.execute(sqlCommand)

		rows = cursor.fetchall()
	except Error as e:
		file = open("logfile.txt", "a")
		file.write("\n\nError while querying data:\n"+e+"\n\n")
		file.close()
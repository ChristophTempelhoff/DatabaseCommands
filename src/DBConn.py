import sqlite3
from sqlite3 import Error
def conn(Database_dir):
    """
    This function connects to a local sqlite3 database or creates one if there's none within the path and with that name

    ###Arguments###
        Database_dir: The path the database should be stored in including the name of the database +.db 

    ###Return###
        connection: Connection object or none. Error will be written in a logfile.txt
    """
    connection = none
    try:
        connection = sqlite3.connect(Database_dir)
        return connection
    except Error as e:
        file = open("logfile.txt","a")
        file.write("\n\nError while creating/connecting database:\n"+e+"\n\n")
        file.close()

    return connection

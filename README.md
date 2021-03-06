# DatabaseCommands
## Structure
- Structure
- General Information about this package
- What can this package do?
  - Create and/or connect to Databases
    - Input
  - Create Tables
    - Input
  - Drop Tables
    - Input
  - Insert Data
    - Input
  - Update Data
    - Input
  - Delete Data
    - Input
  - Query Data
    - Input
    - Output
    - How to handle
- How to insert it into your code

---
## General Information about this package
This package was created so more people could be working with databases without getting to deep into it. The python SQLite3 tutorials from SQLite were the basics of this project
but changed to serve a more general meaning. I tried to make it as userfriendly as I could. Feel free to change stuff in your dir. **This is just the beginning and might get more features _later_**.

---
## What can this package do?
### - Create Databases
   Shortly said the package can create and connect to a SQLite3 Database. It can be accessed through: ```from DatabaseCommands import DBConn```. Your connection should be stored in a variable
   because it will be needed. **This will be critical for any other modules in this package.**
   #### - Input
   You only need to input the dir+the filename or only the filename if you want it in your working dir
   
   ---
### - Create Tables
   With ```from DatabaseCommands import CreateTable``` you can create tables in your database.
  #### - Input
   database-connection object: The connection to your database. 
   
   sql-command: The SQL-Command which creates the table. A full SQL-Command is needed because otherwise your table will not be created.
   
   ---
### - Drop Tables
   With ```from DatabaseCommands import DropTable``` you can drop tables in your database.
  #### - Input
   database-connection object: The connection to your database.
   
   sql-command: The SQL-Command which dropes the table. A full SQL-Command is needed because otherwise your table will not be dropped.
   
   ---
### - Insert Data
   With ```from DatabaseCommands import InsertData``` you can insert data in your database. *This module, Update Data and Delete Data work the same way but will be kept for better readability*
   #### - Input
   database-connection object: The connection to your database. 
   
   sql-command: The SQL-Command which inserts the data. A full SQL-Command is needed because otherwise your data will not be inserted.
   
   ---
### - Update Data
   With ```from DatabaseCommands import UpdateData``` you can update data in your database. *This module, insert data and delete data work the same way but will be kept for better readability*
   #### - Input
   database-connection object: The connection to your database. 
   
   sql-command: The SQL-Command which updates the data. A full SQL-Command is needed because otherwise your data will not be updated.

---
### - Delete Data
   With ```from DatabaseCommands import DeleteData``` you can delete data in your database. *This module, update data and insert data work the same way but will be kept for better readability*
   #### - Input
   database-connection object: The connection to your database. 
   
   sql-command: The SQL-Command which deletes the data. A full SQL-Command is needed because otherwise your data will not be deleted.
   
   ---
### - Query Data
   With ```from DatabaseCommands import QueryData```you can Query data from your database.
   #### - Input
   database-connection object: The connection to your database. 
   
   sql-command: The SQL-Command which selects the data. A full SQL-Command is needed because otherwise your data will not be selected.
   
   #### - Output
   An array with all your beautiful data you asked for.
   
   #### - How to handle
   When you want a specific piece of data i.e. allways the name only to be displayed use the index. Remember they start at 0.
   
---
## - How to insert into your code
An Example:
```
from DatabaseCommands import DBConn
from DatabaseCommands import CreateTable
from DatabaseCommands import InsertData
from DatabaseCommands import QueryData

def main():
  conn = DatabaseCommands.DBConn.conn("test.db")
  
  create_Table_sql = '''CREATE TABLE IF NOT EXIST test(
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        description text NOT NULL);'''
                        
  DatabaseCommands.CreateTable.createTable(conn, create_Table_sql)
  
  insert_data_sql = '''INSERT INTO test(name, description) VALUES("Production test", "This test is meant to check if anything is working");'''
  
  DatabaseCommands.InsertData.insertData(conn, insert_data_sql)
  
  rows = DatabaseCommands.QueryData(conn, "SELECT * FROM test")
  
  for row in rows:
    print("Name: " + row[1])
    print("Description: " + row[2])
```

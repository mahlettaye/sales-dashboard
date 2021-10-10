## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql



class DatabaseHandelr:
    """ ## connecting to the database using 'connect()' method
        ## it takes 3 required parameters 'host', 'user', 'passwd'
    """
    def db_connect(self):
        try:
            db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = ""
            )

            print(db) #
        except Exception as e :
            print ("Unable to connet to Mysqlpass"+e)
         
        return db
    def create_database (self, conn):
        try:
            ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
            cursor = conn.cursor()

            ## creating a databse called 'datacamp'
            ## 'execute()' method is used to compile a 'SQL' statement
            ## below statement is used to create tha 'datacamp' database
            cursor.execute("CREATE DATABASE IF NOT EXISTS Rossmann")
        except Exception as e:
            print("Unable to create Database"+e)
            

if __name__ == "__main__":
    dbobj = DatabaseHandelr()
    conn = dbobj.db_connect()
    dbobj.create_database(conn)

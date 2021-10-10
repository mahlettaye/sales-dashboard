## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
from data_processor import DataProcessor
from pandas.io import sql
from sqlalchemy import create_engine
import json 
import collections




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
            print ("Unable to connet to Mysqlpass",e)
         
        return db
    def create_database (self, conn):
        try:
            ## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
            cursor = conn.cursor()

            ## creating a databse called 'datacamp'
            ## 'execute()' method is used to compile a 'SQL' statement
            ## below statement is used to create tha 'Rossman' database
            cursor.execute("CREATE DATABASE IF NOT EXISTS Rossmann")
        except Exception as e:
            print("Unable to create Database"+e)


    def create_table (self):
        try:
            db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "Rossmann"
)
            cursor = db.cursor()

            ## creating a table called 'sales' in the 'Rossmann' database   
            cursor.execute("""CREATE TABLE IF NOT EXISTS rsales (Store INT (5),
            DayOfWeek INT(5), Date  INT(5), Sales INT(5), Customers INT(5),
            Open INT(5), PromoStateHoliday INT(5),  SchoolHoliday INT(5), 
            Month INT(5),  Day INT(5),  Year INT(5),  Week INT(5))""")
        except Exception as e:
         print("unable to create table", e)
    

    def insert_data(self):
        try:
            obj= DataProcessor()
            data= obj.data_to_send()
            data= data[:100]
            

            engine = create_engine('mysql://root:@localhost/Rossmann')
            with engine.connect() as conn, conn.begin():
                data.to_sql('rsales', conn, if_exists='replace')
            print("All records are submitted successfully")
        except Exception as e:
            print("unable to insert data", e)
            
    def select_function(self):
        db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "Rossmann"
            )
        
        cur = db.cursor()
        cur.execute("SELECT Year,Sales FROM rsales where Open !=0")
        rows = cur.fetchall()
        rowarray_list = []
        for row in rows:
            t = (row[0], row[1])
            rowarray_list.append(t)
        #j = json.dumps(rowarray_list)

        # Convert query to objects of key-value pairs
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d["Year"] = row[0]
            d["Sales"] = row[1]
            
            objects_list.append(d)

        j = json.dumps(objects_list)

        with open("test.js", "w") as f:
            f.write(j)
        return j
        




            
        



            

if __name__ == "__main__":
    dbobj = DatabaseHandelr()
    conn = dbobj.db_connect()
    #dbobj.create_table()
    #dbobj.insert_data()
    dbobj.select_function()

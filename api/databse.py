## Connecting to the database

## importing 'mysql.connector' as mysql for convenient
import mysql.connector as mysql
from api.data_processor import DataProcessor
from pandas.io import sql
from sqlalchemy import create_engine
import json 
import collections
from datetime import datetime,date




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
            cursor.execute("""CREATE TABLE IF NOT EXISTS RSales (SalesID  INT (5)NOT NULL AUTO_INCREMENT, Store INT (5),
            DayOfWeek INT(5), Date  INT(5), Sales INT(5), Customers INT(5),
            Open INT(5), Promo INT(5), StateHoliday INT(5),  SchoolHoliday INT(5), 
            Month INT(5),  Day INT(5),  Year INT(5),  Week INT(5), PRIMARY KEY (SalesID))""")
        except Exception as e:
         print("unable to create table", e)
    

    def insert_data(self):
        try:
            obj= DataProcessor()
            data= obj.data_to_send()
            data = data [:10000]
           
            

            engine = create_engine('mysql://root:@localhost/Rossmann')
            with engine.connect() as conn, conn.begin():
                data.to_sql('RSales', conn, if_exists='replace')
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
        cur.execute("SELECT * FROM RSales LIMIT 2000")
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
            d["Store"] = row[1]
            d["DayOfWeek"] = row[2]
            d["Date"] = row[3]
            d["Sales"] = row[4]
            d["Customers"] = row[5]
            d["Open"] = row[6]
            d["Promo"] = row[7]
            d["StateHoliday"] = row[8]
            d["SchoolHoliday"] = row[9]
            d["Month"] = row[10]
            d["Day"] = row[11]
            d["Year"] = row[12]
            d["Week"] = row[13]
            
            objects_list.append(d)

        #j = json.dumps(objects_list)

        # with open("test.js", "w") as f:
        #     f.write(j)
        return objects_list
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))
    def get_games():
        db = mysql.connect(
            host = "localhost",
            user = "root",
            passwd = "",
            database = "Rossmann"
            )
       
        cursor = db.cursor()
        query = "SELECT Year,Sales FROM rsales where Open !=0"
        cursor.execute(query)
        return cursor.fetchall()
        




            
        



            

if __name__ == "__main__":
    dbobj = DatabaseHandelr()
    conn = dbobj.db_connect()
    dbobj.create_table()
    dbobj.insert_data()
    #dbobj.select_function()

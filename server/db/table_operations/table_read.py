import mysql.connector
from server.utilities.decorators import rdsConnect

@rdsConnect
def tableNames(mycursor):
    try:
        mycursor.execute("SHOW TABLES")
        names=[x for x in mycursor]
        mycursor.close()
        return {"tableNames":names}
    except mysql.connector.Error as err:
        print("Error in trying to retrieve tableNames: {}".format(err))
    finally:
        mycursor.close()

@rdsConnect
def tableColumns(mycursor, table):
    try:
        sql="SHOW columns FROM "+table
        mycursor.execute(sql)
        data=[column[0] for column in mycursor.fetchall()]
        return {"Columns":data}
    except mysql.connector.Error as Err:
        print("Error displaying columns from {} table: {} ".format(table, Err))
    finally:
        mycursor.close()
    
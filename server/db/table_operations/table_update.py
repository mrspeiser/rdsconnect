import mysql.connector
import server.db.connect as rds
import server.db.table_operations.table_read as table_read
from server.utilities.decorators import rdsConnect

@rdsConnect
def createColumn(mycursor, table, columnName):
    try:        
        sql = "ALTER TABLE "+table+" ADD "+columnName+" VARCHAR(255)"
        mycursor.execute(sql)
        columnsList=table_read.tableColumns(mycursor, table)
        mycursor.close()
        return columnsList
    except mysql.connector.Error as Err:
        print("Error updating table: {} and adding Column: {}. Err: {}".format(table, columnName, Err))
    finally:
        mycursor.close()
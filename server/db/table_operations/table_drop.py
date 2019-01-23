import mysql.connector
import server.db.connect as rds
from server.utilities.decorators import rdsConnect

@rdsConnect
def dropTable(mycursor, tableName):
    try:    
        sql="DROP TABLE "+tableName
        mycursor.execute(sql)

        mycursor.execute("SHOW TABLES")
        tables=[x for x in mycursor]
        
        mycursor.close()
        return {"remainingTables": tables}
    except mysql.connector.Error as err:
        print("error dropping table: {}".format(err))
    finally:
        mycursor.close()
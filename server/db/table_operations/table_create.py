import mysql.connector
import server.db.connect as rds
from server.utilities.decorators import rdsConnect

@rdsConnect
def createTable(mycursor, tableName):
    try:
        mycursor.execute(
            """CREATE TABLE {0} 
            (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                first_name VARCHAR(255), 
                last_name VARCHAR(255), 
                email VARCHAR(255), 
                phone_primary VARCHAR(255), 
                body VARCHAR(1200), 
                location_data VARCHAR(255), 
                user_agent VARCHAR(255),
                received_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            )""".format(tableName)
        )
        mycursor.close()
        return {"CreateTable":"Created Successfully"}
    except mysql.connector.Error as err:
        print("there was an error creating the table: {0}".format(err))
    finally:
        mycursor.close()
            
import mysql.connector
from server.utilities.decorators import rdsConnect
from server.config.config_write import write_db_config_section, write_db_config_key_value

@rdsConnect
def createTable(mycursor, tableName, properties, required_client_fields, maxkeys):
    try:
        mycursor.execute(
            """CREATE TABLE {0} 
            (
                {1}
            )""".format(tableName, properties)
        )
        write_db_config_section(tableName)
        write_db_config_key_value(tableName, 'requiredclientfields', required_client_fields)
        write_db_config_key_value(tableName, 'maxkeys', maxkeys)
        mycursor.close()
        return {"CreateTable":"Created Successfully"}
    except mysql.connector.Error as err:
        print("there was an error creating the table: {0}".format(err))
    finally:
        mycursor.close()
            
@rdsConnect
def createDefaultTable(mycursor, tableName="default"):
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
        write_db_config_section(tableName)
        write_db_config_key_value(tableName, 'requiredclientfields', 'first_name,last_name,email')
        write_db_config_key_value(tableName, 'maxkeys', '7')
        mycursor.close()
        return {"CreateTable":"Created Successfully"}
    except mysql.connector.Error as err:
        print("there was an error creating the table: {0}".format(err))
        return "there was an error creating the table: {0}".format(err)
    finally:
        mycursor.close()
  
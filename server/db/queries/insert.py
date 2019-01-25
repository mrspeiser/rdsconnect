import mysql.connector
from server.utilities.decorators import rdsConnect

@rdsConnect
def insertData(mycursor, data, table):
    try:
        sql =   """INSERT INTO """+table+""" 
                (
                    first_name, 
                    last_name, 
                    email, 
                    phone_primary, 
                    body, 
                    location_data,
                    user_agent
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

        val=[   data["first_name"], 
                data["last_name"], 
                data["email"], 
                data["phone_primary"], 
                data["body"], 
                data["location_data"],
                data["user_agent"]
            ]   
        
        mycursor.execute(sql, val)
        # print(mycursor.rowcount, "Record Inserted")
        mycursor.close()
        return data
        
    except mysql.connector.Error as err:
        print("Something went wrong commiting data: {}".format(err))
        return {"Error":"Error inserting data, ERROR: {}".format(err)}
    finally:
        mycursor.close()

@rdsConnect
def insertDataVer(mycursor, data, table, properties):
    try:
        sql =   """INSERT INTO """+table+""" 
                (
                    """+properties+"""
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

        val=[   data["first_name"], 
                data["last_name"], 
                data["email"], 
                data["phone_primary"], 
                data["body"], 
                data["location_data"],
                data["user_agent"]
            ]   
        
        mycursor.execute(sql, val)
        # print(mycursor.rowcount, "Record Inserted")
        mycursor.close()
        return data
        
    except mysql.connector.Error as err:
        print("Something went wrong commiting data: {}".format(err))
        return {"Error":"Error inserting data, ERROR: {}".format(err)}
    finally:
        mycursor.close()
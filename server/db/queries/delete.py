import mysql.connector
from server.utilities.decorators import rdsConnect

@rdsConnect
def delete(mycursor, rowId, table="messages"):
    try:   
        mycursor.execute("DELETE FROM "+table+ " WHERE id = "+rowId)
        print(mycursor.rowcount, "records deleted")
        mycursor.close()
        return {"DeleteQuery":"Sucess","records deleted":mycursor.rowcount }
    except mysql.connector.Error as Err:
        print("Something went wrong Deleting data: {}".format(Err))
    finally:
        mycursor.close()

@rdsConnect
def deleteRowTest(mycursor, rowId="1", table="ProceduresCheck"):
    try:    
        mycursor.execute("DELETE FROM "+table+" WHERE id = "+rowId)
        deletedrows=mycursor.rowcount
        mycursor.close()
        return {"DeleteRow":"Success","records deleted":deletedrows}
    except mysql.connector.Error as Err:
        print("Something went wrong Deleting data: {}".format(Err))
    finally:
        mycursor.close()
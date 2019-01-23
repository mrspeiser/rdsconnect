import mysql.connector
from server.utilities.decorators import rdsConnect

@rdsConnect
def updateRowTest(mycursor, data, rowId="1", table="ProceduresCheck"):
    try:
        updateString="SET "
        updateString += ','.join('{0}=\'{1}\''.format(key,val) for key,val in data.items())
        where="WHERE id = "+rowId

        sql="UPDATE "+table+" "+updateString+" "+where
        print(str(sql))
        mycursor.execute(sql)

        return data
    except mysql.connector.Error as err:
        print("Something went wrong updating data: {}".format(err))
        return {"ERROR": "Something went wrong updating data: {}".format(err)}
    finally:
        mycursor.close()
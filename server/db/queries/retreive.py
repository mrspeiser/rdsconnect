from server.utilities.decorators import rdsConnect
import server.db.table_operations.table_read as table_read

@rdsConnect
def getall(mycursor, table="testTable1"):
    data=[]

    columns=table_read.tableColumns(table)
    columns=columns['Columns']
    
    sql="SELECT * FROM "+table
    mycursor.execute(sql)
    for row in mycursor.fetchall():
        row=list(row)
        d={}
        for i,column in enumerate(columns):
            d[column]=row[i]
        data.append(d)
    mycursor.close()
    return data

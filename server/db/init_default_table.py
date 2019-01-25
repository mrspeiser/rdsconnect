import server.db.table_operations.table_create as table_create

# def conn():
#     config=config_read.read_db_config()
#     try:  
#         return mysql.connector.connect(**config)
#     except mysql.connector.Error as err:
#         print("Something went wrong trying to connect: {}".format(err))

def initializeDefaultTable():
    table_create.createDefaultTable()

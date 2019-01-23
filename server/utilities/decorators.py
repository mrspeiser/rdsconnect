from functools import wraps

def rdsConnect(original):
    import mysql.connector 
    from configparser import ConfigParser
    import server.config.config_read as config_read
    
    @wraps(original)
    def wrapper(*args, **kwargs):
        try:
            config=config_read.read_db_config()  
            connection=mysql.connector.connect(**config)
            mycursor=connection.cursor()
            
            returnValue=original(mycursor, *args, **kwargs)
            
            connection.commit()
            connection.close()
            return returnValue
        except mysql.connector.Error as Err:
            print("Error inside rdsConnect, could not connect to DB. Err: {}".format(Err))
        finally:
            connection.close()
    return wrapper


import mysql.connector
from configparser import ConfigParser
import server.config.config_read as config_read

def conn():
    config=config_read.read_db_config()
    try:  
        return mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        print("Something went wrong trying to connect: {}".format(err))


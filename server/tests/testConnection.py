import sys,os
import mysql.connector 
from configparser import ConfigParser


def read_db_config(filename='server/config/config.ini', section='rds'):
    # create parser and read ini configuration file
    parser=ConfigParser()
    out=parser.read(filename)
    db={}
    if parser.has_section(section):
        items=parser.items(section)
        for item in items:
            db[item[0]]=item[1]
    else:
        raise Exception('{0} not found in the {1} file '.format(section, filename))
    
    return db

try:
    config=read_db_config()  
    connection=mysql.connector.connect(**config)
    mycursor=connection.cursor()
    connection.close()
    print(0)
except mysql.connector.Error as Err:
    print("Error, could not connect to RDS database. Err: {}".format(Err))
    print(1)


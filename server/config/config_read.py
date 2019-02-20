from configparser import ConfigParser

def readConfigFile(filename='config.ini'):
    parser=ConfigParser()
    parser.read(filename)

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

def read_config_value(option, section, filename='server/config/config.ini'):
    parser=ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        if option in parser[section]:
            return parser[section][option]
        else:
            return "Error, option {} not found inside section {}".format(option, section)    
    else:
        return "Error, section {} not found inside file {}".format(section, filename)

# def getConfigValue(tableName, key='requiredClientFields'):
#     parser=ConfigParser()
#     parser.read('server/config/config.ini')
#     if parser.has_section(tableName):
#         section=parser.items(tableName)
#         dictionary=dict(section)
#         for key in dictionary: # For some reason this function works when I use this for loop, if I get rid of this loop the function breaks
#             print(key)
#         required=dictionary[key]
#         return required
#     else:
#         return "Error, field {} not found inside section {}".format(key, tableName)

# def allowInsecure(section, key):
#     parser = ConfigParser()
#     parser.read('server/config/config.ini')
#     if parser.has_section(section):
#         return bool(parser[section][key])
#     else:
#         return "Error, field {} not found inside section {}".format(key, section)

# def getValidHosts(section="security", key="validhosts"):
#     parser=ConfigParser()
#     parser.read('server/config/config.ini')
#     section=parser.items(section)
#     dictionary=dict(section)
#     hosts=dictionary[key]
#     hostlist=hosts.split(",")
#     return hostlist


from configparser import ConfigParser

def readConfigFile(filename='config.ini'):
    parser=ConfigParser()
    parser.read(filename)

def read_db_config(filename='server/config/config.ini', section='mysql'):
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

def getConfigValue():
    pass

def allowInsecure(section, key):
    parser = ConfigParser()
    parser.read('server/config/config.ini')
    section=parser.items(section)
    dictionary=dict(section)
    return bool(dictionary[key])

def getValidHosts(section="security", key="validhosts"):
    parser=ConfigParser()
    parser.read('server/config/config.ini')
    section=parser.items(section)
    dictionary=dict(section)
    hosts=dictionary[key]
    hostlist=hosts.split(",")
    return hostlist


import configparser


def write_db_config_section(section):
    # create parser and read ini configuration file
    config=configparser.ConfigParser()
    config[section] = {}
    with open('server/config/config2.ini', 'w') as configfile:
        config.write(configfile)
    
def write_db_config_key_value(section,key,value):
    config = configparser.ConfigParser()
    config.read('server/config/config2.ini')
    config[section][key] = value
    with open('server/config/config2.ini', 'w') as configfile:
        config.write(configfile)
import configparser

def configInit():
    print("creating empty config file")
    config = configparser.ConfigParser()
    config['rds'] = {
        'host': '', 
        'port': '', 
        'username': '', 
        'passwd': '', 
        'database':''}
    
    config['security'] = {
        'allowAny':'True', 
        'allowInsecure':'True', 
        'validHosts':'127.0.0.1:5000,127.0.0.1.4500', 
        'Authorization':'rdsPass'}

    with open('server/config/config2.ini', 'w') as configfile:
        config.write(configfile)


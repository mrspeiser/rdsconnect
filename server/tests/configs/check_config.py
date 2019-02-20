from configparser import ConfigParser
# import server.config.config_read as config_read
# import server.config.config_init as config_init
import server.config.config_init as config_init

def configFileExists(file='server/config/config2.ini'):
    parser=ConfigParser()
    out=parser.read(file)

    if len(out) < 1:
        print('configFile does not exist')
        config_init.configInit()

def checkConfigFile(file='server/config/config.ini'):
    try:
        parser=ConfigParser()
        out=parser.read(file)
        emptyFields={}
        defaultSections=['rds', 'security']

        for section in defaultSections:
            check=checkSection(parser, section)
            if len(check) > 0:
                emptyFields[section]=check

        if len(emptyFields.keys()) > 0:
            return emptyFields
        else:
            return True

    except BaseException as err:
        print("Error trying to read file: {} - ERR: {}".format(file, err))
        return "Error trying to read file: {} - ERR: {}".format(file, err)

def checkSection(parser, section):
    try:
        if parser.has_section(section):
                
            items=parser.items(section)
            empty=[]
            for item in items:
                if item[1] == '':
                    empty.append(item[0])
            return empty
        else:
            print("error no section: {}".format(section))

    except BaseException as err:
        print("Error trying to read section: {} - ERR: {}".format(section, err))

from configparser import ConfigParser
# import server.config.config_read as config_read
# import server.config.config_init as config_init


#     # Are all the fields empty?
#         # ERROR
#     # Is there a default table?
#         # ERROR
#     # Is there authorization?
#         # WARN

def checkAll(file='../../config/config.ini'):
    # file='../../config/config.ini'
    try:
        parser=ConfigParser()
        out=parser.read(file)
        emptyFields={}
        defaultSections=['mysql', 'table', 'security']

        for section in defaultSections:
            emptyFields[section]=[]
            check=checkSection(parser, section)
            if len(check) > 0:
                emptyFields[section]=check

        return emptyFields

    except BaseException as err:
        print("Error trying to read file: {} - ERR: {}".format(file, err))

def checkSection(parser, section):
    try:
        items=parser.items(section)
        empty=[]
        for item in items:
            if item[1] == '':
                empty.append(item[0])
        return empty
    except BaseException as err:
        print("Error trying to read section: {} - ERR: {}".format(section, err))

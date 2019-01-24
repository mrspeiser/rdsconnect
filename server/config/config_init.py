from configparser import ConfigParser

def configInit():
    pass

def firstInitialization():
    endpoint=getEndPoint()
    port=getPort()
    user=getUserName()
    passwd=getPassword()
    database=getDBname()

def getConfigDefaultSections():
    return ['mysql', 'table', 'security']

def printMessage():
    print("Welcome to rdsConnect!")
    print(" ")
    print("Please follow the prompts to get started")
    print("All of these fields are REQUIRED to have a valid value in order for the service to work properly")
    
def getEndPoint():
    return input("Please enter your AWS RDS database endpoint: ")

def getUserName():
    return input("Please enter your username: ")

def getPassword():
    return input("Please enter your password: ")
    
def getDBname():
    return input("Please enter your database name: ")
    
def getPort():
    return input("Please enter your port if it is not 3306 otherwise you can just hit enter: ")

def printSection():
    section=input("enter section title: ")
    readSection(section)

def getParser():
    parser=ConfigParser()
    parser.read("config.ini")
    return parser
    
def createSection(sectionName):
    parser=getParser()

def readSections():
    parser=getParser()
    print("Section Names: {}".format(parser.sections()))

def readSection(section):
    parser=getParser()
    fields=parser.items(section)
    for field in fields:
        print("{}: {}".format(field[0], field[1]))

def deleteSection(sectionName):
    parser=getParser()
    if parser.has_section(sectionName):
        parser.remove_section(sectionName)
    else:
        print("Section: {} not found in configuration".format(sectionName))

def updateSectionName(sectionName, updatedName):
    parser=getParser()
    if parser.has_section(sectionName):
        parser[sectionName] = updatedName
    else:
        print("Error: section name: {} , not found".format(sectionName))


def createSectionField(section, key, value):
    parser=getParser()
    if parser.has_section(section):
        # parser.set(section, key, value)
        parser[section][key] = value
    else:
        print("Error: section name: {} , not found".format(section))

def readSectionField(section, key):
    parser=getParser()
    if parser.has_section(section):
        print(parser[section][key])
    else:
        print("Error: section name: {} , not found".format(section))

def updateSectionField(section, key, value):
    parser=getParser()
    if parser.has_section(section):
        parser[section][key] = value
    else:
        print("Error: section name: {} , not found".format(section))

def deleteSectionField(section, key):
    parser=getParser()
    if parser.has_section(section):
        if key in parser:
            parser.pop(key, None)
    else:
        print("Error: section name: {} , not found".format(section))
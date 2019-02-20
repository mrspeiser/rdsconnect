import re
from server.config.config_read import read_config_value

def hasValidIncoming(data, table):

    if matchesKeys(data, table) != True:
        return matchesKeys(data,table)
    
    if hasMinimum(data) != True:
        return hasMinimum(data)

    if validEmail(data["email"]) != True:
        return validEmail(data["email"])

    if ValidTextData(data) != True:
        return ValidTextData(data)
    
    if ValidNumerical(data) != True:
        return ValidNumerical(data)
    
    if ValidBody(data) != True:
        return ValidBody(data)
    
    return True
   

def matchesKeys(json, tableName):
    numKeys=len(json.keys())
    maxKeys=read_config_value('maxkeys', tableName)
    if numKeys > maxKeys:
        return {"Error":"too many keys provided in data"}

    requiredKeys=read_config_value('requiredclientfields', tableName)
    requiredKeys=requiredKeys.split(',')
    for key in json:
        if key in requiredKeys:
            requiredKeys.remove(key)
    
    if len(requiredKeys) > 0:
        return "required Keys not found: {}".format(requiredKeys)
    
    return True

def hasMinimum(data):
    if len(data['first_name']) <= 0 and len(data['first_name']) > 35:
        return "first_name field, length either greater than 35 characters or less than or equal to 0 characters"

    if len(data['last_name']) <= 0 and not len(data['last_name']) > 35:
        return "last_name field, length either greater than 35 characters or less than or equal to 0 characters"

    if validEmail(data['email']) != True:
        return "email is invalid, please check formatting"

    return True

def validEmail(email):
    r=re.compile("([a-zA-Z0-9\.-]{1,30}@[a-zA-Z0-9]{2,12}\.[a-z]{1,3})")
    match=r.match(email)
    if match == None:
        return "email is not formatted correctly: {}".format(email)
    return True

def ValidTextData(data):
    return True

def ValidNumerical(cat):
    return True

def ValidBody(cat):
    return True


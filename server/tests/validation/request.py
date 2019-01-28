from configparser import ConfigParser
import server.config.config_read as config_read
from server.db.table_operations.table_read import tableNames as getTableNames

def hasValidPost(request,table):
    key=request.headers["Authorization"]

    if tableExists(table) != True:
        return tableExists(table)

    # if baseUrlValid(request.base_url) != True:
    #     return baseUrlValid(request.base_url)
    if validAuthFrom(key) != True:
        return validAuthFrom(key)

    if validHeaders(request.headers) != True:
        return validHeaders(request.headers)

    if requestSecure(request.is_secure) != True:
        return requestSecure(request.is_secure)

    if acceptUserAgent(request.user_agent) != True:
        return acceptUserAgent(request.user_agent)

    if nonForwardedAccess(request.access_route) != True:
        return nonForwardedAccess(request.access_route)

    return True

def hasValidGet(request, table):
    key=request.headers["Authorization"]
    
    if validAuthFrom(key) != True:
        return "Error invalid Authorization"

    if tableExists(table) != True:
        return tableExists(table)

    return True

def tableExists(tableName):
    tableNames=getTableNames()
    tableNames=tableNames["tableNames"]
    if any(table[0] == tableName for table in tableNames):
        return True
    return "Invalid table name"

def validAuthFrom(authValue):
    key='';
    with open('.key', 'r') as k:
        key = k.readline()
    print("Authorization: {} - Key: {}".format(authValue, key))

    if "Bearer "+key != authValue:
        return "Error Unauthorized"
    return True

def baseUrlValid(base_url):
    # nothing to check yet
    return True

def validHeaders(headers):
    # checking for valid Host property
    hosts=headers["Host"]
    if checkHost(hosts) != True:
        return checkHost(hosts)
    else:
        return True
        
def checkHost(requestHost):
    hosts=config_read.getValidHosts()
    if requestHost in hosts:
        return True
    else:
        return "invalid Host received in headers"

def requestSecure(request_secure_boolean):
    # checking config file if allowinsecure is set to False
    allowInsecure = config_read.allowInsecure("security", "allowinsecure")
    if allowInsecure == False:
        if request_secure_boolean == True:
            return True
        else: 
            return "Request is insecure, please use https"
    return True

def acceptUserAgent(user_agent):
    # checking user agent, always allow for now
    return True

def nonForwardedAccess(forwarded_list):
    # don't allow forwarded requests
    if len(forwarded_list)>1:
        # add a logger here
        return "forwarded access request"
    return True


    # print(" ")
    # print("request: "+str(request))
    # print("base url: "+str(request.base_url))
    # print("request auth: "+str(request.authorization))
    # print("headers: "+str(request.headers))
    # print("user agent: "+str(request.user_agent))
    # print("request is secure: "+str(request.is_secure))
    # print("request is json: "+str(request.is_json))
    # print("remote address: "+str(request.remote_addr))
    # print("access route: "+str(request.access_route))

    # print(" ")
    # print("request: "+str(request))
    # print("request: "+str(request.path))
    # print("request: "+str(request.full_path))
    # print("request: "+str(request.script_root))
    # print("base url: "+str(request.base_url))
    # print("request auth: "+str(request.authorization))
    # print("headers: "+str(request.headers))

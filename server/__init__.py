from flask import Flask, request
import os
import json

import server.config.config_init as initialize

import server.db.table_operations.table_read as table_read
import server.db.table_operations.table_create as table_create
import server.db.table_operations.table_drop as table_drop
import server.db.table_operations.table_update as table_update

import server.db.queries.retreive as retreive
import server.db.queries.insert as insert

import server.tests.validation.data as validateData
import server.tests.validation.request as validateRequest
import server.tests.configs.check_config as check_config
import server.tests.db.operations as operations
import server.utilities.datetimes as datetimes
import server.utilities.startup as startup
import server.utilities.shutdown as shutdown
import server.utilities.keys as token

def create_app(test_config=None):
    #create and configure app
    app = Flask(__name__, instance_relative_config=True)

    #add startup script here:
    # result=startup.checkEnv()

    print("FLASK APP HAS STARTED")
    @app.errorhandler(404)
    def not_found(e):
        return json.dumps({"Response":404, "Error":"Route Not Found"})

    @app.route("/rds/post/<string:table>", methods=['POST'])
    def postData(table):
        if validateRequest.hasValidPost(request,table) == True:
            data=request.get_json()
            # print("data: {}".format(data))
            data["user_agent"]=str(request.user_agent)
            if validateData.hasValidIncoming(data) == True:
                # print("fully validated {}".format(data))
                data=insert.insertData(data,"messages")
                if "Error" in data:
                    return json.dumps({"Response":500,"Error":data})
                else:
                    return json.dumps({"Response":200,"Message":data})
            else:
                return json.dumps({"Response":202,"Error":validateData.hasValidIncoming(data)})
        else:
            return json.dumps({"Response":400, "Error":validateRequest.hasValidPost(request,table)})
    
    @app.route("/rds/get/<string:table>", methods=['GET'])
    def getData(table):
        if validateRequest.hasValidGet(request,table) == True:
            data=retreive.getall(table)
            return json.dumps({"Response":200, "Data":data}, default=datetimes.myconverter, ensure_ascii=False)
        else:
            return json.dumps({"Response":400, "Error":validateRequest.hasValidGet(request,table)})

    @app.route("/checkProcedures")
    def appTestRunthrough():
        results=operations.checkProcedures()
        return json.dumps(results, default=datetimes.myconverter, ensure_ascii=False)

    # @app.route("/rds/api_token", methods=['GET'])
    # def generateToken():
    #     if validateRequest.validTokenRequest(request) == True:
    #         return json.dumps({"api_key":token.configureKey()})
    #     else:
    #         return json.dumps({"Response":400, "Error": "Invalid Request for Token"})

    # @app.route("/testConfig")
    # def configTest():
    #     initialize.firstInitialization()
    #     return "Testing config"
    # @app.route("/showall")
    # def showall():
    #     data=retreive.getall("messages")
    #     print(data)
    #     return json.dumps(data, default=datetimes.myconverter, ensure_ascii=False)

    # @app.route("/getTableNames")
    # def getTables():
    #     data=table_read.tableNames()
    #     return json.dumps(data, ensure_ascii=False)

    # @app.route("/createTable")
    # def newTable():
    #     result=table_create.createTable('messages')
    #     return json.dumps(result, ensure_ascii=False)

    # @app.route("/dropTable")
    # def removeTable():
    #     remaining=table_drop.dropTable('ProceduresCheck')
    #     return json.dumps(remaining, ensure_ascii=False)
    
    # @app.route("/createNewColumn")
    # def updateTableColumns():
    #     columnName="user_agent"
    #     table_update.createColumn("messages", columnName)
    #     return "Create column route"

    # @app.route("/getColumns")
    # def retreiveTableCols():
    #     tname="messages"
    #     columns=table_read.tableColumns(tname)
    #     return json.dumps(columns, ensure_ascii=False)
    
    return app
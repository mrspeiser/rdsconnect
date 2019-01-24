from configparser import ConfigParser

import server.db.connect as conn
import server.db.table_operations.table_create as table_create
import server.db.table_operations.table_read as table_read
import server.db.table_operations.table_drop as table_drop
import server.db.queries.insert as insert
import server.db.queries.retreive as retreive
import server.db.queries.update as update
import server.db.queries.delete as delete
import server.utilities.tmpdata as tempData


def initialize():
    pass

def checkProcedures():
    procedures=[]
    procedures.append(table_create.createTable("ProceduresCheck"))
    procedures.append(table_read.tableNames())
    procedures.append({"insertedData":insert.insertData(tempData.getTempData(), "ProceduresCheck")})
    procedures.append({"queryAll":retreive.getall("ProceduresCheck")})
    procedures.append({"updatedData":update.updateRowTest(tempData.getTempDataAlt())})
    procedures.append({"queryAll":retreive.getall("ProceduresCheck")})
    procedures.append(delete.deleteRowTest())
    procedures.append({"tableDrop":table_drop.dropTable("ProceduresCheck")})
    return procedures
    
    
def checkExistingTableNames(tableNames):
    configTableName=str(read_db_tablename_config())
    for name in tableNames:
        if name[0] == configTableName:
            return True
    return False

def read_db_tablename_config(filename="server/db/config.ini", section="table"):
    parser=ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        return parser[section]['tableName']
    else:
        raise Exception("Error, no {0} section found in the {1} file!".format(section, filename))


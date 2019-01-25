import server.tests.configs.check_config as check_config
import server.tests.db.operations as test_db_operations

def checkEnv():
    applicationStatus={
        "runnable":True,
        "config_status":{"status":True},
        "db_operations_status":{"status":True}
    }

    check_config.configFileExists()

    if check_config.checkConfigFile() != True:
        applicationStatus["runnable"] = False
        applicationStatus["config_status"]["status"] = False
        applicationStatus["config_status"]["Error"] = "Configuration File is missing required parameters"
    
    if test_db_operations.checkDbOperations() != True:
        applicationStatus["runnable"] = False
        applicationStatus["db_operations_status"]["status"] = False
        applicationStatus["db_operations_status"]["Error"] = "Could not complete running all Database procedures"
    
    print(applicationStatus)
    return applicationStatus

        
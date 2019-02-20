# from server.db.table_operations.table_create import createTable

class tablePreProcessor:
    def __init__(self,tableName):
        self.tableName=tableName
        self.columns=[]
        self.requiredclientfields=""


def createTableCLI():
    
    tableName=input("enter a table name: ")
    newTable=tablePreProcessor(tableName)
    print(" ")
    print("to print out current columns enter P")
    print("to attempt creation of table enter: RUN")
    print("to add another column enter: ADD ")
    print("to quit and cancel enter: Q ")

    while True:
        print(" ")
        print("Print - P, RUN - R, ADD - A, Quit - Q")
        print(" ")
        choice=input("Enter next action: ")
        print(choice)
        
        if choice == "Q":
            print('quitting')
            break
        # elif choice == "P":
        #     print('choice matched P')
        #     for col in newTable.columns:
        #         print(col)
        elif choice == "RUN":
            print('choice matched R')
            # sql="" 
            # for col in newTable.columns:
            #     sql+=str(col)
            # createTable(newTable.tableName, sql, newTable.requiredclientfields, len(newTable.columns)-1)
            print("running sql into cursor")
        elif choice == "ADD":
            print('choice matched A')
            newTable=addColumnsloop(newTable)

        else:
            print("sorry nothing matched")

        print('exiting cli')
        break


def addColumnsloop(newTable):
    while True:    
        columnName=input('enter column name, ex: id ')
        datatype=input('enter datatype ex: VARCHAR(255) INT')
        constraint=input('enter constraint ex: NOT NULL DEFAULT \'defaultValue\' or AUTO_INCREMENT PRIMARY KEY ')
        requiredField=input('is this a required field the client must provide? Enter Y or N')
        print(" ")
        print("{} {} {}".format(columnName, datatype, constraint))
        print(" ")
        print("IS THIS CORRECT?")
        confirm=input('enter Y if correct: ')
        if confirm == 'Y':
            if requiredField == 'Y':
                if newTable.requiredclientfields == '':
                    newTable.requiredclientfields+=columnName
                else:    
                    newTable.requiredclientfields+=','+columnName    
            newTable.columns.append("{} {} {}".format(columnName, datatype, constraint)) 

            cont=input("Continue?")
            if cont== 'y' or 'Y':
                continue
            else:
                "exiting sql string"
                break
        else:
            print("restarting")
            continue 
    return newTable 

createTableCLI()
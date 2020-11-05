import os
import subprocess
import time
import sys

'''
os.chdir("/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/mysql_ini")
iniDir = os.getcwd()
iniFiles = os.listdir()

for iniFile in iniFiles:
    SETTINGS = iniFile
    print("Opening file " + iniFile)
    args = ["head", SETTINGS] # define the parameters for the .exe
    proc = subprocess.Popen(args)
    try:
        proc.wait()
        time.sleep(3)
        print("finished!\n")
    except:
        sys.exit()
'''

import json
x = '{ "name":"John", "age":30, "city":"New York"}'
print(json.dumps(x, indent=4))



x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json.dumps(x)

# default value is (,, :)
json.dumps(x, indent=4, separators=(". ", "= "))

json.dumps(x, indent=2, separators=("", "="), sort_keys=False)

mysqlDefaultSettings = {
    'sourcefilename':'<Your mdb files directory>',
    'sourceusername':'',
    'sourcepassword':'',
    'sourcesystemdatabase':'',
    'destinationmethod':'DIRECT',
    'destinationhost':'<Your MySQL Server Host>',
    'destinationport':3306,
    'destinationusername':'<Your MySQL Username>',
    'destinationpassword':'<Your MySQL Password>',
    'destinationdatabase':'<Your destinationdatabase. Leave it default and the program will create a database with the same name as your mdb file.>',
    'storageengine':'InnDB',
    'destinationdumpfilename':'',
    'sourcetables[]':'<default convert all of the tables>',
    'dropdatabase':1,
    'createtables':1,
    'unicode':1,
    'autocommit':1,
    'transferdefaultvalues':1,
    'transferindexes':1,
    'transferautonumbers':1,
    'transferrecords':1,
    'columnlist':1,
    'tableprefix':'',
    'negativeboolean':0,
    'ignorelargeblobs':0,
    'memotype':'LONGTEXT',
    'datetimetype':'DATETIME'
}

# ini file
json.dumps(mysqlDefaultSettings, indent=2, separators=("", "="), sort_keys=False)

# default settings
json.dumps(mysqlDefaultSettings, sort_keys=False)

import os
import re
os.chdir('/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/programs')
os.listdir()

with open ("mysqlDefaultSettings.json", "w") as f:
    #json.dump(mysqlDefaultSettings, f)
    #json.dump(mysqlDefaultSettings, f, indent=2, separators=("", "="), sort_keys=False)
    json.dump(mysqlDefaultSettings, f, indent=4, sort_keys=False)

with open ("mysqlDefaultSettings.json", "r") as f:
    data = json.load(f)

for i in data.items():
    print(i.strip)

def loadSQLSettings(settingsType = None):
    os.chdir(self.programDir)

    mysqlDefaultSettings = {
    'sourcefilename':'<Your mdb files directory>',
    'sourceusername':'',
    'sourcepassword':'',
    'sourcesystemdatabase':'',
    'destinationmethod':'DIRECT',
    'destinationhost':'<Your MySQL Server Host>',
    'destinationport':3306,
    'destinationusername':'<Your MySQL Username>',
    'destinationpassword':'<Your MySQL Password>',
    'destinationdatabase':'<Your destinationdatabase. Leave it default and the program will create a database with the same name as your mdb file.>',
    'storageengine':'InnDB',
    'destinationdumpfilename':'',
    'sourcetables[]':'<default convert all of the tables>',
    'dropdatabase':1,
    'createtables':1,
    'unicode':1,
    'autocommit':1,
    'transferdefaultvalues':1,
    'transferindexes':1,
    'transferautonumbers':1,
    'transferrecords':1,
    'columnlist':1,
    'tableprefix':'',
    'negativeboolean':0,
    'ignorelargeblobs':0,
    'memotype':'LONGTEXT',
    'datetimetype':'DATETIME'
    }

    if "export_MySQL_settings.json" not in os.listdir():
        with open ("export_MySQL_settings.json", "w") as f:
            json.dump(mysqlDefaultSettings, f, indent=4, sort_keys=False)
    else:
        print("Loading 'export_MySQL_settings.json' successfully!\nIf you want to use the default settings, delete 'export_MySQL_settings.json', and restart this program.")

    with open ("mysqlDefaultSettings.json", "r") as f:
        self.userSettings = json.load(f)


re.findall("^[<][a-zA-Z0-9]*", data["sourcefilename"])

# update: add function: query data


import sys
import subprocess

subprocess.run("pip list")

try:
    import skp
except:
    print("Please install module 'mysql.connector'")
    sys.exit()

sys.exit()
import skp

os.getcwd()

mdbFile = "xtreme.mdb"
mdbTxt = "xtreme.txt"
args = ['mdb-schema', mdbFile, '>', mdbTxt]
subprocess.run(args).args # generate mdb Schemas

proc = subprocess.run("ls")
proc.args

subprocess.run("ls {0}".format("~/Desktop"), shell=True).stdout
proc = subprocess.run("ls {0}".format("~/Desktop"), shell=True, capture_output=True)
proc

help(subprocess)
dir(subprocess)

os.system("ls")

proc = subprocess.run('ls ~/Desktop',shell=True,stdout=PIPE,stderr=PIPE)
proc.stdout

import json
import mysql.connector

#def validateMySQLRecords(self, databaseType):
#os.chrdir(self.programDir)
os.chdir('/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/programs')

os.listdir()

with open('mdb2mysql.json') as f:
    userSettings = json.load(f)
    dbUsername = userSettings['destinationusername']
    dbPasswd = userSettings['destinationpassword']
    dbHost = userSettings['destinationhost']
    dbPort = int(userSettings['destinationport'])


dbConnection = mysql.connector.connect(
    host = dbHost,
    user = dbUsername,
    password = dbPassword,
    port = dbPort,
    database = 'xtreme'
    )

dbCursor = dbConnection.cursor()

dbCursor.execute('SHOW TABLES')
dbTables = dbCursor.fetchall()
for dbTable in dbTables:
    dbTable = dbTable[0]
    print('Table: ' + dbTable)
    dbCursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
    dbRecords = dbCursor.fetchall()[0][0]
    print('Records: ' + str(dbRecords))
    #print('')

s = 'y'

if s == y print(1) else print(2)

print(1 if s == 'y' else 2)

def out(s):
    print(s)

n = 1
out(s='y' if n == 1 else s='n')


Exporting DB RptDB-01
Export DB RptDB-01: Successful!
Export DB RptDB-01: Failed!
Exporting DB RptDB-01_mysql
Export DB RptDB-01_mysql: Successful!
Export DB RptDB-01_mysql: Failed!

Handling DB RptDB-01_dump
Dump DB RptDB-01_dump: Successful!

Handling DB RptDB-01
Export DB RptDB-01: Successful!
Export DB RptDB-01: Failed!
Handling DB RptDB-02_dump
Dump DB RptDB-02_dump: Successful!

Handling DB RptDB-02

Exporting DB RptDB-02

f = 'xtreme_dump'
import re
re.findall("_dump$", iniFile)

iniFile = 'xtreme_dump_mysql.ini'
iniFile = 'xtreme_mysql.ini'

iniFile.split('_mysql.ini')[0]


mdbName = iniFile # get the ini file name without extension and DB type
mdbName = mdbName[::-1]
mdbName = mdbName.split("_", 1)
mdbName = mdbName[-1]
mdbName = mdbName[::-1]
mdbName

name = 'name'
value = 5
js = {name: value}
js

#####
%reset -f

import sys
import os
import mysql.connector
import json

rootDir = '/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini'
programDir = '/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/programs'
os.chdir(programDir)

mdbName = 'xtrdb'
with open('mdb2mysql.json') as f:
    userSettings = json.load(f)
    dbUsername = userSettings['destinationusername']
    dbPassword = userSettings['destinationpassword']
    dbHost = userSettings['destinationhost']
    dbPort = int(userSettings['destinationport'])

dbConnection = mysql.connector.connect(
    host = dbHost,
    user = dbUsername,
    password = dbPassword,
    port = dbPort,
    database = mdbName
    )

if dbConnection.is_connected() is False:
    sys.exit()

# write log into mdb_ini_Exporter.log
dbCursor = dbConnection.cursor()
dbCursor.execute('SHOW TABLES')
dbTables = dbCursor.fetchall()

for dbTable in dbTables:
    dbTable = dbTable[0]
    dbCursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
    dbRecords = dbCursor.fetchall()[0][0]
    with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
        f.write('Table: ' + dbTable + '\n')
        f.write('Records: ' + str(dbRecords) + '\n')

with open("mdb_ini_Exporter.log", "a", newline="\n") as f:
    f.write('\n')

####
mysql_recordsDir = rootDir + '/mysql_records/'

dbConnection = mysql.connector.connect(
    host = dbHost,
    user = dbUsername,
    password = dbPassword,
    port = dbPort,
    database = mdbName
    )

if dbConnection.is_connected() is False:
    sys.exit()

dbCursor = dbConnection.cursor()
dbCursor.execute('SHOW TABLES')
dbTables = dbCursor.fetchall()

os.chdir(mysql_recordsDir)
recordsJsonFile = mdbName + '.json'
dbJson = {}
for dbTable in dbTables:
    dbTable = dbTable[0]
    dbCursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
    dbRecords = dbCursor.fetchall()[0][0]
    dbJson[dbTable] = dbRecords

with open(recordsJsonFile, "w", newline="\n") as f:
    json.dump(dbJson, f, indent=4, sort_keys=False) 


###

def hexo(x):
    if x == 1:
        print(1)
    elif x == 2:
        print(2)
    elif x == 3:
        print(3)

while True:
    try:
        x = int(input("Please enter a number from the options:"))
        if x in [1, 2, 3]:
            hexo(x)
            # break
        else:
            print("This is an inviald number!")
    except ValueError:
        print("This is not a number!")

###

def hexo(x):
    if x == 1:
        print(1)
    elif x == 2:
        print(2)
    elif x == 3:
        print(3)

while True:
    try:
        x = int(input("Please enter a number from the options:"))
        if x in [1, 2, 3]:
            hexo(x)
            break # The import stop
        else:
            print("This is an inviald number!")
    except ValueError:
        print("This is not a number!")


####### connect to mssql

import sys
import os
import json
import pyodbc




Server=myServerAddress;Database=myDataBase;User Id=myUsername;Password=myPassword;

MSSQL
sql19.c9d5goyg8g3a.us-east-1.rds.amazonaws.com
admin
myPassWord_123
SQL

import json
import pymssql
import os

rootDir = '/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini'
programDir = '/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/programs'
os.chdir(programDir)

mdbName = 'xtreme'
with open('mdb2mssql.json') as f:
    userSettings = json.load(f)
    dbUsername = userSettings['destinationusername']
    dbPassword = userSettings['destinationpassword']
    dbServer = userSettings['destinationserver']
    dbAuth = userSettings['destinationauthentication']

conn = pymssql.connect(
    server=dbServer,
    user=dbUsername,
    password=dbPassword,
    database=mdbName
    )

conn = pymssql.connect(
    server='sql19.c9d5goyg8g3a.us-east-1.rds.amazonaws.com',
    user='admin',
    password='myPassWord_123',
    database=mdbName
    )

cursor = conn.cursor()

dir(cursor)

cursor.execute("SELECT TABLE_NAME from INFORMATION_SCHEMA.TABLES")
dbTables = cursor.fetchall()
# dbTables[0][0]

## bug fixes

import datetime

datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
datetime.datetime.now().time().strftime("%Y-%m-%d %H:%M:%S")

startTime = datetime.datetime.now()
endTime = datetime.datetime.now()

procTime = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute, seconds=endTime.second) - datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)

## connect to postgresql

import os
import sys
import json
import psycopg2


rootDir = '/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini'
programDir = '/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/programs'
os.chdir(programDir)

mdbName = 'xtreme'
with open('mdb2postgresql.json') as f:
    userSettings = json.load(f)
    dbUsername = userSettings['destinationusername']
    dbPassword = userSettings['destinationpassword']
    dbServer = userSettings['destinationserver']
    dbPort = userSettings['destinationport']

cnx = psycopg2.connect(
    database=mdbName,
    user=dbUsername,
    password=dbPassword,
    host=dbServer,
    port=str(dbPort)
    )

# check connection status
if cnx.status != 1:
    self.outputErrors(errorType='DBConnection', databaseType=databaseType)

# define cursor
cursor = cnx.cursor()


#SELECT table_name FROM information_schema.tables WHERE table_schema='public';

# get all tables name of current database
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
dbTables = cursor.fetchall()

# write log into mdbMigrator.log
for dbTable in dbTables:
    # dbTable = dbTable[0].decode()
    dbTable = dbTable[0]
    cursor.execute('SELECT COUNT(*) FROM "{0}"'.format(dbTable))
    dbRecords = cursor.fetchall()[0][0]
    with open("mdbMigrator.log", "a", newline="\r\n") as f:
        f.write('Table: ' + dbTable + '\n')
        f.write('Records: ' + str(dbRecords) + '\n')

with open("mdbMigrator.log", "a", newline="\r\n") as f:
    f.write('\n')

print("Write records in log file successfully!")

# write records from querying table for each mdb in JSON file
os.chdir(self.mysql_recordsDir)

recordsJsonFile = mdbName + '.json'
dbJson = {}
for dbTable in dbTables:
    # dbTable = dbTable[0].decode()
    dbTable = dbTable[0]
    cursor.execute('SELECT COUNT(*) FROM "{0}"'.format(dbTable))
    dbRecords = cursor.fetchall()[0][0]
    dbJson[dbTable] = dbRecords

with open(recordsJsonFile, "w", newline="\r\n") as f:
    json.dump(dbJson, f, indent=4, sort_keys=False)

print("Write records in JSON file successfully!")

# Close the connection
cnx.close()

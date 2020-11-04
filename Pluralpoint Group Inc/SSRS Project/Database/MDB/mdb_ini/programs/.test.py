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
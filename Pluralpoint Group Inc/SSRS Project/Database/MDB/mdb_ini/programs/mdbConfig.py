#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: mdbConfig.py                                                      #
# File Path: /mdbConfig.py                                                     #
# Created Date: 2020-10-19                                                     #
# -----                                                                        #
# Company: Pluralpoint Group Inc.                                              #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-11-10 3:56:38 pm                                         #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Pluralpoint Group Inc.                                    #
################################################################################

import os
import subprocess
import sys
import shutil  # module for moving file
import re
import json
import numpy as np
from datetime import datetime


class mdbConfig:
    def __init__(self):
        # Path definition
        self.programDir = os.getcwd()
        os.chdir("..")  # now we are in the root
        self.rootDir = os.getcwd()
        self.mdbDir = self.rootDir+"/mdb/"
        self.schemasDir = self.rootDir + "/schemas/"
        if ("schemas" in os.listdir(self.rootDir)) is False:
            os.mkdir("schemas")

        os.chdir(self.programDir)

        # Create README.txt
        with open("README.md", "w", newline="\r\n") as f:
            f.write("## Prerequisite for `mdbConfig.py`:\n")
            f.write("__IMPORTANT__: Run `mdbConfig.py` on your MacBook or Linux before run `mdbMigrator.py.`\n")
            f.write("__ENV: MacOS or Linux, Python 3.7x, PIP.__\n")
            f.write("1. Make a directory named `programs` to store `mdbConfig.py` and `mdbMigrator.py`.\n")
            f.write("2. Make a directory named `mdb` to store mdb files.\n")
            f.write("3. Search `mdbtools` online and install it.\n")
            f.write("4. Module requirements: `numpy`.\n")
            f.write("---\n")
            f.write("## Prerequisite for `mdbMigrator.py`:\n")
            f.write("__IMPORTANT__: Run `mdbMigrator.py` on your Windows after run `mdbConfig.py`\n")
            f.write("__ENV: Windows, Python 3.7x, PIP.__\n")
            f.write("1. Make a directory named `programs` to store `mdbConfig.py` and `mdbMigrator.py`.\n")
            f.write("2. Make a directory named `mdb` to store mdb files.\n")
            f.write("3. Copy all of the following directories from your MacOS or Linux to Windows: `programs`, `mdb`, `*_ini`.\n")
            f.write("4. Modules Required: `mysql.connector`, `pymssql`, `psycopg2`, `mariadb`\n")
            f.write("- P.S: A better solution is sharing a folder through Windows and MackBook/Linux. And let them sync the files and directories automatically.\n")
            f.write("---\n")
            f.write("Sample .ini files:\n")
            f.write("- MySQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mysql.ini\n")
            f.write("- MSSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mssql.ini\n")
            f.write("- PostgreSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2prgsql.ini\n")

        os.chdir(self.rootDir)
        if "mdb" not in os.listdir(self.rootDir):
            print("Please make a directory with the name 'mdb' that in the partent directory of this program!")
            sys.exit()

    # main function
    def main(self):
        # get user target DB type
        print("Which type of DB do you prefer to convert to:\n1. MySQL\n2. MSSQL\n3. PostgreSQL\n4. MariaDB\nq. q for Quit")

        while True:
            try:
                targetDB = input("Input the number here: ")
                if targetDB in ['1', '2', '3', '4']:
                    break
                elif targetDB == 'q':
                    sys.exit()
                else:
                    print("Please input an valid number!\n")
            except ValueError:
                print("Please input an number!\n")
            finally:
                self.generateSchemas()

        if targetDB == '1':
            self.loadMySQLSettings()
            os.chdir(self.schemasDir)
            for self.mdbSchema in self.mdbSchemas:
                self.loadSchemas()
                self.iniMySQL()
                self.iniMySQL(DUMP='y')
        elif targetDB == '2':
            self.loadMSSQLSettings()
            os.chdir(self.schemasDir)
            for self.mdbSchema in self.mdbSchemas:
                self.loadSchemas()
                self.iniMSSQL()
                self.iniMSSQL(DUMP='y')
        elif targetDB == '3':
            self.loadPostgreSQLSettings()
            os.chdir(self.schemasDir)
            for self.mdbSchema in self.mdbSchemas:
                self.loadSchemas()
                self.iniPostgreSQL()
                self.iniPostgreSQL(DUMP='y')
        elif targetDB == '4':
            self.loadMariaDBSettings()
            os.chdir(self.schemasDir)
            for self.mdbSchema in self.mdbSchemas:
                self.loadSchemas()
                self.iniMariaDB()
                self.iniMariaDB(DUMP='y')
        else:
            self.outputErrors('invalidInput')

    # Generate the Schemas for each mdb
    def generateSchemas(self):
        # Get mdb files name
        # find all .mdb files, and store their name with .mdb in list mdbFiles
        os.chdir(self.mdbDir)

        if os.listdir(self.mdbDir) == []:
            print("Please put the .mdb files in mdb directory that in the parent directory of this program!")
            sys.exit()

        mdbFiles = []
        for i in os.listdir(self.mdbDir):
            if re.findall("[.]mdb$", i) != []:
                mdbFiles.append(i)

        os.chdir(self.rootDir)

        # run mdbtools for generating schemas, and give the schemas a extension with .txt
        os.chdir(self.schemasDir)

        # Generate mdb Schemas
        # give mdb schemas extensions with .txt
        os.chdir(self.mdbDir)
        self.mdbSchemas = []
        for mdbFile in mdbFiles:
            mdbTxt = re.split("[.]mdb", mdbFile)  # split .mdb, return a list
            mdbTxt = mdbTxt[0]  # get the first item, which is the mdb name
            mdbTxt += '.txt'  # add the extension .txt to schema files
            self.mdbSchemas.append(mdbTxt)
            subprocess.run("mdb-schema {0} > {1}".format(mdbFile, mdbTxt), shell=True)
            shutil.move(mdbTxt, self.schemasDir + mdbTxt)

    def loadSchemas(self):
        os.chdir(self.schemasDir)

        # Read the schema file
        file = open(self.mdbSchema, "r")
        self.schema = file.read().splitlines()  # self.schema is the whole content of a schema file
        file.close()

        # Extract the schema
        # Get the start index & end index of each table
        # Grab the statement with "CRATE TABLE" statement, which is the 'startIndex'
        startIndex = []  # startIndex: in schema, the items start with "CREATE" is a create table statement block
        for i in self.schema:
            if re.findall("^CREATE", i) != []:
                startIndex.append(self.schema.index(i))

        # define endIndex: start from the second item of startIndex, everyone - 2 is the endIndex
        endIndex = startIndex.copy()
        del endIndex[0]  # so I delete the first item
        endIndex = np.array(endIndex) - 2  # temporarily convert endIndex to array object, then - 2
        endIndex = list(endIndex)  # convert it back to list object
        endIndex.append(len(self.schema)-3)  # add the last ");" index

        # define queryIndices storing the startIndex & endIndex for the range of the query statement
        queryIndices = []
        for s, e in zip(startIndex, endIndex):
            queryIndices.append([s, e])

        # get the full indices from startIndex to endIndex, then get the table name and column name.
        # Grab each table with columns
        tableIndices = []  # define the whole table
        for i in queryIndices:
            tableBlock = range(i[0], i[1])
            tableContent = []
            for i in tableBlock:
                try:
                    startItem = re.search(r'\[', self.schema[i]).start()
                except AttributeError:
                    pass
                else:
                    endItem = re.search(r'\]', self.schema[i]).end()
                    tableContent.append(self.schema[i][startItem+1:endItem-1])
            tableIndices.append(tableContent)

        # get table name and columns name
        self.sourcetables = []  # self.source for ini files outputing
        for eachTable in tableIndices:
            self.sourcetables.append(eachTable[0])  # add table name as the first item
            for i in eachTable[1:]:  # grab column names from the second line
                self.sourcetables.append(eachTable[0] + '\\' + i)  # add columns name as the rest items

    # Load the settings of exporting to MySQL.
    # If there is no settings file, create it.
    # If the settings file is all default, then use the default settings.
    def loadMySQLSettings(self):
        os.chdir(self.programDir)
        
        mysqlDefaultSettings = {
        'ATTENTION':'PLEASE REMOVE < > IN THE FOLLOWING FIELDS.',
        'sourcedirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\mdb\\>',
        'dumpfiledirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\dumps\\>',
        'sourceusername':'<If no username, leave it as default>',
        'sourcepassword':'<If no password, leave it as default>',
        'sourcesystemdatabase':'<If no specified database, leave it as default>',
        'destinationmethod':"DIRECT",
        'destinationhost':'<Your DB Server Host>',
        'destinationport':3306,
        'destinationusername':'<Your DB Username>',
        'destinationpassword':'<Your DB Password>',
        'destinationdatabase':'<Your destination database. Leave it as default and the program will create a database with the same name as your mdb file.>',
        # 'storageengine':"<Select one of the following engine:'ARCHIVE', 'DBD', 'Brighthouse', 'CSV', 'Falcon', 'InnoDB', 'Maria', 'MyISAM'>",
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
        'ignorelargeblobs':0
        }

        if "mdb2mysql.json" not in os.listdir():
            print("\nCreate default settings file named 'mdb2mysql.json' for exporting mdb to MySQL successfully.")
            print("Please customize the settings in 'mdb2mysql.json' as you need. Then run this program again.")
            with open("mdb2mysql.json", "w") as f:
                json.dump(mysqlDefaultSettings, f, indent=4, sort_keys=False)
            sys.exit()  # exit the program after creating the default settings
        else:
            print("\nLoading 'mdb2mysql.json' successfully!\nIf you want to use the default settings, delete 'mdb2mysql.json', and restart this program.")

        with open("mdb2mysql.json", "r") as f:
            self.userSettings = json.load(f)

    # generate .ini file for MySQL
    def iniMySQL(self, DUMP=None):
        os.chdir(self.rootDir)

        if "mysql_ini" not in os.listdir(self.rootDir):
            os.mkdir("mysql_ini")

        mysql_iniDir = self.rootDir + "/mysql_ini/"
        os.chdir(mysql_iniDir)

        self.mdbSchema = self.mdbSchema.replace(".txt", "")  # remove the .txt extension

        if DUMP is None:
            extension = "_mysql.ini"
        elif DUMP == 'y':
            extension = '_dump_mysql.ini'

        with open(self.mdbSchema + extension, "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to MySQL]\n")

            # define sourcefilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['sourcedirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'sourcedirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['sourcedirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['sourcedirectory'] += '\\'
            f.write("  sourcefilename=" + self.userSettings['sourcedirectory'] + self.mdbSchema + ".mdb\n")

            # define sourceusername
            if re.findall('^[<]|[>]$', self.userSettings['sourceusername']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourceusername'] = ''
            f.write("  sourceusername=" + self.userSettings['sourceusername'] + "\n")

            # define sourcepassword
            if re.findall('^[<]|[>]$', self.userSettings['sourcepassword']) == ['<', '>']:
                self.userSettings['sourcepassword'] = ''
            f.write("  sourcepassword=" + self.userSettings['sourcepassword'] + "\n")

            # define sourcesystemdatabase
            if re.findall('^[<]|[>]$', self.userSettings['sourcesystemdatabase']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourcesystemdatabase'] = ''
            f.write("  sourcesystemdatabase=" + self.userSettings['sourcesystemdatabase'] + "\n")

            # define destinationmethod
            if DUMP is None:
                f.write("  destinationmethod=DIRECT\n")
            elif DUMP == 'y':
                f.write("  destinationmethod=DUMP\n")

            # define destinationhost
            if re.findall('^[<]|[>]$', self.userSettings['destinationhost']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationhost')
            f.write("  destinationhost=" + self.userSettings['destinationhost'] + "\n")

            # define destinationport
            f.write("  destinationport=" + str(self.userSettings['destinationport']) + "\n")

            # define destinationusername
            if re.findall('^[<]|[>]$', self.userSettings['destinationusername']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationusername')
            f.write("  destinationusername=" + self.userSettings['destinationusername'] + "\n")

            # define destinationpassword
            if re.findall('^[<]|[>]$', self.userSettings['destinationpassword']) == ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationpassword')
            f.write("  destinationpassword=" + self.userSettings['destinationpassword'] + "\n")

            # define destinationdatabase
            if re.findall('^[<]|[>]$', self.userSettings['destinationdatabase']) + ['<', '>'] != ['<', '>']:
                f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            else:
                f.write("  destinationdatabase=" + self.userSettings['destinationdatabase'] + "\n")

            # define storageengine
            '''
            if re.findall('^[<]|[>]$', self.userSettings['storageengine']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'storageengine')

            if self.userSettings['storageengine'] in ['ARCHIVE', 'DBD', 'Brighthouse', 'CSV', 'Falcon', 'InnoDB', 'Maria', 'MyISAM']:
                f.write("  storageengine=" + self.userSettings['storageengine'] + "\n")
            else:
                self.outputErrors('invalidSetting', 'storageengine')
            '''
            f.write("  storageengine=" + "InnoDB\n")

            # define destinationdumpfilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['dumpfiledirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'dumpfiledirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['dumpfiledirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['dumpfiledirectory'] += '\\'
            f.write("  destinationdumpfilename=" + self.userSettings['dumpfiledirectory'] + self.mdbSchema + ".sql\n")

            # define sourcetables[]
            f.write("  sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')

            # define dropdatabase
            if self.userSettings['dropdatabase'] in [0, 1]:
                f.write("  dropdatabase=" + str(self.userSettings['dropdatabase']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'dropdatabase')

            # define createtables
            if self.userSettings['createtables'] in [0, 1]:
                f.write("  createtables=" + str(self.userSettings['createtables']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'createtables')

            # define unicode
            if self.userSettings['unicode'] in [0, 1]:
                f.write("  unicode=" + str(self.userSettings['unicode']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'unicode')

            # define autocommit
            if self.userSettings['autocommit'] in [0, 1]:
                f.write("  autocommit=" + str(self.userSettings['autocommit']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'autocommit')

            # define transferdefaultvalues
            if self.userSettings['transferdefaultvalues'] in [0, 1]:
                f.write("  transferdefaultvalues=" + str(self.userSettings['transferdefaultvalues']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferdefaultvalues')

            # define transferindexes
            if self.userSettings['transferindexes'] in [0, 1]:
                f.write("  transferindexes=" + str(self.userSettings['transferindexes']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferindexes')

            # define transferautonumbers
            if self.userSettings['transferautonumbers'] in [0, 1]:
                f.write("  transferautonumbers=" + str(self.userSettings['transferautonumbers']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferautonumbers')

            # define transferrecords
            if self.userSettings['transferrecords'] in [0, 1]:
                f.write("  transferrecords=" + str(self.userSettings['transferrecords']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferrecords')

            # define columnlist
            if self.userSettings['columnlist'] in [0, 1]:
                f.write("  columnlist=" + str(self.userSettings['columnlist']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'columnlist')

            # define tableprefix
            f.write("  tableprefix=" + str(self.userSettings['tableprefix']) + "\n")

            # define negativeboolean
            if self.userSettings['negativeboolean'] in [0, 1]:
                f.write("  negativeboolean=" + str(self.userSettings['negativeboolean']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'negativeboolean')

            # define ignorelargeblobs
            if self.userSettings['ignorelargeblobs'] in [0, 1]:
                f.write("  ignorelargeblobs=" + str(self.userSettings['ignorelargeblobs']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'ignorelargeblobs')

            # define memotype
            f.write("  memotype=LONGTEXT\n")

            # define datetimetype
            f.write("  datetimetype=DATETIME\n")

        self.outputLog("MySQL")

    # Load the settings of exporting to MSSQL.
    # If there is no settings file, create it.
    # If the settings file is all default, then use the default settings.
    def loadMSSQLSettings(self):
        os.chdir(self.programDir)

        mssqlDefaultSettings = {
        'ATTENTION':'PLEASE REMOVE < > IN THE FOLLOWING FIELDS.',
        'sourcedirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\mdb\\>',
        'dumpfiledirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\dumps\\>',
        'sourceusername':'<If no username, leave it as default>',
        'sourcepassword':'<If no password, leave it as default>',
        'sourcesystemdatabase':'<If no specified database, leave it as default>',
        'destinationmethod':'DIRECT',
        'destinationserver':'<Your DB Server Host>',
        'destinationauthentication':'<Your authentication method:SQL or Windows>',
        'destinationusername':'<Your DB Username>',
        'destinationpassword':'<Your DB Password>',
        'destinationdatabase':'<Your destination database. Leave it as default and the program will create a database with the same name as your mdb file.>',
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
        'ignorelargeblobs':0
        }

        if "mdb2mssql.json" not in os.listdir():
            print("\nCreate default settings file named 'mdb2mssql.json' for exporting mdb to MySQL successfully.")
            print("Please customize the settings in 'mdb2mssql.json' as you need. Then run this program again.")
            with open("mdb2mssql.json", "w") as f:
                json.dump(mssqlDefaultSettings, f, indent=4, sort_keys=False)
            sys.exit()  # exit the program after creating the default settings
        else:
            print("\nLoading 'mdb2mssql.json' successfully!\nIf you want to use the default settings, delete 'mdb2mssql.json', and restart this program.")

        with open("mdb2mssql.json", "r") as f:
            self.userSettings = json.load(f)

    # generate .ini file for MySQL
    def iniMSSQL(self, DUMP=None):
        os.chdir(self.rootDir)

        if "mssql_ini" not in os.listdir(self.rootDir):
            os.mkdir("mssql_ini")

        mssql_iniDir = self.rootDir + "/mssql_ini/"
        os.chdir(mssql_iniDir)

        self.mdbSchema = self.mdbSchema.replace(".txt", "")  # remove the .txt extension

        if DUMP is None:
            extension = "_mssql.ini"
        elif DUMP == 'y':
            extension = '_dump_mssql.ini'

        with open(self.mdbSchema + extension, "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to MSSQL]\n")

            # define sourcefilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['sourcedirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'sourcedirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['sourcedirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['sourcedirectory'] += '\\'
            f.write("  sourcefilename=" + self.userSettings['sourcedirectory'] + self.mdbSchema + ".mdb\n")

            # define sourceusername
            if re.findall('^[<]|[>]$', self.userSettings['sourceusername']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourceusername'] = ''
            f.write("  sourceusername=" + self.userSettings['sourceusername'] + "\n")

            # define sourcepassword
            if re.findall('^[<]|[>]$', self.userSettings['sourcepassword']) == ['<', '>']:
                self.userSettings['sourcepassword'] = ''
            f.write("  sourcepassword=" + self.userSettings['sourcepassword'] + "\n")

            # define sourcesystemdatabase
            if re.findall('^[<]|[>]$', self.userSettings['sourcesystemdatabase']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourcesystemdatabase'] = ''
            f.write("  sourcesystemdatabase=" + self.userSettings['sourcesystemdatabase'] + "\n")

            # define destinationmethod
            if DUMP is None:
                f.write("  destinationmethod=DIRECT\n")
            elif DUMP == 'y':
                f.write("  destinationmethod=DUMP\n")

            # define destinationserver
            if re.findall('^[<]|[>]$', self.userSettings['destinationserver']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationserver')
            f.write("  destinationserver=" + self.userSettings['destinationserver'] + "\n")

            # define destinationauthentication
            if re.findall('^[<]|[>]$', self.userSettings['destinationauthentication']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationauthentication')
            if self.userSettings['destinationauthentication'] in ['SQL', 'Windows']:
                f.write("  destinationauthentication=" + self.userSettings['destinationauthentication'] + "\n")
            else:
                self.outputErrors('invalidSetting', 'destinationauthentication')

            # define destinationusername
            if re.findall('^[<]|[>]$', self.userSettings['destinationusername']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationusername')
            f.write("  destinationusername=" + self.userSettings['destinationusername'] + "\n")

            # define destinationpassword
            if re.findall('^[<]|[>]$', self.userSettings['destinationpassword']) == ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationpassword')
            f.write("  destinationpassword=" + self.userSettings['destinationpassword'] + "\n")

            # define destinationdatabase
            if re.findall('^[<]|[>]$', self.userSettings['destinationdatabase']) + ['<', '>'] != ['<', '>']:
                f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            else:
                f.write("  destinationdatabase=" + self.userSettings['destinationdatabase'] + "\n")

            # define destinationdumpfilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['dumpfiledirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'dumpfiledirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['dumpfiledirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['dumpfiledirectory'] += '\\'
            f.write("  destinationdumpfilename=" + self.userSettings['dumpfiledirectory'] + self.mdbSchema + ".sql\n")

            # define sourcetables[]
            f.write("  sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')

            # define dropdatabase
            if self.userSettings['dropdatabase'] in [0, 1]:
                f.write("  dropdatabase=" + str(self.userSettings['dropdatabase']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'dropdatabase')

            # define createtables
            if self.userSettings['createtables'] in [0, 1]:
                f.write("  createtables=" + str(self.userSettings['createtables']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'createtables')

            # define unicode
            if self.userSettings['unicode'] in [0, 1]:
                f.write("  unicode=" + str(self.userSettings['unicode']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'unicode')

            # define autocommit
            if self.userSettings['autocommit'] in [0, 1]:
                f.write("  autocommit=" + str(self.userSettings['autocommit']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'autocommit')

            # define transferdefaultvalues
            if self.userSettings['transferdefaultvalues'] in [0, 1]:
                f.write("  transferdefaultvalues=" + str(self.userSettings['transferdefaultvalues']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferdefaultvalues')

            # define transferindexes
            if self.userSettings['transferindexes'] in [0, 1]:
                f.write("  transferindexes=" + str(self.userSettings['transferindexes']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferindexes')

            # define transferautonumbers
            if self.userSettings['transferautonumbers'] in [0, 1]:
                f.write("  transferautonumbers=" + str(self.userSettings['transferautonumbers']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferautonumbers')

            # define transferrecords
            if self.userSettings['transferrecords'] in [0, 1]:
                f.write("  transferrecords=" + str(self.userSettings['transferrecords']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferrecords')

            # define columnlist
            if self.userSettings['columnlist'] in [0, 1]:
                f.write("  columnlist=" + str(self.userSettings['columnlist']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'columnlist')

            # define tableprefix
            f.write("  tableprefix=" + str(self.userSettings['tableprefix']) + "\n")

            # define negativeboolean
            if self.userSettings['negativeboolean'] in [0, 1]:
                f.write("  negativeboolean=" + str(self.userSettings['negativeboolean']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'negativeboolean')

            # define ignorelargeblobs
            if self.userSettings['ignorelargeblobs'] in [0, 1]:
                f.write("  ignorelargeblobs=" + str(self.userSettings['ignorelargeblobs']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'ignorelargeblobs')

            # define memotype
            f.write("  memotype=VARCHAR(MAX)\n")

            # define datetimetype
            f.write("  datetimetype=DATETIME2\n")

        self.outputLog("MSSQL")

    # Load the settings of exporting to PostgreSQL.
    # If there is no settings file, create it.
    # If the settings file is all default, then use the default settings.
    def loadPostgreSQLSettings(self):
        os.chdir(self.programDir)

        postgresqlDefaultSettings = {
        'ATTENTION':'PLEASE REMOVE < > IN THE FOLLOWING FIELDS.',
        'sourcedirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\mdb\\>',
        'dumpfiledirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\dumps\\>',
        'sourceusername':'<If no username, leave it as default>',
        'sourcepassword':'<If no password, leave it as default>',
        'sourcesystemdatabase':'<If no specified database, leave it as default>',
        'destinationmethod':"DIRECT",
        'destinationserver':'<Your DB Server Host>',
        'destinationport':5432,
        'destinationusername':'<Your DB Username>',
        'destinationpassword':'<Your DB Password>',
        'destinationdatabase':'<Your destination database. Leave it as default and the program will create a database with the same name as your mdb file.>',
        'maintenancedb':'postgres',
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
        'ignorelargeblobs':0
        }

        if "mdb2postgresql.json" not in os.listdir():
            print("\nCreate default settings file named 'mdb2postgresql.json' for exporting mdb to MySQL successfully.")
            print("Please customize the settings in 'mdb2postgresql.json' as you need. Then run this program again.")
            with open("mdb2postgresql.json", "w") as f:
                json.dump(postgresqlDefaultSettings, f, indent=4, sort_keys=False)
            sys.exit()  # exit the program after creating the default settings
        else:
            print("\nLoading 'mdb2postgresql.json' successfully!\nIf you want to use the default settings, delete 'mdb2postgresql.json', and restart this program.")

        with open("mdb2postgresql.json", "r") as f:
            self.userSettings = json.load(f)

    # generate .ini file for MySQL
    def iniPostgreSQL(self, DUMP=None):
        os.chdir(self.rootDir)

        if "postgresql_ini" not in os.listdir(self.rootDir):
            os.mkdir("postgresql_ini")

        postgresql_iniDir = self.rootDir + "/postgresql_ini/"
        os.chdir(postgresql_iniDir)

        self.mdbSchema = self.mdbSchema.replace(".txt", "")  # remove the .txt extension

        if DUMP is None:
            extension = "_postgresql.ini"
        elif DUMP == 'y':
            extension = '_dump_postgresql.ini'

        with open(self.mdbSchema + extension, "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to PostgreSQL]\n")

            # define sourcefilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['sourcedirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'sourcedirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['sourcedirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['sourcedirectory'] += '\\'
            f.write("  sourcefilename=" + self.userSettings['sourcedirectory'] + self.mdbSchema + ".mdb\n")

            # define sourceusername
            if re.findall('^[<]|[>]$', self.userSettings['sourceusername']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourceusername'] = ''
            f.write("  sourceusername=" + self.userSettings['sourceusername'] + "\n")

            # define sourcepassword
            if re.findall('^[<]|[>]$', self.userSettings['sourcepassword']) == ['<', '>']:
                self.userSettings['sourcepassword'] = ''
            f.write("  sourcepassword=" + self.userSettings['sourcepassword'] + "\n")

            # define sourcesystemdatabase
            if re.findall('^[<]|[>]$', self.userSettings['sourcesystemdatabase']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourcesystemdatabase'] = ''
            f.write("  sourcesystemdatabase=" + self.userSettings['sourcesystemdatabase'] + "\n")

            # define destinationmethod
            if DUMP is None:
                f.write("  destinationmethod=DIRECT\n")
            elif DUMP == 'y':
                f.write("  destinationmethod=DUMP\n")

            # define destinationserver
            if re.findall('^[<]|[>]$', self.userSettings['destinationserver']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationserver')
            f.write("  destinationserver=" + self.userSettings['destinationserver'] + "\n")

            # define destinationport
            f.write("  destinationport=" + str(self.userSettings['destinationport']) + "\n")

            # define destinationusername
            if re.findall('^[<]|[>]$', self.userSettings['destinationusername']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationusername')
            f.write("  destinationusername=" + self.userSettings['destinationusername'] + "\n")

            # define destinationpassword
            if re.findall('^[<]|[>]$', self.userSettings['destinationpassword']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationpassword')
            f.write("  destinationpassword=" + self.userSettings['destinationpassword'] + "\n")

            # define destinationdatabase
            if re.findall('^[<]|[>]$', self.userSettings['destinationdatabase']) + ['<', '>'] != ['<', '>']:
                f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            else:
                f.write("  destinationdatabase=" + self.userSettings['destinationdatabase'] + "\n")

            # define maintenancedb
            f.write("  maintenancedb=" + self.userSettings['maintenancedb'] + "\n")

            # define destinationdumpfilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['dumpfiledirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'dumpfiledirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['dumpfiledirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['dumpfiledirectory'] += '\\'
            f.write("  destinationdumpfilename=" + self.userSettings['dumpfiledirectory'] + self.mdbSchema + ".sql\n")

            # define sourcetables[]
            f.write("  sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')

            # define dropdatabase
            if self.userSettings['dropdatabase'] in [0, 1]:
                f.write("  dropdatabase=" + str(self.userSettings['dropdatabase']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'dropdatabase')

            # define createtables
            if self.userSettings['createtables'] in [0, 1]:
                f.write("  createtables=" + str(self.userSettings['createtables']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'createtables')

            # define unicode
            if self.userSettings['unicode'] in [0, 1]:
                f.write("  unicode=" + str(self.userSettings['unicode']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'unicode')

            # define autocommit
            if self.userSettings['autocommit'] in [0, 1]:
                f.write("  autocommit=" + str(self.userSettings['autocommit']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'autocommit')

            # define transferdefaultvalues
            if self.userSettings['transferdefaultvalues'] in [0, 1]:
                f.write("  transferdefaultvalues=" + str(self.userSettings['transferdefaultvalues']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferdefaultvalues')

            # define transferindexes
            if self.userSettings['transferindexes'] in [0, 1]:
                f.write("  transferindexes=" + str(self.userSettings['transferindexes']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferindexes')

            # define transferautonumbers
            if self.userSettings['transferautonumbers'] in [0, 1]:
                f.write("  transferautonumbers=" + str(self.userSettings['transferautonumbers']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferautonumbers')

            # define transferrecords
            if self.userSettings['transferrecords'] in [0, 1]:
                f.write("  transferrecords=" + str(self.userSettings['transferrecords']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferrecords')

            # define columnlist
            if self.userSettings['columnlist'] in [0, 1]:
                f.write("  columnlist=" + str(self.userSettings['columnlist']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'columnlist')

            # define tableprefix
            f.write("  tableprefix=" + str(self.userSettings['tableprefix']) + "\n")

            # define negativeboolean
            if self.userSettings['negativeboolean'] in [0, 1]:
                f.write("  negativeboolean=" + str(self.userSettings['negativeboolean']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'negativeboolean')

            # define ignorelargeblobs
            if self.userSettings['ignorelargeblobs'] in [0, 1]:
                f.write("  ignorelargeblobs=" + str(self.userSettings['ignorelargeblobs']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'ignorelargeblobs')

            # define memotype
            f.write("  memotype=TEXT\n")

            # define datetimetype
            f.write("  datetimetype=TIMESTAMP\n")

        self.outputLog("PostgreSQL")

    # Load the settings of exporting to MySQL.
    # If there is no settings file, create it.
    # If the settings file is all default, then use the default settings.
    def loadMariaDBSettings(self):
        os.chdir(self.programDir)
        
        mariadbDefaultSettings = {
        'ATTENTION':'PLEASE REMOVE < > IN THE FOLLOWING FIELDS.',
        'sourcedirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\mdb\\>',
        'dumpfiledirectory':'<Your mdb files directory, e.g, W:\\My Documents\\mdb_ini\\dumps\\>',
        'sourceusername':'<If no username, leave it as default>',
        'sourcepassword':'<If no password, leave it as default>',
        'sourcesystemdatabase':'<If no specified database, leave it as default>',
        'destinationmethod':"DIRECT",
        'destinationhost':'<Your DB Server Host>',
        'destinationport':3306,
        'destinationusername':'<Your DB Username>',
        'destinationpassword':'<Your DB Password>',
        'destinationdatabase':'<Your destination database. Leave it as default and the program will create a database with the same name as your mdb file.>',
        # 'storageengine':"<Select one of the following engine:'ARCHIVE', 'DBD', 'Brighthouse', 'CSV', 'Falcon', 'InnoDB', 'Maria', 'MyISAM'>",
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
        'ignorelargeblobs':0
        }

        if "mdb2mariadb.json" not in os.listdir():
            print("\nCreate default settings file named 'mdb2mariadb.json' for exporting mdb to MySQL successfully.")
            print("Please customize the settings in 'mdb2mariadb.json' as you need. Then run this program again.")
            with open("mdb2mariadb.json", "w") as f:
                json.dump(mariadbDefaultSettings, f, indent=4, sort_keys=False)
            sys.exit()  # exit the program after creating the default settings
        else:
            print("\nLoading 'mdb2mariadb.json' successfully!\nIf you want to use the default settings, delete 'mdb2mariadb.json', and restart this program.")

        with open("mdb2mariadb.json", "r") as f:
            self.userSettings = json.load(f)

    # generate .ini file for MySQL
    def iniMariaDB(self, DUMP=None):
        os.chdir(self.rootDir)

        if "mariadb_ini" not in os.listdir(self.rootDir):
            os.mkdir("mariadb_ini")

        mariadb_iniDir = self.rootDir + "/mariadb_ini/"
        os.chdir(mariadb_iniDir)

        self.mdbSchema = self.mdbSchema.replace(".txt", "")  # remove the .txt extension

        if DUMP is None:
            extension = "_mariadb.ini"
        elif DUMP == 'y':
            extension = '_dump_mariadb.ini'

        with open(self.mdbSchema + extension, "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to MySQL]\n")

            # define sourcefilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['sourcedirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'sourcedirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['sourcedirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['sourcedirectory'] += '\\'
            f.write("  sourcefilename=" + self.userSettings['sourcedirectory'] + self.mdbSchema + ".mdb\n")

            # define sourceusername
            if re.findall('^[<]|[>]$', self.userSettings['sourceusername']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourceusername'] = ''
            f.write("  sourceusername=" + self.userSettings['sourceusername'] + "\n")

            # define sourcepassword
            if re.findall('^[<]|[>]$', self.userSettings['sourcepassword']) == ['<', '>']:
                self.userSettings['sourcepassword'] = ''
            f.write("  sourcepassword=" + self.userSettings['sourcepassword'] + "\n")

            # define sourcesystemdatabase
            if re.findall('^[<]|[>]$', self.userSettings['sourcesystemdatabase']) + ['<', '>'] != ['<', '>']:
                self.userSettings['sourcesystemdatabase'] = ''
            f.write("  sourcesystemdatabase=" + self.userSettings['sourcesystemdatabase'] + "\n")

            # define destinationmethod
            if DUMP is None:
                f.write("  destinationmethod=DIRECT\n")
            elif DUMP == 'y':
                f.write("  destinationmethod=DUMP\n")

            # define destinationhost
            if re.findall('^[<]|[>]$', self.userSettings['destinationhost']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationhost')
            f.write("  destinationhost=" + self.userSettings['destinationhost'] + "\n")

            # define destinationport
            f.write("  destinationport=" + str(self.userSettings['destinationport']) + "\n")

            # define destinationusername
            if re.findall('^[<]|[>]$', self.userSettings['destinationusername']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationusername')
            f.write("  destinationusername=" + self.userSettings['destinationusername'] + "\n")

            # define destinationpassword
            if re.findall('^[<]|[>]$', self.userSettings['destinationpassword']) == ['<', '>']:
                self.outputErrors('invalidSetting', 'destinationpassword')
            f.write("  destinationpassword=" + self.userSettings['destinationpassword'] + "\n")

            # define destinationdatabase
            if re.findall('^[<]|[>]$', self.userSettings['destinationdatabase']) + ['<', '>'] != ['<', '>']:
                f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            else:
                f.write("  destinationdatabase=" + self.userSettings['destinationdatabase'] + "\n")

            # define destinationdumpfilename
            # validate value
            if re.findall('^[<]|[>]$', self.userSettings['dumpfiledirectory']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'dumpfiledirectory')
            # if no \ at the end of directory, the program will add a \
            if re.findall("[a-z]$", self.userSettings['dumpfiledirectory']) != []:  # make sure the windows Path is end with \
                self.userSettings['dumpfiledirectory'] += '\\'
            f.write("  destinationdumpfilename=" + self.userSettings['dumpfiledirectory'] + self.mdbSchema + ".sql\n")

            # define sourcetables[]
            f.write("  sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')


            # define storeageengine
            # define storageengine
            '''
            if re.findall('^[<]|[>]$', self.userSettings['storageengine']) + ['<', '>'] != ['<', '>']:
                self.outputErrors('invalidSetting', 'storageengine')

            if self.userSettings['storageengine'] in ['ARCHIVE', 'DBD', 'Brighthouse', 'CSV', 'Falcon', 'InnoDB', 'Maria', 'MyISAM']:
                f.write("  storageengine=" + self.userSettings['storageengine'] + "\n")
            else:
                self.outputErrors('invalidSetting', 'storageengine')
            '''
            f.write("  storageengine=" + "Maria\n")

            # define dropdatabase
            if self.userSettings['dropdatabase'] in [0, 1]:
                f.write("  dropdatabase=" + str(self.userSettings['dropdatabase']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'dropdatabase')

            # define createtables
            if self.userSettings['createtables'] in [0, 1]:
                f.write("  createtables=" + str(self.userSettings['createtables']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'createtables')

            # define unicode
            if self.userSettings['unicode'] in [0, 1]:
                f.write("  unicode=" + str(self.userSettings['unicode']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'unicode')

            # define autocommit
            if self.userSettings['autocommit'] in [0, 1]:
                f.write("  autocommit=" + str(self.userSettings['autocommit']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'autocommit')

            # define transferdefaultvalues
            if self.userSettings['transferdefaultvalues'] in [0, 1]:
                f.write("  transferdefaultvalues=" + str(self.userSettings['transferdefaultvalues']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferdefaultvalues')

            # define transferindexes
            if self.userSettings['transferindexes'] in [0, 1]:
                f.write("  transferindexes=" + str(self.userSettings['transferindexes']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferindexes')

            # define transferautonumbers
            if self.userSettings['transferautonumbers'] in [0, 1]:
                f.write("  transferautonumbers=" + str(self.userSettings['transferautonumbers']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferautonumbers')

            # define transferrecords
            if self.userSettings['transferrecords'] in [0, 1]:
                f.write("  transferrecords=" + str(self.userSettings['transferrecords']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'transferrecords')

            # define columnlist
            if self.userSettings['columnlist'] in [0, 1]:
                f.write("  columnlist=" + str(self.userSettings['columnlist']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'columnlist')

            # define tableprefix
            f.write("  tableprefix=" + str(self.userSettings['tableprefix']) + "\n")

            # define negativeboolean
            if self.userSettings['negativeboolean'] in [0, 1]:
                f.write("  negativeboolean=" + str(self.userSettings['negativeboolean']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'negativeboolean')

            # define ignorelargeblobs
            if self.userSettings['ignorelargeblobs'] in [0, 1]:
                f.write("  ignorelargeblobs=" + str(self.userSettings['ignorelargeblobs']) + "\n")
            else:
                self.outputErrors('invalidSetting', 'ignorelargeblobs')

            # define memotype
            f.write("  memotype=LONGTEXT\n")

            # define datetimetype
            f.write("  datetimetype=DATETIME\n")

        self.outputLog("MariaDB")

    # Define log function
    def outputLog(self, filetype):
        os.chdir(self.programDir)
        with open("mdbConfig.log", "a", newline="\n") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": Generating " + filetype + " " + self.mdbSchema + " ini file. Mission successful!\n")
        f.close()

    # Define errors reminder
    def outputErrors(self, errorType=None, errorLocation=None):
        if errorType == 'invalidInput':
            print("\nError!\nInput Invalid!\nProgram Exit!\n")
        elif errorType == 'invalidSetting':
            print("\nError!")
            print(errorLocation + " in .json file is invalid!\nProgram Exit!\n")

        sys.exit()


# execute the program
obj = mdbConfig()
obj.main()
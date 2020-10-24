#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: mdb_ini_Generator.py                                              #
# File Path: /mdb_ini_Generator.py                                             #
# Created Date: 2020-10-19                                                     #
# -----                                                                        #
# Company: Pluralpoint Group Inc.                                              #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-10-23 8:41:57 pm                                         #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Pluralpoint Group Inc.                                    #
################################################################################

"""
Description:
1. This program will generate .ini files
2. This program working in MacOS/Linux will grab all of the Access DB's tables in a specificed working directory, and export files with the same name as Access DB to the working directory.

OS: MacOS
Prerequisite:
- Homebrew:  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" 
- mdbtools: brew install mdbtools
"""

"""
Sample .ini files:
- MySQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mysql.ini
- MSSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mssql.ini
- PostgreSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2prgsql.ini
"""

# %reset -f

import os
import sys
import re
import numpy as np

class mdb_ini_Generator:
    def __init__(self):
        pass

    def getUserInput(self):
        '''
        sourcePath = input("Please input your .mdb files directory: ")
        windowsPath = input("Please input your Windows .mdb files directory: ")
        '''
        
        # define the python working directory
        self.sourcePath = os.getcwd()

        # Tim
        # define the the .mdb files' path in Windows
        #self.windowsPath = 'D:\xtrdb\multi-mdbs'
        self.windowsPath = input("Please input your Windows .mdb files directory: ")
        if re.findall("[a-z]$", self.windowsPath) != []: # make sure the windowsPath is end with \
            self.windowsPath += '\\'

        # get user target DB type
        self.DB = input("Which type of DB do you prefer to convert to:\n1. MySQL\n2. MSSQL\n3. PostGreSQL\nInput the number here: ")

        self.getMdbFiles()
        self.infoCheck()
    
    def getMdbFiles(self):
        # find all .mdb files, and store their name with .mdb in list self.mdbFiles
        self.mdbFiles = []
        for i in os.listdir(self.sourcePath):
            if re.findall("[.]mdb$", i) != []:
                self.mdbFiles.append(i)

        if self.mdbFiles == []:
            print("Please input correct .mdb files directory!")
            sys.exit()
        else:
            return(self.mdbFiles)

    def infoCheck(self):
        # run mdbtools for generating schemas, and give the schemas a extension with .txt
        self.mdbSchemas = []
        for self.mdbFile in self.mdbFiles:
            self.mdbTxt = re.split("[.]mdb", self.mdbFile) # split .mdb, return a list
            self.mdbTxt = self.mdbTxt[0] # get the first item, which is the mdb name
            self.mdbTxt += '.txt' # add the extension .txt to schema files
            self.mdbSchemas.append(self.mdbTxt)
            os.system("mdb-schema {0} > {1}".format(self.mdbFile, self.mdbTxt))

        for self.mdbSchema in self.mdbSchemas:
            self.readFile()
            self.getSchemaIndex()
            self.getTableStructure()
            if self.DB == '1':
                self.iniMySQL()
            elif self.DB == '2':
                self.iniMSSQL()
            elif self.DB == '3':
                self.iniPostgreSQL()
            else:
                print("Please input correct target DB ID!")
                sys.exit() 

    def readFile(self):
        # Read the schema file
        file = open(self.mdbSchema, "r")
        self.schema = file.read().splitlines()
        file.close()
        
        return self.schema

    # get the start index & end index of each table
    def getSchemaIndex(self):
        # Grab the index of "CRATE TABLE" statement
        startIndex = [] # startIndex: in schema, the items start with "CREAT" is a create table statement block
        for i in self.schema:
            if re.findall("^CREATE", i) != []:
                startIndex.append(self.schema.index(i))

        # define endIndex: start from the second item of startIndex, everyone-2 is the end_index
        endIndex = startIndex.copy()
        del endIndex[0] # so I delete the first item
        endIndex = np.array(endIndex)-2 # temporarily convert endIndex to array object, then -2
        endIndex = list(endIndex) # convert it back to list object
        endIndex.append(len(self.schema)-3) # add the last ");" index

        # define sqlTableIndex storing the startIndex & endIndex for each table
        self.sqlTableIndex = []
        for s, e in zip(startIndex, endIndex):
            self.sqlTableIndex.append([s, e])

        return self.sqlTableIndex

    # get the full indices from start index and end index, then get the table name and column name.
    def getTableStructure(self):
        # Grab each table with columns
        self.tableIndices = [] # define the whole table
        for tableIndex in self.sqlTableIndex:
            tableBlock = range(tableIndex[0], tableIndex[1])
            tableContent = []
            for i in tableBlock:
                try:
                    startItem = re.search('\[', self.schema[i]).start()
                except AttributeError:
                    pass
                else:
                    endItem = re.search('\]', self.schema[i]).end()
                    tableContent.append(self.schema[i][startItem+1:endItem-1])
            self.tableIndices.append(tableContent)
        
        # get table name and columns name
        self.sourcetables = []
        for eachTable in self.tableIndices:
            self.sourcetables.append(eachTable[0]) # add table name as the first item
            for i in eachTable[1:]:
                columnName = r'{0}\{1}'.format(eachTable[0], i)
                self.sourcetables.append(eachTable[0] + '\\' + i) # add columns name as the rest items
        
        return self.sourcetables

    # generate .ini file for MySQL
    def iniMySQL(self):
        self.mdbSchema = self.mdbSchema.replace(".txt", "") # remove the .txt extension
        with open(self.mdbSchema + "_mysql.ini", "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to MySQL]\n")
            f.write("  sourcefilename=" + self.windowsPath + self.mdbSchema + ".mdb\n")
            f.write("  sourceusername=\n")
            f.write("  sourcepassword=\n")
            f.write("  sourcesystemdatabase=\n")
            f.write("  destinationmethod=DIRECT\n")
            f.write("  destinationhost=mysql-xtr.c9d5goyg8g3a.us-east-1.rds.amazonaws.com\n")
            f.write("  destinationport=3306\n")
            f.write("  destinationusername=admin\n")
            f.write("  destinationpassword=myPassWord_123\n")
            f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            f.write("  storageengine=InnoDB\n")
            f.write("  destinationdumpfilename=\n")

            f.write("  self.sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')

            f.write("  dropdatabase=1\n")
            f.write("  createtables=1\n")
            f.write("  unicode=1\n")
            f.write("  autocommit=1\n")
            f.write("  transferdefaultvalues=1\n")
            f.write("  transferindexes=1\n")
            f.write("  transferautonumbers=1\n")
            f.write("  transferrecords=1\n")
            f.write("  columnlist=1\n")
            f.write("  tableprefix=\n")
            f.write("  negativeboolean=0\n")
            f.write("  ignorelargeblobs=0\n")
            f.write("  memotype=LONGTEXT\n")
            f.write("  datetimetype=DATETIME\n")
        
        f.close()

    # generate .ini file for MSSQL
    def iniMSSQL(self):
        self.mdbSchema = self.mdbSchema.replace(".txt", "") # remove the .txt extension
        with open(self.mdbSchema + "_mssql.ini", "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to MSSQL]\n")
            f.write("  sourcefilename=" + self.windowsPath + self.mdbSchema + ".mdb\n")
            f.write("  sourceusername=\n")
            f.write("  sourcepassword=\n")
            f.write("  sourcesystemdatabase=\n")
            f.write("  destinationmethod=DIRECT\n")
            f.write("  destinationserver=sql19.c9d5goyg8g3a.us-east-1.rds.amazonaws.com\n")
            f.write("  destinationauthentication=SQL\n")
            f.write("  destinationusername=admin\n")
            f.write("  destinationpassword=myPassWord_123\n")
            f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            f.write("  destinationdumpfilename=\n")

            f.write("  self.sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')

            f.write("  dropdatabase=1\n")
            f.write("  createtables=1\n")
            f.write("  unicode=1\n")
            f.write("  autocommit=1\n")
            f.write("  transferdefaultvalues=1\n")
            f.write("  transferindexes=1\n")
            f.write("  transferautonumbers=1\n")
            f.write("  transferrecords=1\n")
            f.write("  columnlist=1\n")
            f.write("  tableprefix=\n")
            f.write("  negativeboolean=0\n")
            f.write("  ignorelargeblobs=0\n")
            f.write("  memotype=VARCHAR(MAX)\n")
            f.write("  datetimetype=DATETIME2\n")
        
        f.close()

    # generate .ini file for PostgreSQL
    # connection string: Server=127.0.0.1;Port=5432;Database=myDataBase;User Id=myUsername;Password=myPassword;
    # select statement: SELECT * FROM "table_name";
    def iniPostgreSQL(self):
        self.mdbSchema = self.mdbSchema.replace(".txt", "") # remove the .txt extension
        with open(self.mdbSchema + "_postgresql.ini", "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to PostgreSQL]\n")
            f.write("  sourcefilename=" + self.windowsPath + self.mdbSchema + ".mdb\n")
            f.write("  sourceusername=\n")
            f.write("  sourcepassword=\n")
            f.write("  sourcesystemdatabase=\n")
            f.write("  destinationmethod=DIRECT\n")
            f.write("  destinationserver=postgresql.c9d5goyg8g3a.us-east-1.rds.amazonaws.com\n")
            f.write("  destinationport=5432\n")
            f.write("  destinationusername=postgre\n")
            f.write("  destinationpassword=myPassWord_123\n")
            f.write("  destinationdatabase=" + self.mdbSchema + "\n")
            f.write("  maintenancedb=postgres\n")
            f.write("  destinationdumpfilename=\n")

            f.write("  self.sourcetables[]=")
            for i in self.sourcetables[:-1]:
                f.write('"' + i + '"' + ',')
            f.write('"' + self.sourcetables[-1] + '"' + '\n')

            f.write("  dropdatabase=1\n")
            f.write("  createtables=1\n")
            f.write("  unicode=1\n")
            f.write("  autocommit=1\n")
            f.write("  transferdefaultvalues=1\n")
            f.write("  transferindexes=1\n")
            f.write("  transferautonumbers=1\n")
            f.write("  transferrecords=1\n")
            f.write("  columnlist=1\n")
            f.write("  tableprefix=\n")
            f.write("  negativeboolean=0\n")
            f.write("  ignorelargeblobs=0\n")
            f.write("  memotype=TEXT\n")
            f.write("  datetimetype=TIMESTAMP\n")
        
        f.close()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: msa2mys.py                                                        #
# File Path: /msa2mys.py                                                       #
# Created Date: 2020-10-19                                                     #
# -----                                                                        #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-10-19 3:28:02 pm                                         #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Zacks Shen                                                #
################################################################################

"""
Description: 
1. This program will replace .ini file

3. This program working in MacOS will grab all of the Access DB's tables in a specificed working directory, and export to the file with the same name as Access DB.

OS: MacOS
Prerequisite:
- Homebrew:  $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)" 
- mdbtools: brew install mdbtools
"""

"""
Sample .ini file:
- MySQL: https://raw.githubusercontent.com/ZacksAmber/Work/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini/msa2mysql.ini?token=AF3F6DHYHL4NB6TIOAY7THK7SDRRE
- MSSQL: https://raw.githubusercontent.com/ZacksAmber/Work/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini/msa2mssql.ini?token=AF3F6DE5DA63MVNLP52C37K7SDRLM
- PostgreSQL: https://raw.githubusercontent.com/ZacksAmber/Work/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini/msa2prgsql.ini?token=AF3F6DDMZLHNFDJW2DIICJS7SDRUA
"""

# %reset -f

import os
import sys
import re
import numpy as np

class msa2mys:
    def __init__(self, mdbSchema):
        self.mdbSchema = mdbSchema

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

    # generate .ini file
    def iniFile(self):
        with open(self.mdbSchema + ".ini", "w", newline="\r\n") as f:
            f.write("[MoveDB MSAccess to MySQL]\n")
            f.write("  sourcefilename=" + windowsPath + self.mdbSchema + ".mdb\n")
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
    
    # run all functions
    def iniGenerate(self):
        self.readFile()
        self.getSchemaIndex()
        self.getTableStructure()
        self.iniFile()


# Main Function
'''
sourcePath = input("Please input your .mdb files directory: ")
windowsPath = input("Please input your Windows .mdb files directory: ")
'''

sourcePath = os.getcwd()

# Tim
# windowsPath = D:\xtrdb\multi-mdbs
windowsPath = input("Please input your Windows .mdb files directory: ")

# find all .mdb files
files = os.listdir(sourcePath)

# find all .mdb files
mdbFiles = []
for i in files:
    if re.findall("[.]mdb$", i) != []:
        mdbFiles.append(i)

# run mdbtools for generating schemas
mdbSchemas = []
for mdbFile in mdbFiles:
    mdb = re.split("[.]mdb", mdbFile) # split .mdb, return a list
    mdb = mdb[0] # get the first item, which is the mdb name
    mdbSchemas.append(mdb)
    os.system("mdb-schema {0} > {1}".format(mdbFile, mdb))

if mdbSchemas == []:
    print("Please input correct .mdb files directory!")
    sys.exit()
else:
    for mdbSchema in mdbSchemas:
        obj = msa2mys(mdbSchema)            
        obj.iniGenerate()
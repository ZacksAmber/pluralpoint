#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: mdb_ini_Exporter.py                                               #
# File Path: /mdb_ini_Exporter.py                                              #
# Created Date: 2020-10-24                                                     #
# -----                                                                        #
# Company: Pluralpoint Group Inc.                                              #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-11-03 10:01:32 am                                        #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Pluralpoint Group Inc.                                    #
################################################################################

"""
This program is designed for passing parameters to the covertor then runing it.
"""

import os
import sys
import subprocess
import datetime
import re
import json
import mysql.connector

class mdb_ini_Exporter:
    def __init__(self):
        self.programDir = os.getcwd()
        os.chdir("..")
        self.rootDir = os.getcwd()

        # Create README.txt
        os.chdir(self.programDir)
        with open("README.txt", "w", newline="\r\n") as f:
            f.write("Prerequisite:\n")
            f.write("1. Please make a directory named 'programs' to store 'mdb_ini_Generator.py' and 'mdb_ini_Exporter.py'.\n")
            f.write("2. Please make a directory named 'mdb' to store mdb files.\n")
            f.write("3. Search 'mdbtools' online and install it.\n")
            f.write("4. Modules Required: mysql.connector\n")
            f.write("\n")
            f.write("Instruction:\n")
            f.write("1. Run 'mdb_ini_Generator.py' on your MacBook or Linux.\n")
            f.write("2. copy the following directories to your Windows: 'mdb', 'programs', *_ini\n")
            f.write("3. Run 'mdb_ini_Exporter.py' on your Windows.\n")
            f.write("P.S: A better solution is sharing a folder through Windows and MackBook/Linux. And let them sync the files and directories automatically.")
        
        os.chdir(self.rootDir)
        if "mdb" not in os.listdir(self.rootDir):
            print("Please make a directory with the name 'mdb' that in the partent directory of this program!")
            input("Press anything to exit")
            sys.exit()

    # main function
    def main(self):
        os.chdir(self.rootDir)
        
        # get user target DB type
        print("Which type of DB do you prefer to convert to:\n1. MySQL (for other engines such as MariaDB, input 1)\n2. MSSQL\n3. PostgreSQL")
        targetDB = input("Input the number here: ")
        print("")
        
        if targetDB not in ['1', '2', '3']:
            print("Please input an valid number!")
            input("Press any to exit!")
            sys.exit()
        else:
            print("")

        # get user preference for validation of DB migration
        print("Do you prefer to validate the records after DB migration: y or n")
        validateDB = input("Input the choice here: ")
        print('')

        if validateDB not in ['y', 'n']:
            print("Please input 'y' or 'n'!")
            input("Press any to exit!")
            sys.exit()
        else:
            print('')

        if targetDB == '1':
            if validateDB == 'y':
                self.getMySQL('y')
            else:
                self.getMySQL('n')
        elif targetDB == '2':
            if validateDB == 'y':
                self.getMSSQL('y')
            else:
                self.getMSSQL('n')
        elif targetDB == '3':
            if validateDB == 'y':
                self.PostgreSQL('y')
            else:
                self.PostgreSQL('n')

    def getMySQL(self, validateDB):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MySQL\\msa2mys.exe'
        self.iniDir = self.rootDir + "\\mysql_ini\\"

        os.chdir(self.rootDir)
        if "mysql_dump" not in os.listdir(self.rootDir):
            os.mkdir("mysql_dump")
        if validateDB == 'y':
            if 'mysql_records' not in os.listdir(self.rootDir):
                os.mkdir('mysql_records')
            self.mysql_recordsDir = self.rootDir + '\\mysql_records\\'
        
        self.exportDB(exePath, "MySQL", validateDB)

    def getMSSQL(self, validateDB):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MSSQL\\msa2sql.exe'
        self.iniDir = self.rootDir + "\\mssql_ini\\"

        os.chdir(self.rootDir)
        if "mssql_dump" not in os.listdir(self.rootDir):
            os.mkdir("mssql_dump")
        if validateDB == 'y':
            if 'mssql_records' not in os.listdir(self.rootDir):
                os.mkdir('mssql_records')
            self.mssql_recordsDir = self.rootDir + '\\mssql_records\\'
        
        self.exportDB(exePath, "MSSQL", validateDB)

    def getPostgreSQL(self, validateDB):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to PostgreSQL\\msa2pgs.exe'
        self.iniDir = self.rootDir + "\\postgresql_ini\\"

        os.chdir(self.rootDir)
        if "postgresql_dump" not in os.listdir(self.rootDir):
            os.mkdir("postgresql_dump")
        if validateDB == 'y':
            if "postgresql_records" not in os.listdir(self.rootDir):
                os.mkdir("postgresql_records")
            self.postgresql_recordsDir = self.rootDir + '\\postgresql_records\\'
                    
        self.exportDB(exePath, "PostgreSQL", validateDB)

    def exportDB(self, exePath, databaseType, validateDB):
        os.chdir(self.iniDir)
        iniFiles = os.listdir()

        for iniFile in iniFiles:
            os.chdir(self.iniDir) # after invoking outputLog, go back to the iniDir
            '''
            mdbName = iniFile # get the ini file name without extension and DB type
            mdbName = mdbName[::-1]
            mdbName = mdbName.split("_", 1)
            mdbName = mdbName[-1]
            mdbName = mdbName[::-1]
            '''
            if databaseType == 'MySQL':
                mdbName = iniFile.split('_mysql.ini')[0]
            elif databaseType == 'MSSSQL':
                mdbName = iniFile.split('_mssql.ini')[0]
            elif databaseType == 'PostgreSQL':
                mdbName = iniFile.split('_postgresql.ini')[0]
            SETTINGS = "SETTINGS=" + iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"]  # define the parameters for the .exe
            #proc = subprocess.Popen(args)
            proc = subprocess.run(args)
            try:
                print("Handling DB " + mdbName)
                startTime = datetime.datetime.now().time()
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful", startTime=startTime)
                #proc.wait()
                proc
                if re.findall("_dump$", mdbName) == []:
                    print("Export DB " + mdbName + ": Successful!")
                    endTime = datetime.datetime.now().time()
                    self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful",  startTime=startTime, endTime=endTime)
                    if validateDB == 'y':  # validate the DB records
                        self.validateDB(mdbName, databaseType)
                else:
                    print("Dump DB " + mdbName + ": Successful!")
                    endTime = datetime.datetime.now().time()
                    self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful",  startTime=startTime, endTime=endTime)
                print("")
            except:
                #proc.kill()
                startTime = datetime.datetime.now().time()
                print("Export DB " + mdbName + ": Failed!")
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="failed", startTime=startTime)
                sys.exit()
                
    def validateDB(self, mdbName, databaseType):
        if databaseType == 'MySQL':
            self.validateMySQL(mdbName)
        elif databaseType == 'MSSQL':
            self.validateMSSQL(mdbName)
        elif databaseType == 'PostgreSQL':
            self.validatePostgreSQL(mdbName)

    def validateMySQL(self, mdbName):
        os.chdir(self.programDir)

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

        dbCursor = dbConnection.cursor()
        dbCursor.execute('SHOW TABLES')
        dbTables = dbCursor.fetchall()
        
        # write log into mdb_ini_Exporter.log
        for dbTable in dbTables:
            dbTable = dbTable[0].decode()
            dbCursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
            dbRecords = dbCursor.fetchall()[0][0]
            with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                f.write('Table: ' + dbTable + '\n')
                f.write('Records: ' + str(dbRecords) + '\n')

        with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
            f.write('\n')

        print("Write records in log file successfully!")

        # write records from querying table for each mdb in JSON file
        os.chdir(self.mysql_recordsDir)
        
        recordsJsonFile = mdbName + '.json'
        dbJson = {}
        for dbTable in dbTables:
            dbTable = dbTable[0].decode()
            dbCursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
            dbRecords = dbCursor.fetchall()[0][0]
            dbJson[dbTable] = dbRecords

        with open(recordsJsonFile, "w", newline="\r\n") as f:
            json.dump(dbJson, f, indent=4, sort_keys=False)

        print("Write records in JSON file successfully!")

    def validateMSSQL(self, mdbName):
        os.chdir(self.programDir)
        with open('mdb2mssql.json') as f:
            userSettings = json.load(f)
            dbUsername = userSettings['destinationusername']
            dbPassword = userSettings['destinationpassword']
            dbServer = userSettings['destinationserver']

    def validatePostgreSQL(self, mdbName):
        os.chdir(self.programDir)
        with open('mdb2postgresql.json') as f:
            userSettings = json.load(f)
            dbUsername = userSettings['destinationusername']
            dbPassword = userSettings['destinationpassword']
            dbServer = userSettings['destinationserver']
            dbPort = int(userSettings['destinationport'])

    def outputLog(self, mdbName=None, databaseType=None, status=None, startTime=None, endTime=None):
        os.chdir(self.programDir)

        if status == "successful":
            if endTime == None:
                with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                    f.write("####################\n")
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission start!\n")               
            else:
                procTime = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute, seconds=endTime.second) - datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)
                with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                    f.write("Time consumed: " + str(procTime) + "\n")
                    f.write("\n")
        else:
            with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                f.write("####################\n")
                f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                f.write("\n")

# Execute the program
obj = mdb_ini_Exporter()
obj.main()
input("\nAll missions have been completed! Please check the log file.")

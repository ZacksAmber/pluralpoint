#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: mdbMigrator.py                                                    #
# File Path: /mdbMigrator.py                                                   #
# Created Date: 2020-11-02                                                     #
# -----                                                                        #
# Company: Pluralpoint Group Inc.                                              #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-11-05 3:50:14 pm                                         #
# Modified By: Zacks Shen <zacks.shen@pluralpoint.com>                         #
# -----                                                                        #
# Copyright (c) 2020 Pluralpoint Group Inc.                                    #
################################################################################

import os
import sys
import subprocess
import shutil  # module for moving file
import datetime
import re
import json
# for databases connection
import mysql.connector
import pymssql
import psycopg2


class mdbMigrator:
    def __init__(self):
        self.programDir = os.getcwd()
        os.chdir("..")
        self.rootDir = os.getcwd()

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
            f.write("4. Modules Required: `mysql.connector`, `psmssql`, `psycopg2`\n")
            f.write("- P.S: A better solution is sharing a folder through Windows and MackBook/Linux. And let them sync the files and directories automatically.\n")
            f.write("---\n")
            f.write("Sample .ini files:\n")
            f.write("- MySQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mysql.ini\n")
            f.write("- MSSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mssql.ini\n")
            f.write("- PostgreSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2prgsql.ini\n")
        
        os.chdir(self.rootDir)
        if "mdb" not in os.listdir(self.rootDir):
            print("Please make a directory with the name 'mdb' that in the partent directory of this program!")
            input("Press anything to exit")
            sys.exit()

    # main function
    def main(self):
        os.chdir(self.rootDir)
        
        # get user target DB type
        print("Which type of DB do you prefer to convert to:\n1. MySQL (for other engines such as MariaDB, input 1)\n2. MSSQL\n3. PostgreSQL\nq. q for Quit")

        while True:
            try:
                targetDB = input("Input the number here: ")
                if targetDB in ['1', '2', '3']:
                    break
                elif targetDB == 'q':
                    sys.exit()
                else:
                    print("Please input an valid number!\n")
            except ValueError:
                print("Please input an number!\n")
        
        # create dumps directory
        if targetDB == '1':
            jsonFile = 'mdb2mysql.json'
        elif targetDB == '2':
            jsonFile = 'mdb2mssql.json'
        elif targetDB == '3':
            jsonFile = 'mdb2postgresql.json'

        os.chdir(self.programDir)
        with open(jsonFile) as f:
            userSettings = json.load(f)
            dumpsDir = userSettings['dumpfiledirectory']

        if re.findall("[a-z]$", dumpsDir) != []:  # make sure the windows Path is end with \
            dumpsDir += '\\'

        os.chdir(self.rootDir)
        dumpsDir = dumpsDir.split('\\')[-2]
        if dumpsDir not in os.listdir(self.rootDir):
            os.mkdir(dumpsDir)

        os.chdir(dumpsDir)
        self.dumpsDir = os.getcwd()

        # get user preference for validation of DB migration
        # get user target DB type
        print("\nDo you prefer to validate the records after DB migration: y or n, q for Quit")

        while True:
            try:
                validateDB = input("Input the choice here: ")
                if validateDB == 'y':
                    os.chdir(self.rootDir)
                    if 'records' not in os.listdir(self.rootDir):
                        os.mkdir('records')
                    os.chdir('records')
                    self.recordsDir = os.getcwd()
                    break
                elif validateDB == 'n':
                    break
                elif validateDB == 'q':
                    sys.exit()
                else:
                    print("Please input an valid letter!\n")
            except ValueError:
                print("Please input an letter!\n")
        print('')

        if targetDB == '1':
            if validateDB == 'y':
                self.setMySQL('y')
            else:
                self.setMySQL('n')
        elif targetDB == '2':
            if validateDB == 'y':
                self.setMSSQL('y')
            else:
                self.setMSSQL('n')
        elif targetDB == '3':
            if validateDB == 'y':
                self.setPostgreSQL('y')
            else:
                self.setPostgreSQL('n')

    # Set MySQL
    def setMySQL(self, validateDB):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MySQL\\msa2mys.exe'
        self.iniDir = self.rootDir + "\\mysql_ini\\"

        os.chdir(self.dumpsDir)
        if "mysql_dumps" not in os.listdir(self.dumpsDir):
            os.mkdir("mysql_dumps")

        if validateDB == 'y':
            os.chdir(self.recordsDir)
            if validateDB == 'y':
                if 'mysql_records' not in os.listdir(self.recordsDir):
                    os.mkdir('mysql_records')
                self.mysql_recordsDir = self.rootDir + '\\records\\mysql_records\\'
        
        self.migrateDB(exePath, "MySQL", validateDB)

    # Set MSSQL
    def setMSSQL(self, validateDB):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MSSQL\\msa2sql.exe'
        self.iniDir = self.rootDir + "\\mssql_ini\\"

        os.chdir(self.dumpsDir)
        if "mssql_dumps" not in os.listdir(self.dumpsDir):
            os.mkdir("mssql_dumps")

        if validateDB == 'y':
            os.chdir(self.recordsDir)
            if validateDB == 'y':
                if 'mssql_records' not in os.listdir(self.recordsDir):
                    os.mkdir('mssql_records')
                self.mssql_recordsDir = self.rootDir + '\\records\\mssql_records\\'
        
        self.migrateDB(exePath, "MSSQL", validateDB)

    # Set PostgreSQL
    def setPostgreSQL(self, validateDB):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to PostgreSQL\\msa2pgs.exe'
        self.iniDir = self.rootDir + "\\postgresql_ini\\"

        os.chdir(self.dumpsDir)
        if "postgresql_dumps" not in os.listdir(self.dumpsDir):
            os.mkdir("postgresql_dumps")

        if validateDB == 'y':
            os.chdir(self.recordsDir)
            if validateDB == 'y':
                if "postgresql_records" not in os.listdir(self.recordsDir):
                    os.mkdir("postgresql_records")
                self.postgresql_recordsDir = self.rootDir + '\\records\\postgresql_records\\'
                    
        self.migrateDB(exePath, "PostgreSQL", validateDB)

    def migrateDB(self, exePath, databaseType, validateDB):
        os.chdir(self.iniDir)
        iniFiles = os.listdir()

        for iniFile in iniFiles:
            os.chdir(self.iniDir)  # after invoking outputLog, go back to the iniDir

            if databaseType == 'MySQL':
                mdbName = iniFile.split('_mysql.ini')[0]
            elif databaseType == 'MSSQL':
                mdbName = iniFile.split('_mssql.ini')[0]
            elif databaseType == 'PostgreSQL':
                mdbName = iniFile.split('_postgresql.ini')[0]
            SETTINGS = "SETTINGS=" + iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"]  # define the parameters for the .exe
            proc = subprocess.Popen(args)
            print("Handling DB " + mdbName)
            # proc = subprocess.run(args)
            try:
                startTime = datetime.datetime.now()
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful", startTime=startTime, endTime=None)
                proc.wait() # start migration
                # proc
                if re.findall("_dump$", mdbName) == []:
                    print("Migrate DB " + mdbName + ": Successful!")
                    endTime = datetime.datetime.now()
                    self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful",  startTime=startTime, endTime=endTime)
                    if validateDB == 'y':  # validate the DB records
                        self.validateDB(mdbName, databaseType)
                else:
                    print("Dump DB " + mdbName + ": Successful!")
                    endTime = datetime.datetime.now()
                    self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful",  startTime=startTime, endTime=endTime)
                    sqlFile = mdbName.split('_dump')[0]
                    if databaseType == "MySQL":
                        shutil.move(os.path.join(self.dumpsDir, sqlFile+".sql"), os.path.join(self.dumpsDir+"\\mysql_dumps", sqlFile+".sql"))
                    elif databaseType == "MSSQL":
                        shutil.move(os.path.join(self.dumpsDir, sqlFile+".sql"), os.path.join(self.dumpsDir+"\\mssql_dumps", sqlFile+".sql"))
                    elif databaseType == "PostgreSQL":
                        shutil.move(os.path.join(self.dumpsDir, sqlFile+".sql"), os.path.join(self.dumpsDir+"\\postgresql_dumps", sqlFile+".sql"))
                print("")
            except:
                # proc.kill()
                startTime = datetime.datetime.now()
                print("Migrate DB " + mdbName + ": Failed!")
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="failed", startTime=startTime)
                input("Please review log file! Press enter to exit!\n")
                sys.exit()

    # Define function for connecting to different DB
    def validateDB(self, mdbName, databaseType):
        if databaseType == 'MySQL':
            self.validateMySQL(mdbName)
        elif databaseType == 'MSSQL':
            self.validateMSSQL(mdbName)
        elif databaseType == 'PostgreSQL':
            self.validatePostgreSQL(mdbName)

    # Define MySQL connection
    def validateMySQL(self, mdbName):
        os.chdir(self.programDir)

        # read DB settings from .json file
        with open('mdb2mysql.json') as f:
            userSettings = json.load(f)
            dbUsername = userSettings['destinationusername']
            dbPassword = userSettings['destinationpassword']
            dbHost = userSettings['destinationhost']
            dbPort = int(userSettings['destinationport'])

        # create connection
        try:
            cnx = mysql.connector.connect(
                host=dbHost,
                user=dbUsername,
                password=dbPassword,
                port=dbPort,
                database=mdbName,
                )
        except mysql.connector.Error:
            print("Connection Error")

        # define cursor
        cursor = cnx.cursor()

        # get all tables name of current database
        cursor.execute('SHOW TABLES')
        dbTables = cursor.fetchall()
        
        # write log into mdbMigrator.log
        for dbTable in dbTables:
            dbTable = dbTable[0].decode()
            cursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
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
            dbTable = dbTable[0].decode()
            cursor.execute('SELECT COUNT(*) FROM `{0}`'.format(dbTable))
            dbRecords = cursor.fetchall()[0][0]
            dbJson[dbTable] = dbRecords

        with open(recordsJsonFile, "w", newline="\r\n") as f:
            json.dump(dbJson, f, indent=4, sort_keys=False)

        print("Write records in JSON file successfully!")

        # Close the connection
        cnx.close()

    # Define MSSQL connection
    def validateMSSQL(self, mdbName):
        os.chdir(self.programDir)

        # read DB settings from .json file
        with open('mdb2mssql.json') as f:
            userSettings = json.load(f)
            dbUsername = userSettings['destinationusername']
            dbPassword = userSettings['destinationpassword']
            dbServer = userSettings['destinationserver']
            dbAuth = userSettings['destinationauthentication']

        # create connection
        try:
            cnx = pymssql.connect(
                server=dbServer,
                user=dbUsername,
                password=dbPassword,
                database=mdbName
                )
        except pymssql.OperationalError:
            self.outputErrors(errorType='DBConnection', databaseType=databaseType)
        
        # define cursor
        cursor = cnx.cursor()

        # get all tables name of current database
        cursor.execute("SELECT TABLE_NAME from INFORMATION_SCHEMA.TABLES")
        dbTables = cursor.fetchall()

        # write log into mdbMigrator.log
        for dbTable in dbTables:
            dbTable = dbTable[0]
            cursor.execute('SELECT COUNT(*) FROM "{0}";'.format(dbTable))
            dbRecords = cursor.fetchall()[0][0]
            with open("mdbMigrator.log", "a", newline="\r\n") as f:
                f.write('Table: ' + dbTable + '\n')
                f.write('Records: ' + str(dbRecords) + '\n')

        with open("mdbMigrator.log", "a", newline="\r\n") as f:
            f.write('\n')

        print("Write records in log file successfully!")

        # write records from querying table for each mdb in JSON file
        os.chdir(self.mssql_recordsDir)
        
        recordsJsonFile = mdbName + '.json'
        dbJson = {}
        for dbTable in dbTables:
            dbTable = dbTable[0]
            cursor.execute('SELECT COUNT(*) FROM "{0}";'.format(dbTable))
            dbRecords = cursor.fetchall()[0][0]
            dbJson[dbTable] = dbRecords

        with open(recordsJsonFile, "w", newline="\r\n") as f:
            json.dump(dbJson, f, indent=4, sort_keys=False)

        print("Write records in JSON file successfully!")

        # Close the connection
        cnx.close()

    # Define PostgreSQL connection
    def validatePostgreSQL(self, mdbName):
        os.chdir(self.programDir)

        # read DB settings from .json file
        with open('mdb2postgresql.json') as f:
            userSettings = json.load(f)
            dbUsername = userSettings['destinationusername']
            dbPassword = userSettings['destinationpassword']
            dbServer = userSettings['destinationserver']
            dbPort = userSettings['destinationport']

        # create connection
        try:
            cnx = psycopg2.connect(
                database=mdbName,
                user=dbUsername,
                password=dbPassword,
                host=dbServer,
                port=str(dbPort)
                )
        except psycopg2.OperationalError:
            self.outputErrors(errorType='DBConnection', databaseType=databaseType)

        # define cursor
        cursor = cnx.cursor()

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
        os.chdir(self.postgresql_recordsDir)

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

    # Define log function
    def outputLog(self, mdbName=None, databaseType=None, status=None, startTime=None, endTime=None):
        os.chdir(self.programDir)

        if status == "successful":
            if endTime is None:
                with open("mdbMigrator.log", "a", newline="\r\n") as f:
                    f.write("####################\n")
                    f.write(startTime.strftime("%Y-%m-%d %H:%M:%S") + " -- Migrate DB " + mdbName + " to RDS " + databaseType + ". Mission start!\n")               
            else:
                procTime = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute, seconds=endTime.second) - datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)
                with open("mdbMigrator.log", "a", newline="\r\n") as f:
                    f.write(endTime.strftime("%Y-%m-%d %H:%M:%S") + " -- Migrate DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                    f.write("Time consumed: " + str(procTime) + "\n")
                    f.write("\n")
        else:
            with open("mdbMigrator.log", "a", newline="\r\n") as f:
                f.write("####################\n")
                f.write(endTime.strftime("%Y-%m-%d %H:%M:%S") + " -- Migrate DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                f.write("\n")

    # Define errors reminder
    def outputErrors(self, errorType=None, errorDB=None):
        if errorType == 'invalidInput':
            print("\nError!\nInput Invalid!\nProgram Exit!\n")
        elif errorType == 'DBConnection':
            print("\nError!")
            print('Connect to ' + errorDB + ' failed!\n')
            print('Please check your DB settings in *.json file under "programs" directory!\n')
            print('Please check your DB running status!\n')

        sys.exit()

# Execute the program
obj = mdbMigrator()
obj.main()
input("\nAll missions have been completed! Please check the log file.")

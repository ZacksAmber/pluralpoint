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
# Last Modified: 2020-11-01 10:04:23 pm                                        #
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

class mdb_ini_Exporter:
    def __init__(self):
        self.programDir = os.getcwd()
        os.chdir("..")
        self.rootDir = os.getcwd()
        '''
        wdCheck = input("Please make a directory to store the programs, and make another directory with the name 'mdb' to store the mdb files.\n1. Input 'y' to start.\n2. Input anything to quit.\nYour input: ")
        
        if wdCheck not in ["y", "Y"]:
            sys.exit()
        '''
        # Create README.txt
        os.chdir(self.programDir)
        with open("README.txt", "w", newline="\r\n") as f:
            f.write("Prerequisite:\n")
            f.write("1. Please make a directory named 'programs' to store 'mdb_ini_Generator.py' and 'mdb_ini_Exporter.py'.\n")
            f.write("2. Please make a directory named 'mdb' to store mdb files.\n")
            f.write("3. Search 'mdbtools' online and install it.\n")
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

    def main(self):
        # get user target DB type
        self.DB = input("Which type of DB do you prefer to convert to:\n1. MySQL (for other engines such as MariaDB, input 1)\n2. MSSQL\n3. PostgreSQL\nInput the number here: ")
        print("")
        
        if self.DB == '1':
            self.getMySQL()
        elif self.DB == '2':
            self.getMSSQL()
        elif self.DB == '3':
            self.getPostgreSQL()
        else:
            print("Please input an valid number!")
            sys.exit() 

    def getMySQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MySQL\\msa2mys.exe'
        iniDir = self.rootDir + "\\mysql_ini\\"

        self.exportDB(exePath, iniDir, "MySQL")

        if "mysql_dump" not in os.listdir(self.rootDir):
            os.mkdir("mysql_dump")
        #self.exportDB(exePath, iniDir, "MySQL", DUMP='Y')

    def getMSSQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MSSQL\\msa2sql.exe'
        mssql_iniDir = self.rootDir + "\\mssql_ini\\"

        self.exportDB(exePath, iniDir, "MSSQL")

        if "mssql_dump" not in os.listdir(self.rootDir):
            os.mkdir("mssql_dump")
        #self.exportDB(exePath, iniDir, "MSSQL", DUMP='Y')

    def getPostgreSQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to PostgreSQL\\msa2pgs.exe'
        postgresql_iniDir = self.rootDir + "\\postgresql_ini\\"

        self.exportDB(exePath, iniDir, "PostgreSQL")

        if "postgresql_dump" not in os.listdir(self.rootDir):
            os.mkdir("postgresql_dump")
        #self.exportDB(exePath, iniDir, "PostgreSQL", DUMP='Y')

    def exportDB(self, exePath, iniDir, databaseType, DUMP=None):
        os.chdir(iniDir)
        iniFiles = os.listdir()

        for iniFile in iniFiles:
            os.chdir(iniDir) # after invoking outputLog, go back to the iniDir
            mdbName = iniFile # get the ini file name without extension and DB type
            mdbName = mdbName[::-1]
            mdbName = mdbName.split("_", 1)
            mdbName = mdbName[-1]
            mdbName = mdbName[::-1]
            SETTINGS = "SETTINGS=" + iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"] # define the parameters for the .exe
            proc = subprocess.Popen(args)
            try:
                print("Exporting DB " + mdbName)
                startTime = datetime.datetime.now().time()
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful", startTime=startTime)
                proc.wait()
                print("Export DB " + mdbName + ": Successful!")
                print("")
                endTime = datetime.datetime.now().time()
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="successful",  startTime=startTime, endTime=endTime)
            except:
                proc.kill()
                startTime = datetime.datetime.now().time()
                print("Export DB " + mdbName + ": Failed!")
                self.outputLog(mdbName=mdbName, databaseType=databaseType, status="failed", startTime=startTime)

    def outputLog(self, mdbName=None, databaseType=None, status=None, startTime=None, endTime=None):
        os.chdir(self.programDir)

        if status == "successful":
            if endTime == None:
                with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission start!\n")               
            else:
                procTime = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute, seconds=endTime.second) - datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)
                with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                    f.write("Time consumed: " + str(procTime) + "\n")
                    f.write("\n")
        else:
            with open("mdb_ini_Exporter.log", "a", newline="\r\n") as f:
                f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                f.write("")
        
        f.close()
            
# Execute the program
obj = mdb_ini_Exporter()
obj.main()
input("All missions have been completed! Please check the log file.")
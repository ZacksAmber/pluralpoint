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
# Last Modified: 2020-10-25 7:43:15 pm                                         #
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

        wdCheck = input("Please make a directory to store the programs, and make another directory with the name 'mdb' to store the mdb files.\n1. Input 'y' to start.\n2. Input anything to quit.\nYour input: ")
        
        if wdCheck not in ["y", "Y"]:
            sys.exit()
        
        if "mdb" not in os.listdir(self.rootDir):
            print("Please make a directory with the name 'mdb' that in the partent directory of this program!")
            sys.exit()

    def main(self):
        # get user target DB type
        self.DB = input("Which type of DB do you prefer to convert to:\n1. MySQL\n2. MSSQL\n3. PostgreSQL\nInput the number here: ")
        
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

    def getMSSQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MSSQL\\msa2sql.exe'
        mssql_iniDir = self.rootDir + "\\mssql_ini\\"

        self.exportDB(exePath, iniDir, "MSSSQL")

    def getPostgreSQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to PostgreSQL\\msa2pgs.exe'
        postgresql_iniDir = self.rootDir + "\\postgresql_ini\\"

        self.exportDB(exePath, iniDir, "PostgreSQL")

    def exportDB(self, exePath, iniDir, databaseType):
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
                with open("mdb_ini_Exporter_log.txt", "a", newline="\r\n") as f:
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission start!\n")               
            else:
                procTime = datetime.timedelta(hours=endTime.hour, minutes=endTime.minute, seconds=endTime.second) - datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)
                with open("mdb_ini_Exporter_log.txt", "a", newline="\r\n") as f:
                    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                    f.write("Time consumed: " + str(procTime) + "\n")
                    f.write("\n")
        else:
            with open("mdb_ini_Exporter_log.txt", "a", newline="\r\n") as f:
                f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " -- Exporting DB " + mdbName + " to RDS " + databaseType + ". Mission " + status + "!\n")
                f.write("")
        
        f.close()
            
# Execute the program
obj = mdb_ini_Exporter()
obj.main()
input("All mission complete! Please check the log file.")
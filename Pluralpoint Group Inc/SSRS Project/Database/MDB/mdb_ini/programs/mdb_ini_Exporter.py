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
# Last Modified: 2020-10-24 8:26:08 pm                                         #
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

class mdb_ini_Exporter:
    def __init__(self):
        os.chdir("..")
        self.rootDir = os.getcwd()

        wdCheck = input("Please make a directory to store the programs, and make another directory with the name 'mdb' to store the mdb files.\n1. Input 'y' to start.\n2 .Input anything to quit.\nYour input: ")
        
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
        self.exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MySQL\\msa2mys.exe'
        self.mysql_iniDir = self.rootDir + "\\mysql_ini\\"
        os.chdir(self.mysql_iniDir)

        self.exportDB("MySQL")


    def getMSSQL(self):
        self.exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MSSQL\\msa2sql.exe'
        self.mssql_iniDir = self.rootDir + "\\mssql_ini\\"
        os.chdir(self.mssql_iniDir)

        self.exportDB("MSSSQL")

    def getPostgreSQL(self):
        self.exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to PostgreSQL\\msa2pgs.exe'
        self.postgresql_iniDir = self.rootDir + "\\postgresql_ini\\"
        os.chdir(self.postgresql_iniDir)

        self.exportDB("PostgreSQL")

    def exportDB(self, databaseType):
        os.
        iniFiles = os.listdir()
        for iniFile in iniFiles:
            mdbName = iniFile # get the ini file name without extension and DB type
            mdbName = mdbName[::-1]
            mdbName = mdbName.split("_", 1)
            mdbName = mdbName[-1]
            mdbName = mdbName[::-1]
            SETTINGS = "SETTINGS=" + self.iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"] # define the parameters for the .exe
            proc = subprocess.Popen(args)
            try:
                proc.wait() # wait until the current process finished
                print("Process Running Succeed: " + iniFile)
                outputLog(mdbName, "succeed!")
            except:
                proc.kill()
                print("Process Running Failed: " + iniFile)
                outputLog(mdbName, "failed!")

    def outputLog(self, mdbName, databaseType, status):
        os.chdir(self.programDir)
        with open("mdb_ini_Exporter_log.txt", "a", newline="\r\n") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": Export DB " + mdbName + " to RDS " + databaseType + " " + status + "\n")

# Execute the program
obj = mdb_ini_Exporter()
obj.main()
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
################################################################################
# File Name: mdb_ini_exe.py                                                    #
# File Path: /mdb_ini_exe.py                                                   #
# Created Date: 2020-10-23                                                     #
# -----                                                                        #
# Company: Pluralpoint Group Inc.                                              #
# Author: Zacks Shen                                                           #
# Blog: https://zacks.one                                                      #
# Email: <zacks.shen@pluralpoint.com>                                          #
# Github: https://github.com/ZacksAmber                                        #
# -----                                                                        #
# Last Modified: 2020-10-23 10:14:29 pm                                        #
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

class mdb_ini_exe:
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
        self.DB = input("Which type of DB do you prefer to convert to:\n1. MySQL\n2. MSSQL\n3. PostGreSQL\nInput the number here: ")
        
        if self.DB == '1':
            self.exportMySQL()
        elif self.DB == '2':
            self.exportMSSQL()
        elif self.DB == '3':
            self.exportPostgreSQL()
        else:
            print("Please input an valid number!")
            sys.exit() 

    def exportMySQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MySQL\\msa2mys.exe'
        
        mysql_iniDir = self.rootDir + "\\mysql_ini\\"
        os.chdir(mysql_iniDir)

        iniFiles = os.listdir()
        for iniFile in iniFiles:
            SETTINGS = "SETTINGS=" + iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"]
            proc = subprocess.Popen(args)
            try:
                proc.wait()
                #outs, errs = proc.communicate(timeout=15)
                print("Process Running Succeed: " + iniFile)
            except:
            #except TimeoutExpired:
                proc.kill()
                #outs, errs = proc.communicate()
                print("Process Running Failed: " + iniFile)  

    def exportMSSQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MSSQL\\msa2sql.exe'

        mssql_iniDir = self.rootDir + "\\mssql_ini\\"
        os.chdir(mssql_iniDir)

        iniFiles = os.listdir()
        for iniFile in iniFiles:
            SETTINGS = "SETTINGS=" + iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"]
            proc = subprocess.Popen(args)
            try:
                proc.wait()
                #outs, errs = proc.communicate(timeout=15)
                print("Process Running Succeed: " + iniFile)
            except:
            #except TimeoutExpired:
                proc.kill()
                #outs, errs = proc.communicate()
                print("Process Running Failed: " + iniFile)

    def exportPostgreSQL(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to PostgreSQL\\msa2pgs.exe'

        postgresql_iniDir = self.rootDir + "\\postgresql_ini\\"
        os.chdir(postgresql_iniDir)

        iniFiles = os.listdir()
        for iniFile in iniFiles:
            SETTINGS = "SETTINGS=" + iniFile
            args = [exePath, SETTINGS, ",AUTORUN", ",HIDE"]
            proc = subprocess.Popen(args)
            try:
                proc.wait()
                #outs, errs = proc.communicate(timeout=15)
                print("Process Running Succeed: " + iniFile)
            except:
            #except TimeoutExpired:
                proc.kill()
                #outs, errs = proc.communicate()
                print("Process Running Failed: " + iniFile)

# Execute the program
obj = mdb_ini_exe()
obj.main()
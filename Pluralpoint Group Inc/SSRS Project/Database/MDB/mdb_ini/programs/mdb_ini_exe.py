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

class mdb_ini_Generator:
    def __init__(self):
        os.chdir("..")
        self.rootDir = os.getcwd()

        wdCheck = input("Please make a directory to store the programs, and make another directory with the name 'mdb' to store the mdb files.\n1. Input 'y' to start.\n2 .Input anything to quit.\nYour input: ")
        
        if wdCheck in ["y", "Y"] == False:
            sys.exit()
        
        if "mdb" in os.listdir(self.rootDir) is False:
            print("Please make a directory with the name 'mdb' that in the partent directory of this program!")
            sys.exit()

    def main(self):
        pass

    def mysql(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\\MS Access to MySQL\\msa2mys.exe'
        mdbPath = 'W:\\My Documents\\mdb_ini\\mdb\\'
        iniPath = 'W:\My Documents\mdb_ini\mysql_ini\\'

        args = ['SETTINGS=', 'AUTORUN,',]
        subprocess.Popen()
        pass

    def mssql(self):
        exePath = 'C:\\Program Files (x86)\Bullzip\\MS Access to MSSQL\\msa2sql.exe'
        pass

    def postgresql(self):
        exePath = 'C:\\Program Files (x86)\\Bullzip\MS Access to PostgreSQL\\msa2pgs.exe'
        pass


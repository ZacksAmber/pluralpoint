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

[MoveDB MSAccess to MySQL]
  sourcefilename=D:\Users\zacks\Desktop\xtreme.mdb
  sourceusername=
  sourcepassword=
  sourcesystemdatabase=
  destinationmethod=DIRECT
  destinationhost=mysql-xtr.c9d5goyg8g3a.us-east-1.rds.amazonaws.com
  destinationport=3306
  destinationusername=admin
  destinationpassword=myPassWord_123
  destinationdatabase=testdb2
  storageengine=InnoDB
  destinationdumpfilename=
  sourcetables[]="Credit","Credit\Credit Authorization Number","Credit\Customer Credit ID","Credit\Amount","Customer","Customer\Customer ID","Customer\Customer Credit ID","Customer\Customer Name","Customer\Contact First Name","Customer\Contact Last Name","Customer\Contact Title","Customer\Contact Position","Customer\Last Year Sales","Customer\Address1","Customer\Address2","Customer\City","Customer\negion","Customer\Country","Customer\Postal Code","Customer\Email","Customer\Web Site","Customer\Phone","Customer\Fax","Employee","Employee\Employee ID","Employee\Supervisor ID","Employee\Last Name","Employee\First Name","Employee\Position","Employee\Birth Date","Employee\Hire Date","Employee\Home Phone","Employee\Extension","Employee\Photo","Employee\notes","Employee\neports To","Employee\Salary","Employee\SSN","Employee\Emergency Contact First Name","Employee\Emergency Contact Last Name","Employee\Emergency Contact Relationship","Employee\Emergency Contact Phone","Employee Addresses","Employee Addresses\Employee ID","Employee Addresses\Address1","Employee Addresses\Address2","Employee Addresses\City","Employee Addresses\negion","Employee Addresses\Country","Employee Addresses\Postal Code","Employee Addresses\Emergency Contact Address1","Employee Addresses\Emergency Contact Address2","Employee Addresses\Emergency Contact City","Employee Addresses\Emergency Contact Region","Employee Addresses\Emergency Contact Country","Employee Addresses\Emergency Contact Postal Code","Financials","Financials\Company ID","Financials\Statement Date","Financials\Cash","Financials\Account Receivable","Financials\Inventories","Financials\Other Current Assets","Financials\Land","Financials\Buildings","Financials\Machinery etc","Financials\Accumulated Depreciation","Financials\Other Assets","Financials\Accounts Payable","Financials\Accrued Liabilities","Financials\Accrued Income Taxes","Financials\notes Payable","Financials\Deferred Income Taxes","Financials\Preferred Stock","Financials\Common Stock","Financials\netained Earnings","Financials\net Sales","Financials\COGS","Financials\General Expenses","Financials\Depreciation","Financials\Interest Expenses","Financials\Other Income Expenses","Financials\Taxes","Orders","Orders\Order ID","Orders\Order Amount","Orders\Customer ID","Orders\Employee ID","Orders\Order Date","Orders\nequired Date","Orders\Ship Date","Orders\Courier Website","Orders\Ship Via","Orders\Shipped","Orders\PO","Orders\Payment Received","Orders Detail","Orders Detail\Order ID","Orders Detail\Product ID","Orders Detail\Unit Price","Orders Detail\Quantity","Product","Product\Product ID","Product\Product Name","Product\Color","Product\Size","Product\MF","Product\Price","Product\Product Type ID","Product\Product Class","Product\Supplier ID","Product Type","Product Type\Product Type ID","Product Type\Product Type Name","Product Type\Description","Product Type\Picture","Purchases","Purchases\Product ID","Purchases\neorder Level","Purchases\Units in Stock","Purchases\Units on Order","Purchases\PO","Purchases\Order Date","Purchases\Expected Receiving Date","Purchases\neceived","Purchases\Paid","Supplier","Supplier\Supplier ID","Supplier\Supplier Name","Supplier\Address1","Supplier\Address2","Supplier\City","Supplier\negion","Supplier\Country","Supplier\Postal Code","Supplier\Phone","Xtreme Info","Xtreme Info\Xtreme Name","Xtreme Info\Address","Xtreme Info\City","Xtreme Info\Province","Xtreme Info\Country","Xtreme Info\Postal Code","Xtreme Info\Phone","Xtreme Info\Fax","Xtreme Info\Logo B&W","Xtreme Info\Logo Color"
  dropdatabase=1
  createtables=1
  unicode=1
  autocommit=1
  transferdefaultvalues=1
  transferindexes=1
  transferautonumbers=1
  transferrecords=1
  columnlist=1
  tableprefix=
  negativeboolean=0
  ignorelargeblobs=0
  memotype=LONGTEXT
  datetimetype=DATETIME
  """
'''
# Modules
import os
import sys
import re
import numpy as np



file = open(sourcePath, "r")
'''

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

# Time
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
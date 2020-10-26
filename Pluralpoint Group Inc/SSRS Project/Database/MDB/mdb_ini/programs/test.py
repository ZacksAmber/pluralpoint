import os
import subprocess
import time
import sys

'''
os.chdir("/Users/zacks/Desktop/Work/Pluralpoint Group Inc/SSRS Project/Database/MDB/mdb_ini/mysql_ini")
iniDir = os.getcwd()
iniFiles = os.listdir()

for iniFile in iniFiles:
    SETTINGS = iniFile
    print("Opening file " + iniFile)
    args = ["head", SETTINGS] # define the parameters for the .exe
    proc = subprocess.Popen(args)
    try:
        proc.wait()
        time.sleep(3)
        print("finished!\n")
    except:
        sys.exit()
'''

subprocess.run(['ls', '-l'])
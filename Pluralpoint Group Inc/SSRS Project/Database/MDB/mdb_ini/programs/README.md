## Prerequisite for `mdbConfig.py`:
__IMPORTANT__: Run `mdbConfig.py` on your MacBook or Linux before run `mdbMigrator.py.`
__ENV: MacOS or Linux, Python 3.7x, PIP.__
1. Make a directory named `programs` to store `mdbConfig.py` and `mdbMigrator.py`.
2. Make a directory named `mdb` to store mdb files.
3. Search `mdbtools` online and install it.
4. Module requirements: `numpy`.
---
## Prerequisite for `mdbMigrator.py`:
__IMPORTANT__: Run `mdbMigrator.py` on your Windows after run `mdbConfig.py`
__ENV: Windows, Python 3.7x, PIP.__
1. Make a directory named `programs` to store `mdbConfig.py` and `mdbMigrator.py`.
2. Make a directory named `mdb` to store mdb files.
3. Copy all of the following directories from your MacOS or Linux to Windows: `programs`, `mdb`, `*_ini`.
4. Modules Required: `mysql.connector`
- P.S: A better solution is sharing a folder through Windows and MackBook/Linux. And let them sync the files and directories automatically.
---
Sample .ini files:
- MySQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mysql.ini
- MSSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2mssql.ini
- PostgreSQL: https://github.com/ZacksAmber/Work/blob/master/Pluralpoint%20Group%20Inc/SSRS%20Project/Database/MDB/mdb_ini_samples/msa2prgsql.ini

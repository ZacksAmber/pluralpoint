-- Operations by Zacks

-- Endpoint: sql19.c9d5goyg8g3a.us-east-1.rds.amazonaws.com
-- Port: 1433
-- Running under Zacks AWS Account
-- Stopping instance may cause more than 10 minutes to restart

-- Logs

-- 10/14/2020
-- Restore database  from S3://pluraldata/advworks2008.bak (132.1 MB)

exec msdb.dbo.rds_restore_database
	@restore_db_name='ADW2008', 
	@s3_arn_to_restore_from='arn:aws:s3:::pluraldata/advworks2008.bak';

-- 10/15/2020
-- Restore database  from S3://pluraldata/XTRDB.bak (29.1 MB)

exec msdb.dbo.rds_restore_database
	@restore_db_name='XTRDB', 
	@s3_arn_to_restore_from='arn:aws:s3:::pluraldata/XTRDB.bak';

---

select name from master.sys.databases;

exec msdb.dbo.rds_task_status
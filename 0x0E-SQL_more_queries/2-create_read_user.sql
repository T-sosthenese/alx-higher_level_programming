-- Script that creates the database 'hbtn_0d_2' and 'user_0d_2'user
-- user_0d_2 should have only SELECT privilege in 'htn_0d_2' database
-- 'user_0d_2' password should be set to 'user_0d_2_pwd'
-- script does not fail if 'hbtn_0d_2' database or 'user_0d_2' exist

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

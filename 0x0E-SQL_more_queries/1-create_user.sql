-- A script that creates 'user_0d_1' user 
-- Gives the user above all the provileges
-- sets the password for 'user_0d_1' to 'user_0d_1_pwd'
-- Does not fail if 'user_0d_1' exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Creates 'hbtn_0d_usa' database with 'states' table in it
-- Does not fail if the database exists
-- Does not fail if the table exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_od_usa;

CREATE TABLE IF NOT EXISTS states(
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL);

-- Creates cities table in 'hbtn_0d_usa' database
-- Does not fail if the database exists
-- Does not fail if the table exists

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUT0_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);

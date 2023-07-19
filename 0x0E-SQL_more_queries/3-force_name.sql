-- Creates 'force_name' table of MySQL server
-- If 'force_name' table exists, the script does not fail

CREATE TABLE IF NOT EXISTS force_name(
	id INT,
	name VARCHAR(256) NOT NULL);

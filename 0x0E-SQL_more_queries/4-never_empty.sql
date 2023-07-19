-- Creates 'id_not_null' table on MySQL server
-- Does not fail if the table exists

CREATE TABLE IF NOT EXISTS id_not_null(
	id INT DEFAULT 1,
	name VARCHAR(256)NOT NULL);

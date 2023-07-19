-- Creates 'unique_id' table in MySQL server
-- Does not fail if the table exists

CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));

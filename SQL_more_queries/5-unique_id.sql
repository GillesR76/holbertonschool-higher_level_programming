-- create a table called 'unique_id' if it doesn't already exist.
CREATE TABLE IF NOT EXISTS unique_id (
    -- 'id' column of type INT with a default value of 1 and a unique constraint
    id INT DEFAULT 1 UNIQUE,
    -- 'name' column of type VARCHAR(256)
    name VARCHAR(256)
);
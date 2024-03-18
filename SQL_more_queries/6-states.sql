-- create a database called hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- setting it as the active database for the creation of the table
USE hbtn_0d_usa;
-- creation of a table called "states"
CREATE TABLE IF NOT EXISTS states (
    -- setting the id column : an auto-incrementing integer that serves as the primary key
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    -- column that sets a non-null string that represents the name of the state
    name VARCHAR(256) NOT NULL,
    -- setting the id column as the primary key
    PRIMARY KEY (id)
);
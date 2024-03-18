-- script that creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- setting it as the active database for the creation of the table
USE hbtn_0d_usa;
-- creation of a table called cities
CREATE TABLE IF NOT EXISTS cities (
-- setting the id column : an auto-incrementing integer that serves as the primary key
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    -- stores the foreign key referencing the "id" column of the "states" table
    state_id INT NOT NULL,
    -- stores the name of the city. It cannot be nul
    name VARCHAR(256) NOT NULL,
    -- primary key constraint is set on the "id" column
    PRIMARY KEY (id),
    -- foreign key constraint is set on the "state_id" column
    FOREIGN KEY (state_id) REFERENCES states(id)
);
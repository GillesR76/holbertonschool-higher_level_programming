/*
    This SQL script creates a table called 'force_name' if it doesn't already exist.
    The table has two columns:
    - id: an integer column
    - name: a non-null varchar column with a maximum length of 256 characters
*/
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
-- create a second table with multiple rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
-- insert multiple rows in new table
INSERT INTO second_table VALUES
(1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14),
(4, "George", 8);


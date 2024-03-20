-- selects the id, name of cities, and name of states from the 'cities' table and 'states' table
SELECT cities.id, cities.name, states.name 
FROM cities
-- using Inner Join on the 'state_id' column of the
-- 'cities' table and the 'id' column of the 'states' table
INNER JOIN states ON cities.state_id = states.id
-- result ordered by the 'id' column of the 'cities' table
ORDER BY cities.id;
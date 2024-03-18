/*
    This SQL query selects the id and name of cities in the state of California.
    It uses a subquery to retrieve the id of the state with the name 'California',
    and then selects all cities that have a state_id equal to the retrieved id.
    The result is ordered by the city id in ascending order.
*/
SELECT id, name FROM cities WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id;

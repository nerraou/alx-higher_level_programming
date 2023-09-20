-- This scipt creates the table cities on your MySQL server.
SELECT cities.id, cities.name, states.name FROM cities, states
WHERE state_id = states.id
ORDER BY id;

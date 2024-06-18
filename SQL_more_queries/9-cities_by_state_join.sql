-- list all cities along the corresponding state names
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = state_id
ORDER BY cities.id
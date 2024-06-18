-- list all cities along the corresponding state names

SELECT c.id, c.name AS city_name, s.name AS state_name 
FROM cities AS c INNER JOIN states AS s ON c.state_id = s.id 
ORDER BY c.id;
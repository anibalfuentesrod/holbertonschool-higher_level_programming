-- this writes the list of all the records of a score >= 10 in table second...
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
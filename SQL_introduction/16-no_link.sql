-- Lists all records of the table `second_table`, excluding rows with a NULL name.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
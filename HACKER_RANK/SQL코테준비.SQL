/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT Name||'('||substr(Occupation,1,1)||')' FROM OCCUPATIONS
ORDER BY Name ASC;

SELECT 'There are a total of '||count(Name)||' '||LOWER(Occupation)||'s.'
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY count(Name),Occupation ASC;


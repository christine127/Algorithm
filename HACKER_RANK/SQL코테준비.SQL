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

--이진트리
SELECT DISTINCT BST.N, 
    CASE WHEN BST.P IS NULL THEN 'Root'
        WHEN BST2.N IS NULL THEN 'Leaf'
        ELSE 'Inner'
    END
FROM BST
LEFT JOIN BST "BST2" ON BST.N= BST2.P
ORDER BY BST.N ASC;
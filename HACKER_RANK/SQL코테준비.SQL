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
ORDER BY BST.N ASC;]

select C.company_code,C.founder, count(distinct L.lead_manager_code),count(distinct S.senior_manager_code),count(distinct M.manager_code),count(distinct E.employee_code)
from Company "C", Lead_Manager "L",Senior_Manager "S",Manager "M", Employee "E"
where C.company_code  =L.company_code
and M.company_code  =L.company_code
and M.company_code  =S.company_code
and S.company_code  =E.company_code
GROUP BY C.company_code,C.founder
order by C.company_code asc;
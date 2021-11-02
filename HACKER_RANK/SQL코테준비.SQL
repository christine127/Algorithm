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

--mssql Occupation
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
set @r1 = 0,@r2 = 0, @r3=0, @r4 = 0;
with temp as(
select *, 
    case Occupation 
        when 'Doctor' then(@r1 := @r1+1)
        when 'Professor' then(@r2 := @r2+1)
        when 'Singer' then(@r3 := @r3+1)
        when 'Actor' then(@r4 := @r4+1)
        end as rownum,
    case Occupation when 'Doctor' then name end as Doctor,
    case Occupation when 'Professor' then name end as Professor,
    case Occupation when 'Singer' then name end as Singer,
    case Occupation when 'Actor' then name end as Actor
    from Occupations
    order by Name
)

select min(Doctor), min(Professor),min(Singer),min(Actor)
from temp
group by rownum;
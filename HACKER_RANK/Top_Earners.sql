-- Where절 서브쿼리

SELECT MAX(months * salary) max_total, Count(*)
FROM Employee
WHERE months*salary = (SELECT MAX(months * salary) max_total
                       FROM Employee E1)
                       
-- Having절 서브쿼리

SELECT months * salary AS earnings
FROM Employee
GROUP BY earnings
HAVING earnings = (SELECT MAX(months * salary) FROM Employee )                        

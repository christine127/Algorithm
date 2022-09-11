SELECT D.name AS Department, E.name AS Employee, E.salary
FROM Employee E, 
     Department D
WHERE (E.departmentId, E.salary) in (SELECT departmentId, MAX(Salary)
                                    FROM Employee
                                    GROUP BY departmentId) 
AND E.departmentId = D.id

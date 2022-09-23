-- 서브쿼리 
SELECT D.name AS Department, E.name AS Employee, E.salary
FROM Employee E, 
     Department D
WHERE (E.departmentId, E.salary) in (SELECT departmentId, MAX(Salary)
                                    FROM Employee
                                    GROUP BY departmentId) 
AND E.departmentId = D.id


-- 윈도우함수(나의 답안)
SELECT
    Department, 
    Employee,
    MaxSalary AS Salary
FROM
    (SELECT 
        D.name AS Department, 
        E.name AS Employee,
        E.Salary,
        MAX(E.salary) OVER (Partition BY departmentId) AS MaxSalary
    FROM 
        Employee AS E INNER JOIN Department AS D ON E.departmentId = D.id) AS T
WHERE T.Salary = MaxSalary

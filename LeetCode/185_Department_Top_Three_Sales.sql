

SELECT 
    T.Department, 
    T.name AS 'Employee',
    T.Salary
FROM
    (
    SELECT
        E.* ,
        D.name AS 'Department',
        DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS 'dense_rank'
    FROM Employee AS E INNER JOIN Department AS D ON E.departmentId = D.id
    ) AS T
WHERE 
    dense_rank <= 3
 

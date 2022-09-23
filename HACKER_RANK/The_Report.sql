SELECT 
    CASE WHEN 8 <= g.grade THEN s.name
    END AS Name,
    g.grade,
    s.marks 
FROM 
    students AS s LEFT JOIN grades as g 
    ON (CASE WHEN s.marks = 100 THEN g.grade = 10
             ELSE TRUNCATE(s.marks, -1) = g.min_mark END)
ORDER BY 
    g.grade DESC,
    s.name ASC,
    s.marks ASC

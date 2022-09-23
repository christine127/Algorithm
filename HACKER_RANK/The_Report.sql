-- 나의 답안
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

-- 정답(인프런 백문이 불여일타)
SELECT 
    CASE WHEN 8 <= g.grade THEN s.name
    END AS Name,
    g.grade,
    s.marks 
FROM 
    students AS s INNER JOIN grades as g 
    ON s.marks BETWEEN g.min_mark AND g.max_mark
ORDER BY 
    g.grade DESC,
    s.name ASC,
    s.marks ASC

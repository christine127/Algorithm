
SELECT DISTINCT L1.num AS ConsecutiveNums
FROM 
    Logs AS L1 
    INNER JOIN Logs AS L2 ON L1.ID+1 = L2.ID
    INNER JOIN Logs AS L3 ON L1.ID+2 = L3.ID
WHERE L1.num = L2.num
AND L2.num = L3.num

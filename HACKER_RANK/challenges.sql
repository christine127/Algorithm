
SELECT H.HACKER_ID, H.NAME, COUNT(CHALLENGE_ID) AS CHALLENGES_CREATED
FROM HACKERS H, CHALLENGES C
WHERE H.HACKER_ID = C.HACKER_ID
GROUP BY H.HACKER_ID, H.NAME
HAVING CHALLENGES_CREATED IN 
        (SELECT T.CNT
        FROM
            (SELECT HACKER_ID, COUNT(CHALLENGE_ID) CNT
            FROM CHALLENGES 
            GROUP BY HACKER_ID) T
        GROUP BY T.CNT
        HAVING COUNT(T.HACKER_ID) = 1)
        OR
        CHALLENGES_CREATED = 
        (SELECT MAX(CNT)
        FROM
        (SELECT HACKER_ID, COUNT(CHALLENGE_ID) CNT
            FROM CHALLENGES 
            GROUP BY HACKER_ID) T)
ORDER BY 3 DESC, 1 ASC


-- 풀이 ver.02
SELECT H.hacker_id
    ,  H.name
    ,  COUNT(*) AS challenges_created
FROM Hackers AS H
     INNER JOIN Challenges AS C ON H.hacker_id = C.hacker_id
GROUP BY H.hacker_id, H.name
HAVING challenges_created = (SELECT MAX(cnt)
                             FROM
                                (SELECT hacker_id, COUNT(*) AS cnt
                                 FROM Challenges
                                 GROUP BY hacker_id
                                 ) AS C
                             )
OR challenges_created IN  (SELECT cnt
                          FROM
                             (SELECT hacker_id, COUNT(*) AS cnt
                              FROM Challenges
                              GROUP BY hacker_id
                              ) AS C
                          GROUP BY cnt
                          HAVING count(cnt) = 1
                             )
ORDER BY challenges_created DESC, H.hacker_id

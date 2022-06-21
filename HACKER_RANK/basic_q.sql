
-- ends with vowel
select distinct(CITY)
from STATION
where right(CITY,1) IN ('a','e','i','o','u')


-- start or end with vowel
select distinct(city)
from STATION
where left(CITY,1) IN ('a','e','i','o','u') AND right(CITY,1) IN ('a','e','i','o','u')


--SUBSTRING
SELECT Name
FROM STUDENTS
WHERE Marks > 75
ORDER BY SUBSTRING(Name,-3,3) ASC ,ID ASC

SELECT T1.HACKER_ID, T1.NAME, SUM(SCORE) TOTAL_SCORE
FROM HACKERS T1
LEFT JOIN (SELECT HACKER_ID, MAX(SCORE) SCORE
           FROM SUBMISSIONS
           GROUP BY CHALLENGE_ID, HACKER_ID) T2 ON T1.HACKER_ID = T2.HACKER_ID
GROUP BY T1.HACKER_ID, T1.NAME
HAVING TOTAL_SCORE > 0
ORDER BY TOTAL_SCORE DESC, T1.HACKER_ID ASC


--UPDATE 문에서 조건으로 CASE문 사용이 가능하다

UPDATE salary SET sex = CASE WHEN sex = 'f' THEN 'm'
                              ELSE 'f' END
                              
                             
                             

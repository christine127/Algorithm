set @row_index := -1;

select round(avg(LAT_N),4) as median_value
from (SELECT @row_index := @row_index+1 as row_index, LAT_N
     FROM STATION
     ORDER BY LAT_N
     ) AS subq
     WHERE subq.row_index
     IN (FLOOR(@row_index/2), CEIL(@row_index/2))
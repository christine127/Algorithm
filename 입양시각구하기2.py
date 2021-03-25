
-- hour table만들기
with recursive hour_table as(
select 0 as hour
union all
select hour+1 from hour_table where hour < 23)
# select h.hour from hour_table h 


select h.hour, ifnull(a.cnt,0) count
from hour_table h
left join (select count(animal_id) cnt, hour(datetime) h_date
from animal_outs 
group by hour(datetime))a
on h.hour = a.h_date 
order by h.hour asc;
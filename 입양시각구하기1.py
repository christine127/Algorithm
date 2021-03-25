# -- 코드를 입력하세요


select t.hour, count(animal_id) as count
from 
(select *,
case
    when "09:00:00" <= time(datetime) and time(datetime) < "10:00:00" then "09"
    when "10:00:00"<= time(datetime) and time(datetime) < "11:00:00" then "10"
    when "11:00:00"<= time(datetime) and time(datetime) < "12:00:00" then "11"
    when "12:00:00"<= time(datetime) and time(datetime) < "13:00:00" then "12"
    when "13:00:00"<= time(datetime) and time(datetime) < "14:00:00" then "13"
    when "14:00:00"<= time(datetime) and time(datetime) < "15:00:00" then "14"
    when "15:00:00"<= time(datetime) and time(datetime) < "16:00:00" then "15"
    when "16:00:00"<= time(datetime) and time(datetime) < "17:00:00" then "16"
    when "17:00:00"<= time(datetime) and time(datetime) < "18:00:00" then "17"
    when "18:00:00"<= time(datetime) and time(datetime) < "19:00:00" then "18"
    when "19:00:00"<= time(datetime) and time(datetime) < "20:00:00" then "19"
end as HOUR
from animal_outs)T
where hour is not null
group by hour
order by hour asc;

set @end_date_lag := (select end_date from projects limit 1);
set @project_id := 0;

select min(start_date), max(end_date)
from
    (select task_id, start_date, end_date, 
           case when abs(datediff(end_date, end_date_lag)) <=1 then @project_id
           else @project_id := @project_id + 1 end as p_id
    from 
            (select task_id, start_date,@end_date_lag as end_date_lag, @end_date_lag := end_date as end_date
            from projects
            order by end_date) T)T1
group by p_id
order by datediff(max(end_date),min(start_date)),1
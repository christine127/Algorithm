-- animal_id, name 차집합
SELECT b.animal_id,b.name
from animal_ins a
right join animal_outs b
on a.animal_id = b.animal_id
where a.animal_id is null;
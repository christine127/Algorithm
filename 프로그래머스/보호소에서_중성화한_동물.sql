-- 코드를 입력하세요
SELECT o.animal_id animal_id, o.animal_type animal_type, o.name name
from animal_outs o, animal_ins i
where o.animal_id = i.animal_id
and not i.sex_upon_intake = "Neutered Male" 
and not i.sex_upon_intake = "Spayed Female"
and (o.sex_upon_outcome = "Neutered Male" or o.sex_upon_outcome = "Spayed Female")
order by o.animal_id;
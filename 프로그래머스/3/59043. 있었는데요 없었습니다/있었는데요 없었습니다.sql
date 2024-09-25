-- 코드를 입력하세요
SELECT b.animal_id as ANIMAL_ID, b.name as NAME
from animal_outs b 
join animal_ins a on a.animal_id = b.animal_id 
where b.datetime < a.datetime
order by a.datetime asc

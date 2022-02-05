-- 서브쿼리
select  name,
        datetime
from    animal_ins 
where   animal_id not in
        (
            select  animal_id
            from    animal_outs
        )
order by datetime
limit 3

-- left join
SELECT  I.name,
        I.datetime
from    animal_ins I
left join animal_outs O
on      I.animal_id = O.animal_id
where   O.animal_id is null
order by I.datetime
limit 3
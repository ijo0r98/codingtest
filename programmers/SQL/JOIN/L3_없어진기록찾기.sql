-- JOIN > 없어진 기록 찾기

select  animal_id,
        name
from    animal_outs
where   animal_id not in
        (
            select  O.animal_id
            from    animal_outs O
            inner join animal_ins I
            on      O.animal_id = I.animal_id
        )


select  animal_id,
        name
from    animal_outs
where   animal_id not in
        (
            select  animal_id
            from    animal_ins I
        )
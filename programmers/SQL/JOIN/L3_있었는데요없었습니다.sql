
-- 내 풀이
select  I.animal_id,
        I.name
from    animal_outs O
join    animal_ins I
on      O.animal_id = I.animal_id
where   (O.datetime - I.datetime) < 0 -- where   O.datetime < I.datetime
order by I.datetime


-- 다른 사람 풀이
SELECT  ANIMAL_INS.ANIMAL_ID, ANIMAL_INS.NAME
FROM    ANIMAL_INS
LEFT JOIN ANIMAL_OUTS
ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
WHERE   ANIMAL_INS.DATETIME > ANIMAL_OUTS.DATETIME
ORDER BY ANIMAL_INS.DATETIME

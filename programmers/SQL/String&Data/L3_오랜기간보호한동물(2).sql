-- 내 풀이(join)
select  I.animal_id,
        I.name
from    animal_ins I
join    animal_outs O
on      I.animal_id = O.animal_id
order by O.datetime - I.datetime desc
limit 2

-- join 안 쓴 풀이
SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS A, ANIMAL_OUTS B
WHERE A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY B.DATETIME-A.DATETIME DESC
LIMIT 2


-- 다른 사람 join & datetime 함수
SELECT  O.ANIMAL_ID, 
        O.NAME
FROM    ANIMAL_OUTS AS O
INNER JOIN  ANIMAL_INS AS I
ON  O.ANIMAL_ID = I.ANIMAL_ID
ORDER   BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT   2;
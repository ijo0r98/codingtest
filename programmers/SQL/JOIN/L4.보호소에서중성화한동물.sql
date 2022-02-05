-- 내 풀이
select  O.animal_id,
        O.animal_type,
        O.name
from    animal_outs O
left join animal_ins I
on  I.animal_id = O.animal_id
where I.sex_upon_intake like "%Intact%"
and (O.sex_upon_outcome like "%Spayed%" or O.sex_upon_outcome like "%Neutered%")
order by animal_id


-- 다른 사람 풀이
SELECT  I.ANIMAL_ID,
        I.ANIMAL_TYPE,
        I.NAME 
FROM    ANIMAL_INS as I
JOIN    ANIMAL_OUTS as O 
WHERE   I.ANIMAL_ID = O.ANIMAL_ID
AND     I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME -- 중성화함 -> 안함 상태변화는 없기 때문에
ORDER BY I.ANIMAL_ID
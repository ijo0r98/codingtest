-- order by
select  datetime "시간"
from    animal_ins
order by datetime desc
limit 1

-- max
select  max(datetime) "시간"
from    animal_ins
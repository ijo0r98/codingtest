select  hour(datetime),
        count(animal_id) as count
from    animal_outs
where hour(datetime) >= 9
and   hour(datetime) <= 20
group by hour(datetime)
order by hour(datetime)
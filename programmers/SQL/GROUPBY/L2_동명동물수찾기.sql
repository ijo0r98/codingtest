select name, count
from (
        select  name,
                count(animal_id) as count
        from animal_ins
        where name is not null
        group by name
        order by name
    ) T
where T.count > 1
SELECT  column1,
        column2
        CASE column3
            WHEN value1 THEN result1 -- when 조건식 then 반환값
            WHEN value2 THEN result2
            WHEN value3 THEN result3
        ELSE else_value -- 조건에 해당하지 않을 경우 반환값
        END,
        column4
FROM    table_name


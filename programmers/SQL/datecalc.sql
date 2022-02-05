-- 시간 더하기
DATE_ADD({기준 날짜}, INTERVAL)
SELECT DATE_ADD(NOW(), INTERVAL 1 SECOND);
SELECT DATE_ADD(NOW(), INTERVAL 1 MINUTE);
SELECT DATE_ADD(NOW(), INTERVAL 1 HOUR);
SELECT DATE_ADD(NOW(), INTERVAL 1 DAY);
SELECT DATE_ADD(NOW(), INTERVAL 1 MONTH);
SELECT DATE_ADD(NOW(), INTERVAL 1 YEAR);

-- 시간 빼기
DATE_SUB({기준 날짜}, INTERVAL)
SELECT DATE_ADD(NOW(), INTERVAL -1 YEAR);
SELECT DATE_SUB(NOW(), INTERVAL 1 YEAR);

-- 날짜에서 일부분 추출
SELECT YEAR(NOW()); -- 년
SELECT DAY(NOW()); -- 일
SELECT DAYOFMONTH(NOW()); -- 일

-- datetime, time diff
DATEDIFF('expr1', 'expr2') -- 두 기간 사이의 일수 계산, 시간은 신경 안씀
-- YYYY-MM-DD, YYYY-MM-DD HH:MM:SS
TIMEDIFF('expr1', 'expr2') -- 두 기간 사이의 시간 계산
-- HH:MM:SS, YYYY-MM-DD HH:MM:SS
PERIOD_DIFF('expr1', 'expr2') -- 두 기간 사이의 개월 수 계산
-- YYYYMM, YYMM
TIMESTAMPDIFF(result_type, 'expr1', 'expr2') -- 두 기간 사이의 시간 계산
-- FRAC_SECOND (MICROSECOND, 마이크로 초), SECOND(초), MINUTE(분), HOUR(시간), DAY(일), WEEK(주), MONTH(월), QUARTER(분기), YEAR

-- * date_format()으로 형 변환 후 이용하는 것이 좋음

select now(); -- 2022-02-05 11:52:51
select datediff(now(), '2022-02-03'); -- 2
select datediff(now(), '2022-02-10'); -- -5
select datediff(now(), '2022-13-10'); -- NULL

select timediff(now(), '2022-02-05 15:00:00'); -- -03:04:57
select timediff(current_timestamp(), '2022-02-04 15:00:00'); -- 20:55:35

select period_diff(date_format(now(), "%Y%m"), '202201'); -- 1

select timestampdiff(day, now(), '2022-01-01'); -- -35
select timestampdiff(month, now(), '2022-01-01'); -- -1


-- 코드를 입력하세요
SELECT month(START_DATE) as MONTH,
    CAR_ID, count(HISTORY_ID) as RECORDS
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where START_DATE>="2022-08-01" and START_DATE<"2022-11-01"
    and CAR_ID in (
        select CAR_ID
        from CAR_RENTAL_COMPANY_RENTAL_HISTORY
        where START_DATE>="2022-08-01" and START_DATE<"2022-11-01" 
        group by car_id 
        having count(history_id)>4)
group by CAR_ID, MONTH
order by MONTH, CAR_ID desc
-- 코드를 입력하세요
SELECT h.HISTORY_ID,
case 
    when datediff(h.END_DATE, h.START_DATE) >= 90 then round((c.DAILY_FEE * (datediff(h.END_DATE, h.START_DATE)+1))*0.85)
    when datediff(h.END_DATE, h.START_DATE) >= 30 then round((c.DAILY_FEE * (datediff(h.END_DATE, h.START_DATE)+1))*0.92)
    when datediff(h.END_DATE, h.START_DATE) >= 7 then round((c.DAILY_FEE * (datediff(h.END_DATE, h.START_DATE)+1))*0.95)
    else round((c.DAILY_FEE * (datediff(h.END_DATE, h.START_DATE)+1)))
end as FEE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h join CAR_RENTAL_COMPANY_CAR c
on c.CAR_ID = h.CAR_ID
join CAR_RENTAL_COMPANY_DISCOUNT_PLAN d
on c.CAR_TYPE = d.CAR_TYPE
where c.CAR_TYPE = '트럭'
group by h.HISTORY_ID
order by FEE desc, h.HISTORY_ID desc
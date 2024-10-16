-- 코드를 입력하세요
SELECT year(s.SALES_DATE) as YEAR, month(s.SALES_DATE) as MONTH, i.GENDER, count(distinct s.USER_ID) as USERS
from USER_INFO i join ONLINE_SALE s
on i.USER_ID = s.USER_ID
group by year(s.SALES_DATE), month(s.SALES_DATE), i.GENDER	
having i.GENDER	is not NULL
order by year(s.SALES_DATE), month(s.SALES_DATE), i.GENDER	
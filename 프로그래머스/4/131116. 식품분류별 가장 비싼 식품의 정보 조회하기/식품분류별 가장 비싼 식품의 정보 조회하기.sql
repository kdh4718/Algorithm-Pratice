-- 코드를 입력하세요
SELECT CATEGORY, PRICE, PRODUCT_NAME
from FOOD_PRODUCT 
where PRICE in (
    select max(PRICE)
    from FOOD_PRODUCT
    group by CATEGORY)
    and CATEGORY in ('과자', '국', '김치', '식용유')
order by PRICE desc
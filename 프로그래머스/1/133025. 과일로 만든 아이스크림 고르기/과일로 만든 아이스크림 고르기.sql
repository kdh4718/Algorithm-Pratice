-- 코드를 입력하세요
SELECT f.FLAVOR
from ICECREAM_INFO e right join FIRST_HALF f
on e.FLAVOR = f.FLAVOR
where e.INGREDIENT_TYPE = 'fruit_based' and f.TOTAL_ORDER >= 3000
order by f.TOTAL_ORDER desc
-- 코드를 작성해주세요
select ID, LENGTH
from FISH_INFO
where LENGTH
order by LENGTH desc, ID
limit 10

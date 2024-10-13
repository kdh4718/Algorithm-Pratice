-- 코드를 작성해주세요
select count(i.ID) as FISH_COUNT, n.FISH_NAME
from FISH_INFO i left join FISH_NAME_INFO n
on i.FISH_TYPE = n.FISH_TYPE
group by n.FISH_NAME
order by FISH_COUNT desc
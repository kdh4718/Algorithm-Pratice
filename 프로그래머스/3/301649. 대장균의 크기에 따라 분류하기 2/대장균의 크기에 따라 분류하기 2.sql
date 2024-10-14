-- 코드를 작성해주세요
select a.ID, 
    case
        when a.percent <= 0.25 then 'CRITICAL'
        when a.percent <= 0.5 then 'HIGH'
        when a.percent <= 0.75 then 'MEDIUM'
        when a.percent <= 1 then 'LOW'
    end as 'COLONY_NAME'
from (
    select ID, percent_rank() over (order by SIZE_OF_COLONY desc) 
    as percent
    from ECOLI_DATA ) a
order by a.ID
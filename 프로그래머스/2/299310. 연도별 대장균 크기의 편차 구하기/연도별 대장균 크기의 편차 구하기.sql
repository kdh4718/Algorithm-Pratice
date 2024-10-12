-- 코드를 작성해주세요
select year(a.DIFFERENTIATION_DATE) as YEAR	
    , abs(b.size - a.SIZE_OF_COLONY) as YEAR_DEV
    , a.ID
from ECOLI_DATA a
    left join (select year(DIFFERENTIATION_DATE) as YEAR
               , max(SIZE_OF_COLONY) as size
              from ECOLI_DATA 
              group by year(DIFFERENTIATION_DATE)) b
on year(a.DIFFERENTIATION_DATE) = b.YEAR
order by YEAR, YEAR_DEV 
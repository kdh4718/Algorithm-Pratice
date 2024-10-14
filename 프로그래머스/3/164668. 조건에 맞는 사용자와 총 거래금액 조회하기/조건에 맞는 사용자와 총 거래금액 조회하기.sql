-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, b.TOTAL_SALES
from USED_GOODS_USER u join (
    select WRITER_ID, sum(PRICE) as TOTAL_SALES
    from USED_GOODS_BOARD 
    where STATUS = 'DONE'
    group by WRITER_ID) b
on u.USER_ID = b.WRITER_ID
where b.TOTAL_SALES >= 700000
order by b.TOTAL_SALES

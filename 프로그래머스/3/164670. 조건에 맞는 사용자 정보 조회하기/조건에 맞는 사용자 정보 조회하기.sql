-- 코드를 입력하세요
SELECT u.USER_ID, u.NICKNAME, concat(u.CITY, " ", u.STREET_ADDRESS1, " ", u.STREET_ADDRESS2) as '전체주소',
CONCAT(
        SUBSTRING(u.TLNO, 1, 3), '-',  
        SUBSTRING(u.TLNO, 4, 4), '-',  
        SUBSTRING(u.TLNO, 8, 4)         
    ) AS '전화번호'
from USED_GOODS_BOARD b join USED_GOODS_USER u
on b.WRITER_ID = u.USER_ID
where b.WRITER_ID is not NULL
group by u.USER_ID
having count(b.BOARD_ID) >= 3
order by u.USER_ID desc
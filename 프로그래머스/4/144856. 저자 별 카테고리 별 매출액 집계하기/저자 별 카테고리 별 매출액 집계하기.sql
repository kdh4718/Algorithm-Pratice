-- 코드를 입력하세요
SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY,
    sum(b.PRICE * s.SALES) as TOTAL_SALES
from AUTHOR a join Book b
on b.AUTHOR_ID = a.AUTHOR_ID
join BOOK_SALES s
on b.BOOK_ID = s.BOOK_ID
where SALES_DATE like '2022-01-%'
group by b.AUTHOR_ID, b.CATEGORY
order by a.AUTHOR_ID, b.CATEGORY desc
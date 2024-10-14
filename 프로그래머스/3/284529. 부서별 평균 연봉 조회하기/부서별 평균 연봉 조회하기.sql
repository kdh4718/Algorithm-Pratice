-- 코드를 작성해주세요
select d.DEPT_ID, d.DEPT_NAME_EN, e.AVG_SAL
from HR_DEPARTMENT d join (
    select DEPT_ID, round(avg(SAL)) as AVG_SAL
    from HR_EMPLOYEES
    group by DEPT_ID) e
on d.DEPT_ID = e.DEPT_ID
order by e.AVG_SAL desc
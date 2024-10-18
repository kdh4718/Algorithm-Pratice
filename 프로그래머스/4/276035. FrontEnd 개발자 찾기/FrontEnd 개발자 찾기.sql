-- 코드를 작성해주세요
select d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from SKILLCODES s, DEVELOPERS d
where s.CODE & d.SKILL_CODE = s.CODE
    and s.CATEGORY = 'Front End'
group by d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
order by d.ID
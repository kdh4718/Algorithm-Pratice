-- 코드를 작성해주세요
select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i join ITEM_TREE t
on i.ITEM_ID = t.ITEM_ID
where i.ITEM_ID not in (
    select PARENT_ITEM_ID
    from ITEM_TREE
    where PARENT_ITEM_ID is not NULL
    group by PARENT_ITEM_ID)
order by i.ITEM_ID desc
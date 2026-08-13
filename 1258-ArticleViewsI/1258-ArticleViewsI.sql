-- Last updated: 8/13/2026, 8:21:48 PM
# Write your MySQL query statement below
select distinct author_id as id
from Views as v
where v.author_id=v.viewer_id
order by id asc
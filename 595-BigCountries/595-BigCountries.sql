-- Last updated: 8/13/2026, 8:22:42 PM
# Write your MySQL query statement below
select name, population,area
from World
where
 population>=25000000 or area>=3000000;
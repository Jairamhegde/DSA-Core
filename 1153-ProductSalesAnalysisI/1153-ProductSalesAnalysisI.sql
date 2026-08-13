-- Last updated: 8/13/2026, 8:21:57 PM
# Write your MySQL query statement below
select a.product_name,b.year,b.price
from Product as a
right join Sales as b
on a.product_id=b.product_id
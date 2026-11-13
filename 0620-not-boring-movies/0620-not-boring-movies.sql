-- Write your PostgreSQL query statement below
select id,movie,description,rating
from Cinema
where id % 2 <> 0 and description <>'boring'
order by rating desc;

/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
with temp as (
select num,id , 
LAG(num,1) OVER( ) as p1,
LAG(num,2) OVER( ) as p2
from Logs
)
select distinct num as ConsecutiveNums 
from temp 
where num = p1 and num =p2;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
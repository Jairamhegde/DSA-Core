with t as (
select id,  salary , dense_rank() over(order by salary desc) as Salary_rank
from Employee 
)
select (
select distinct salary 
from t
where Salary_rank = 2)
as SecondHighestSalary 

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
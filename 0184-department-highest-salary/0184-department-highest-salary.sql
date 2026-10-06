with temp as (
select d.name as Department,e.name as Employee,e.salary as Salary,
max(e.salary) over(partition by d.name) as maxsal
from Employee e
join Department d on e.departmentId = d.id
)
select  Department,Employee, Salary
from temp
where Salary = maxsal;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
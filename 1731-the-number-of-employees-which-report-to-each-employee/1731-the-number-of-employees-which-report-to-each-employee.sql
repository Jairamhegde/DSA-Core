-- Write your PostgreSQL query statement below

with temp as (
select e1.reports_to as employee_id,count(*) as reports_count,avg(e1.age) as average_age
from Employees e1
join Employees e2 on e1.reports_to = e2.employee_id
group by e1.reports_to
)
select t.employee_id, e.name , t.reports_count,round(t.average_age,0) as average_age
from temp t
join Employees e on e.employee_id = t.employee_id
order by t.employee_id;

/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
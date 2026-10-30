-- Write your PostgreSQL query statement below
with ranked as (
    select d.id as Department_id,e.Salary,d.name  as Department,e.id as emp_id,e.name as Employee, DENSE_RANK() OVER(partition by d.id order by e.Salary desc) as rnk
    from Department d
    join Employee e on d.id = e.departmentId
)
select Department,Employee,Salary
from ranked
where rnk <=3
;





/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
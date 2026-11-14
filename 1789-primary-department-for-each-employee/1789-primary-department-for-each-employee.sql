-- Write your PostgreSQL query statement below
select distinct outer_emp.employee_id,
case 
when
count(*) over(partition by outer_emp.employee_id) = 1 then outer_emp.department_id else (select e.department_id from Employee e where e.employee_id = outer_emp.employee_id and e.primary_flag = 'Y' limit 1)
end as department_id
from Employee outer_emp
;



/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
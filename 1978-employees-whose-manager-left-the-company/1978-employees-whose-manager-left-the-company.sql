select employee_id
from Employees
where manager_id not in (
    select employee_id
    from Employees
) and salary < 30000 
order by employee_id asc;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
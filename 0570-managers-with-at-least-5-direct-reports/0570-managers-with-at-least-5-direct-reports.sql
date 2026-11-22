with temp as (
select e2.id
from Employee e
join Employee e2 on e.managerId = e2.id
group by e2.id
having count(*) >=5
)
select e.name
from Employee e
join temp t on e.id = t.id;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
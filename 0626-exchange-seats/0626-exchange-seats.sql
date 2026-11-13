-- Write your PostgreSQL query statement below
select s1.id, 
case
when s1.id % 2 = 0 then 
    (select student 
    from Seat s2
    where s2.id = s1.id -1)

when s1.id % 2 > 0 and s1.id <> (select max(id) from Seat) 
then(
    select s2.student
    from Seat s2
    where s2.id = s1.id + 1
    )
else s1.student 
end as student
from Seat s1;


/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
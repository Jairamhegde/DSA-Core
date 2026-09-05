select name as Customers
from Customers 
where id not in (
    select c.id 
    from Customers c
    inner join Orders o on c.id = o.customerId
);


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
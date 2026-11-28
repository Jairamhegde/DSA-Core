WITH temp AS (
    SELECT 
        s.user_id,
        COUNT(c.action) AS total_request,
        COUNT(c.action) FILTER (WHERE c.action = 'confirmed') AS confirmed
    FROM Signups s
    LEFT JOIN Confirmations c ON s.user_id = c.user_id
    GROUP BY s.user_id
)
SELECT 
    user_id,
    COALESCE(ROUND(confirmed::numeric / NULLIF(total_request, 0), 2), 0) AS confirmation_rate
FROM temp;

/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
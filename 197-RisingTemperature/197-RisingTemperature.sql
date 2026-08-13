-- Last updated: 8/13/2026, 8:25:13 PM
# Write your MySQL query statement below
SELECT w2.id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w2.RecordDate, w1.RecordDate) = 1
               AND w2.Temperature > w1.Temperature
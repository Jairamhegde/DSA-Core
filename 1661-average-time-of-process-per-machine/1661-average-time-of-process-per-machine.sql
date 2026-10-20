with each_proces_time as (
    select machine_id,process_id, (max(timestamp) - min(timestamp)) as time_taken
    from Activity
    group by machine_id,process_id
)

-- select * from each_proces_time;
select machine_id,
round(sum(time_taken)/count(*),3) as processing_time
from each_proces_time
group by machine_id;

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
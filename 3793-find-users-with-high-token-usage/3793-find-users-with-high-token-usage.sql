select user_id,count(*) as prompt_count,round(avg(tokens),2) as avg_tokens 
from prompts
group by user_id
having prompt_count >= 3 and max(tokens)> avg_tokens
order by avg_tokens desc,user_id asc ;


-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
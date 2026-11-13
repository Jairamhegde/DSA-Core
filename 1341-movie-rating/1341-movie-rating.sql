with gretest_user as (
    select u.user_id,u.name,count(distinct Mr.movie_id) as total
    from Users u
    join MovieRating Mr on u.user_id = Mr.user_id
    group by u.user_id,u.name
    order by total desc, u.name asc
    limit 1
),
best_movie as (
    select m.movie_id,m.title, avg(mr.rating) as average
    from Movies m
    join MovieRating mr on m.movie_id = mr.movie_id
    where  extract('month' from mr.created_at::date) = 2 and 
    extract('year' from mr.created_at::date) = 2020

    group by m.movie_id,m.title
    order by average desc, m.title asc
    limit 1
    
)

select name as results
from gretest_user
 union all
select title as results
from best_movie;



/*
Synced seamlessly with LeetHub Pro
Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
*/
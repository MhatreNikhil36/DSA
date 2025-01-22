with res1 as (
    select distinct user_id, count(user_id) over(partition by user_id) as c
    from MovieRating
),
res2 as (
    select movie_id, avg(rating) as avg_rating
    from MovieRating
    where created_at LIKE '2020-02%'
    group by movie_id
)
select results from (
    select name as results
    from users
    where user_id in (
        select user_id
        from res1
        where c = (select max(c) from res1)
    )
    order by name
    limit 1
) a
union all 
select results from (
    select title as results
    from movies
    where movie_id in (
        select movie_id
        from res2
        where avg_rating = (select max(avg_rating) from res2)
    )
    order by title
    limit 1
) b;

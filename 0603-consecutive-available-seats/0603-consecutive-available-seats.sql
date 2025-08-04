# Write your MySQL query statement below
select seat_id from (
select seat_id  ,free c,lead(free) over(order by seat_id) prev, lag(free) over(order by seat_id) nxt
 from
cinema) a
where c=1  and ( prev=1 or nxt=1 )
order by  seat_id

WITH multiple_ip_users as (
   SELECT
       account_id,
       count(distinct ip_address) as n_ips
   FROM LogInfo
   GROUP BY 1
   HAVING count(distinct ip_address) > 1
),
ip_cleaned as (
   SELECT
       a.account_id,
       ip_address,
       date(login) as date_of_login,
       min(login) as first_ip_login,
       max(logout) as last_ip_logout
   FROM LogInfo as a INNER JOIN multiple_ip_users as b
       on a.account_id = b.account_id
   GROUP BY 1,2,3
),
cte1 as (
   SELECT
       a.account_id,
       a.ip_address,
       a.first_ip_login,
       a.last_ip_logout,
       LAG(a.last_ip_logout,1,0) OVER (PArtition by account_id ORDER BY first_ip_login asc) as last_logout
       
   FROM ip_cleaned a
)

   SELECT
       account_id
   FROM cte1 
   WHERE first_ip_login <= last_logout
   GROUP BY 1
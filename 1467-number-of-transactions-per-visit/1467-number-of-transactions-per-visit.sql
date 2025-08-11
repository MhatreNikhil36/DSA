WITH 
    # This is to add 0s to dates when user visite but didn't complete a transaction
    num_transactions_by_users_by_date AS #nvbubd
    (
        SELECT v.user_id
            , visit_date
            , count(transaction_date) AS num_transactions
        FROM visits v
        LEFT JOIN Transactions t        
        ON v.user_id = t.user_id
        AND v.visit_date = t.transaction_date
        -- where v.user_id in (1,2) -- for testing only
        GROUP BY 1, 2
        ORDER BY 1, 2
    )
    
    , num_transactions_by_date AS #ntbd
    (
        SELECT user_id  # not really necessary but leaving it in for testing small use case
            ,visit_date
            , sum(num_transactions) AS num_transactions
        FROM num_transactions_by_users_by_date
        -- where user_id in (1,2)  # for testing only
        GROUP BY 1,2
        ORDER BY 1,2
    )
    
    # This is to list the give an ordered list starting from 0 up to the max_number_transactions      
    ,num_transactions AS #nt
    (
        SELECT row_number() over () as num_transactions
        FROM transactions
        UNION select 0   
    )
    
# ******************************************   
# Test CTEs
# ******************************************   

# SELECT * FROM num_transactions_by_users_by_date
# SELECT * FROM num_transactions_by_date
# SELECT * FROM num_transactions


# ******************************************   
# Max number of calculations
# ****************************************** 

# SELECT MAX(num_transactions) FROM num_transactions_by_date

# ******************************************   
# Final Query
# ******************************************  

SELECT nt.num_transactions AS transactions_count
	, COUNT(ntbd.num_transactions) AS visits_count
FROM num_transactions AS nt
LEFT JOIN num_transactions_by_date AS ntbd
ON nt.num_transactions = ntbd.num_transactions
WHERE nt.num_transactions <= (SELECT MAX(num_transactions) FROM num_transactions_by_date)
# AND ntbd.user_id in (1,2) -- for testing only
GROUP BY 1
ORDER by 1
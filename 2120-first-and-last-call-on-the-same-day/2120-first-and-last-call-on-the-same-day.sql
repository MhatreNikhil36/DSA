-- CTE to create a unified view of all calls, treating each user as a 'participant'
WITH UnifiedCalls AS (
  -- Include calls where the user is the caller
  SELECT 
    caller_id AS user_id, 
    call_time, 
    recipient_id AS other_participant_id 
  FROM 
    Calls 
  UNION 
    -- Include calls where the user is the recipient
  SELECT 
    recipient_id AS user_id, 
    call_time, 
    caller_id AS other_participant_id 
  FROM 
    Calls
), 
-- CTE to rank the calls for each user on each day
RankedCalls AS (
  SELECT 
    user_id, 
    other_participant_id, 
    DATE(call_time) AS call_date, 
    -- Extracting just the date part of call_time
    DENSE_RANK() OVER (
      PARTITION BY user_id, 
      DATE(call_time) 
      ORDER BY 
        call_time ASC
    ) AS rank_earliest_call, 
    DENSE_RANK() OVER (
      PARTITION BY user_id, 
      DATE(call_time) 
      ORDER BY 
        call_time DESC
    ) AS rank_latest_call 
  FROM 
    UnifiedCalls
) -- Selecting users whose first and last calls of the day were with the same person
SELECT 
  DISTINCT user_id 
FROM 
  RankedCalls 
WHERE 
  rank_earliest_call = 1 
  OR rank_latest_call = 1 -- Filtering for first and last calls
GROUP BY 
  user_id, 
  call_date 
HAVING 
  COUNT(DISTINCT other_participant_id) = 1;

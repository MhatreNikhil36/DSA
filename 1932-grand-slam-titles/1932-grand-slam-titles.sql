SELECT 
  p.player_id,
  p.player_name,
  COUNT(*) AS grand_slams_count
FROM Players p
JOIN (
    SELECT Wimbledon AS player_id FROM Championships
    UNION ALL
    SELECT Fr_open AS player_id FROM Championships
    UNION ALL
    SELECT US_open AS player_id FROM Championships
    UNION ALL
    SELECT Au_open AS player_id FROM Championships
) AS all_wins
ON p.player_id = all_wins.player_id
GROUP BY p.player_id, p.player_name
ORDER BY player_id;

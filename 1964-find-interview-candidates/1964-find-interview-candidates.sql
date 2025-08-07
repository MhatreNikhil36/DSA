WITH Medalists AS (
  SELECT gold_medal AS user_id, contest_id FROM Contests
  UNION ALL
  SELECT silver_medal, contest_id FROM Contests
  UNION ALL
  SELECT bronze_medal, contest_id FROM Contests
),
GoldWinners AS (
  SELECT gold_medal AS user_id
  FROM Contests
  GROUP BY gold_medal
  HAVING COUNT(*) >= 3
),
UserMedalSeq AS (
  SELECT
    user_id,
    contest_id,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY contest_id) AS rn
  FROM Medalists
),
ConsecutiveGroups AS (
  SELECT
    user_id,
    contest_id,
    rn,
    contest_id - rn AS grp
  FROM UserMedalSeq
),
ConsecutiveCounts AS (
  SELECT user_id, grp, COUNT(*) AS streak_length
  FROM ConsecutiveGroups
  GROUP BY user_id, grp
  HAVING COUNT(*) >= 3
),
ConsecutiveWinners AS (
  SELECT DISTINCT user_id FROM ConsecutiveCounts
),
InterviewCandidates AS (
  SELECT user_id FROM GoldWinners
  UNION
  SELECT user_id FROM ConsecutiveWinners
)
SELECT u.name, u.mail
FROM Users u
JOIN InterviewCandidates ic ON u.user_id = ic.user_id;

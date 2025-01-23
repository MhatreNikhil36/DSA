delete from person where id in (
SELECT id
FROM (
    SELECT id, email, ROW_NUMBER() OVER (PARTITION BY email ORDER BY id) AS rn
    FROM person
) a
WHERE rn !=1)

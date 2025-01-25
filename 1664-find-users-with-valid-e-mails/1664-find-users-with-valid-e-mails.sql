SELECT user_id, name, mail
FROM Users
-- Note that we also escaped the `@` character, as it has a special meaning in some regex flavors
WHERE mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*\\@leetcode\\.com$';
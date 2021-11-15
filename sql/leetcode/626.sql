-- https://leetcode.com/problems/exchange-seats/

SELECT
    CASE
        WHEN id % 2 <> 0
            AND id = (SELECT COUNT(*) FROM Seat) THEN id -- last index
        WHEN id % 2 = 0 THEN id - 1 
        ELSE id + 1
    END as id,
    student
FROM Seat
ORDER BY id;
        
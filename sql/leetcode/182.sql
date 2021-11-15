-- https://leetcode.com/problems/duplicate-emails/

SELECT Email from Person GROUP BY email HAVING COUNT(email) > 1;

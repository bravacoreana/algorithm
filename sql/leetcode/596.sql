-- https://leetcode.com/problems/classes-more-than-5-students/

SELECT class FROM courses GROUP BY class HAVING COUNT(*) >= 5;
-- https://leetcode.com/problems/rising-temperature/

SELECT a.id FROM Weather a, Weather b WHERE DATEDIFF(a.recordDate, b.recordDate) = 1 AND a.temperature > b.temperature;
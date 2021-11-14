-- https://leetcode.com/problems/big-countries/

SELECT name, population, area FROM World WHERE area >= 300000 AND population >= 25000000;
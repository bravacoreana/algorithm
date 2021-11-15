-- https://leetcode.com/problems/customers-who-never-order/

SELECT name AS Customers from Customers WHERE NOT EXISTS (SELECT customerId from Orders WHERE customerId = customers.id);
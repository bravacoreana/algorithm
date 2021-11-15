-- https://leetcode.com/problems/delete-duplicate-emails/

DELETE p from Person p, Person q WHERE p.id > q.id AND p.email=q.email;
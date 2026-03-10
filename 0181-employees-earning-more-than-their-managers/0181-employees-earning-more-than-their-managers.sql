# Write your MySQL query statement below
SELECT e.name as Employee FROM EMPLOYEE e
join EMPLOYEE m
on e.managerId = m.id
where e.salary > m.salary
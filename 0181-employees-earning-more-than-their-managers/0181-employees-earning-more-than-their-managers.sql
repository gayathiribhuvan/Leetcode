# Write your MySQL query statement below
#SELECT e.name as Employee FROM EMPLOYEE e
#join EMPLOYEE m
#on e.managerId = m.id
#where e.salary > m.salary'''

SELECT name as Employee 
from Employee 
where salary > (
    select m.salary from employee m
    where employee.managerID = m.id
)
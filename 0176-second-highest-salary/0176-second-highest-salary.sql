# Write your MySQL query statement below
SELECT MAX(SALARY) as SecondHighestSalary
FROM (
    SELECT SALARY, DENSE_RANK() OVER (ORDER BY SALARY DESC) AS r
    FROM EMPLOYEE
) t

WHERE r = 2;
# Write your MySQL query statement below
SELECT C.name AS 'Customers' FROM Customers C LEFT JOIN (SELECT customerId FROM Orders) O ON C.id = O.customerID WHERE O.customerID IS NULL;
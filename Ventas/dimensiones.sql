INSERT INTO Dim_Producto (nombre_producto, linea_producto, cantidad)
SELECT productName, productLine, SUM(quantityOrdered) AS cantidad
FROM products
JOIN orderdetails ON products.productCode = orderdetails.productCode
GROUP BY productName, productLine;


INSERT INTO Dim_Vendedor ( nombre_vendedor, apellido_vendedor)
SELECT DISTINCT  firstName, lastName
FROM employees;

INSERT INTO Dim_Oficina ( nombre_oficina, ubicacion_oficina)
SELECT DISTINCT officeCode, city
FROM offices;

INSERT INTO Dim_fecha ( fecha)
SELECT DISTINCT  orderDate
FROM orders;


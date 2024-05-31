-- ¿Cuántas ventas se han realizado en total?
SELECT COUNT(*) AS total_ventas FROM Ventas;

-- ¿Cuál es el valor total de las ventas?
SELECT SUM(valor_venta) AS valor_total_ventas FROM Ventas;

-- ¿Cuál es el valor de las ventas por año?
SELECT Dim_Fecha.fecha, SUM(Ventas.valor_venta) AS valor_ventas_por_año
FROM Ventas
JOIN Dim_Fecha ON Ventas.fecha_venta = Dim_Fecha.fecha
GROUP BY Dim_Fecha.fecha;

-- ¿Cuál es el valor de las ventas por línea de producto?
SELECT Dim_Producto.linea_producto, SUM(Ventas.valor_venta) AS valor_ventas_por_linea
FROM Ventas
JOIN Dim_Producto ON Ventas.id_producto = Dim_Producto.id_producto
GROUP BY Dim_Producto.linea_producto;

-- ¿Cuál es el valor de las ventas por vendedor?
SELECT CONCAT(Dim_Vendedor.nombre_vendedor, ' ', Dim_Vendedor.apellido_vendedor) AS nombre_vendedor,
       SUM(Ventas.valor_venta) AS valor_ventas_por_vendedor
FROM Ventas
JOIN Dim_Vendedor ON Ventas.id_vendedor = Dim_Vendedor.id_vendedor
GROUP BY Dim_Vendedor.id_vendedor;

-- ¿Cuál es el valor de las ventas por oficina?
SELECT Dim_Oficina.nombre_oficina, SUM(Ventas.valor_venta) AS valor_ventas_por_oficina
FROM Ventas
JOIN Dim_Oficina ON Ventas.id_oficina = Dim_Oficina.id_oficina
GROUP BY Dim_Oficina.nombre_oficina;

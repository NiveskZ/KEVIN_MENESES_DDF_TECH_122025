SELECT 
    CustomerName AS Cliente,
    COUNT(SalesOrderNumber) AS "Qtd Pedidos",
    SUM(TotalAmount) AS "Total Gasto"
FROM TB__HP84A8__SILVER__CDM_SALES_ORDER 
GROUP BY CustomerName
ORDER BY SUM(TotalAmount) DESC
LIMIT 1;
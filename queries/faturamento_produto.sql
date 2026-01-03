SELECT 
    Category AS Categoria, 
    SUM(TotalAmount) AS Faturamento
FROM TB__HP84A8__SILVER__CDM_SALES_ORDER
GROUP BY Category
ORDER BY Faturamento DESC;
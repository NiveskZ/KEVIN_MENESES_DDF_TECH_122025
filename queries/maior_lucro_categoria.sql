SELECT 
    v.Category AS Categoria,
    SUM((v.UnitPrice - p.StandardCost) * v.Quantity) AS Lucro_Total,
    SUM(v.TotalAmount) AS Faturamento_Total,
    (SUM((v.UnitPrice - p.StandardCost) * v.Quantity) / SUM(v.TotalAmount)) * 100 AS "Margem Percentual"
FROM TB__HP84A8__SILVER__CDM_SALES_ORDER v
LEFT JOIN TB__HP84A8__SILVER__CDM_PRODUCT p
ON p.id = v.productid 
GROUP BY 1
ORDER BY Lucro_Total DESC
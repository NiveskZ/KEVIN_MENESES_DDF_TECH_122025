WITH Metricas_Por_Categoria AS (
    SELECT 
        CASE 
            WHEN v.Category = 'Cerveja Artesanal' THEN 'Artesanal'
            WHEN v.Category = 'Cerveja Comum' THEN 'Comum'
            ELSE 'Outros'
        END AS Tipo_Cerveja,
        SUM(v.TotalAmount) AS Faturamento,
        SUM((v.UnitPrice - p.StandardCost) * v.Quantity) AS Lucro_Bruto
    FROM TB__HP84A8__SILVER__CDM_SALES_ORDER v
    LEFT JOIN TB__HP84A8__SILVER__CDM_PRODUCT p ON p.Id = v.ProductId
    WHERE v.Category IN ('Cerveja Artesanal', 'Cerveja Comum')
    GROUP BY 1
)
SELECT 
    Tipo_Cerveja,
    Lucro_Bruto 
FROM Metricas_Por_Categoria
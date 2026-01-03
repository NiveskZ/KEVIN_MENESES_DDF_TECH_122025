WITH Vendas_Diarias AS (
    SELECT 
        CAST(OrderDate AS DATE) AS Dia,
        SUM(TotalAmount) / COUNT(DISTINCT SalesOrderNumber) AS Ticket_Medio
    FROM TB__HP84A8__SILVER__CDM_SALES_ORDER 
    GROUP BY 1
),
Rankeamento AS (
    SELECT 
        Dia,
        Ticket_Medio,
        LAG(Ticket_Medio) OVER (ORDER BY Dia ASC) AS Ticket_Dia_Anterior,
        ROW_NUMBER() OVER (ORDER BY Dia ASC) AS Posicao
    FROM Vendas_Diarias
)
SELECT 
    Dia,
    Ticket_Medio,
    Ticket_Dia_Anterior
FROM Rankeamento
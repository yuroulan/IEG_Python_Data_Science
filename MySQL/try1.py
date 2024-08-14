WITH FirstAttempt AS (
    SELECT 
        order_id, 
        MIN(created_at) AS first_attempt_date
    FROM 
        attempts
    GROUP BY 
        order_id
),
NextDayDeliveries AS (
    SELECT 
        o.id AS order_id,
        o.shipper_name,
        MIN(a.created_at) AS success_date
    FROM 
        orders o
    JOIN 
        attempts a ON o.id = a.order_id
    WHERE 
        a.status = 'Success'
    GROUP BY 
        o.id, o.shipper_name
    HAVING 
        DATEDIFF(MIN(a.created_at), o.created_at) <= 1
)
SELECT 
    o.shipper_name,
    COUNT(o.id) AS total_orders_created,
    ROUND(
        COUNT(nd.order_id) / COUNT(o.id), 4
    ) AS percentage_delivered_by_next_day
FROM 
    orders o
LEFT JOIN 
    NextDayDeliveries nd ON o.id = nd.order_id
GROUP BY 
    o.shipper_name;
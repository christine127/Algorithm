SELECT 
  order_date AS dt,
  dau,
  wau,
  ROUND(DAU/WAU,2) AS stickiness
FROM
  (SELECT 
    order_date, 
    COUNT(DISTINCT customer_id) AS dau,
      (
      SELECT COUNT(DISTINCT customer_id)
      FROM records AS r1
      WHERE 
        r1.order_date 
          BETWEEN DATE_SUB(r.order_date, INTERVAL 6 DAY)
          AND r.order_date
        ) AS wau 
  FROM records AS r
  WHERE MONTH(order_date) = '11'
  GROUP BY order_date
  HAVING DAU > 0 
  ) AS T

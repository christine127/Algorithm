-- SELECT 서브쿼리 (나의 답안)
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

-- LEFT JOIN (강사님)
SELECT 
  dt,
  dau,
  wau,
  ROUND(dau/wau,2) AS stickiness
FROM
  (SELECT 
    d.order_date AS dt,
    COUNT(DISTINCT d.customer_id) AS dau,
    COUNT(DISTINCT w.customer_id) AS wau
  FROM records AS d
    LEFT JOIN records AS w ON w.order_date BETWEEN DATE_ADD(d.order_date, INTERVAL -6 DAY) AND d.order_date
  WHERE d.order_date BETWEEN '2020-11-01' AND '2020-11-30'
  GROUP BY d.order_date) AS T

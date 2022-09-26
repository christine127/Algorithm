-- 클래식 리텐션
WITH
  records_preprocessed AS (
    SELECT
      r.customer_id,
      r.order_id,
      r.order_date,
      c.first_order_date,
      DATE_FORMAT(r.order_date, '%Y-%m-01') as order_month,
      DATE_FORMAT(c.first_order_date, '%Y-%m-01') as first_order_month
    FROM
      records as r
      INNER JOIN customer_stats as c ON r.customer_id = c.customer_id
  )
    SELECT
      first_order_month,
      COUNT(DISTINCT (customer_id)) as month0,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 1 month) = order_month THEN customer_id END) month1,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 2 month) = order_month THEN customer_id END) month2,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 3 month) = order_month THEN customer_id END) month3,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 4 month) = order_month THEN customer_id END) month4,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 5 month) = order_month THEN customer_id END) month5,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 6 month) = order_month THEN customer_id END) month6,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 7 month) = order_month THEN customer_id END) month7,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 8 month) = order_month THEN customer_id END) month8,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 9 month) = order_month THEN customer_id END) month9,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 10 month) = order_month THEN customer_id END) month10,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 11 month) = order_month THEN customer_id END) month11
    FROM
      records_preprocessed
    GROUP BY
      first_order_month

-- 롤링 리텐션(마지막 달까지 유지한 것으로 계산)
WITH customers AS ( 
     SELECT customer_id
          , DATE_FORMAT(first_order_date, '%Y-%m-01') first_order_month
          , DATE_FORMAT(last_order_date, '%Y-%m-01') last_order_month
     FROM customer_stats c
)

SELECT first_order_month
     , COUNT(DISTINCT customer_id) month0
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 1 MONTH) <= last_order_month THEN customer_id END) AS month1
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 2 MONTH) <= last_order_month THEN customer_id END) AS month2
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 3 MONTH) <= last_order_month THEN customer_id END) AS month3
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 4 MONTH) <= last_order_month THEN customer_id END) AS month4
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 5 MONTH) <= last_order_month THEN customer_id END) AS month5
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 6 MONTH) <= last_order_month THEN customer_id END) AS month6
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 7 MONTH) <= last_order_month THEN customer_id END) AS month7
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 8 MONTH) <= last_order_month THEN customer_id END) AS month8
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 9 MONTH) <= last_order_month THEN customer_id END) AS month9
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 10 MONTH) <= last_order_month THEN customer_id END) AS month10
     , COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 11 MONTH) <= last_order_month THEN customer_id END) AS month11
FROM customers
GROUP BY 1

-- 나의 답안  
WITH
  records_preprocessed AS (
    SELECT
      r.customer_id,
      r.order_id,
      r.order_date,
      c.first_order_date,
      DATE_FORMAT(r.order_date, '%Y-%m-01') as order_month,
      DATE_FORMAT(c.first_order_date, '%Y-%m-01') as first_order_month,
      DATE_FORMAT(
        DATE_ADD(c.first_order_date, INTERVAL 1 MONTH),
        '%Y-%m-01'
      ) as second_order_month
    FROM
      records as r
      INNER JOIN customer_stats as c ON r.customer_id = c.customer_id
  )
SELECT first_order_month, month0, month1
FROM
  (
    SELECT
      first_order_month,
      COUNT(DISTINCT (customer_id)) as month0
    FROM
      records_preprocessed
    GROUP BY
      first_order_month
  ) AS T1
  INNER JOIN (
    SELECT
      second_order_month,
      COUNT(DISTINCT (customer_id)) as month1
    FROM
      records_preprocessed
    WHERE
      order_month = second_order_month
    GROUP BY
      second_order_month
  ) AS T2 ON T1.first_order_month = T2.second_order_month
  
  
  
  
  -- 간단한 답안
  WITH
  records_preprocessed AS (
    SELECT
      r.customer_id,
      r.order_id,
      r.order_date,
      c.first_order_date,
      DATE_FORMAT(r.order_date, '%Y-%m-01') as order_month,
      DATE_FORMAT(c.first_order_date, '%Y-%m-01') as first_order_month,
      DATE_FORMAT(
        DATE_ADD(c.first_order_date, INTERVAL 1 MONTH),
        '%Y-%m-01'
      ) as second_order_month
    FROM
      records as r
      INNER JOIN customer_stats as c ON r.customer_id = c.customer_id
  )
    SELECT
      first_order_month,
      COUNT(DISTINCT (customer_id)) as month0,
      COUNT(DISTINCT CASE WHEN DATE_ADD(first_order_month, INTERVAL 1 month) = order_month THEN customer_id END) month1
    FROM
      records_preprocessed
    GROUP BY
      first_order_month


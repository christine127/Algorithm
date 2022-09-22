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

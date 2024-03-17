-- order_summary.sql

-- Create or replace the order_summary view
-- CREATE OR REPLACE VIEW order_summary AS
WITH temp_view AS (
  SELECT
    o.order_id,
    c.customer_name,
    p.product_name,
    o.order_date,
    o.total_amount,
    py.payment_date,
    py.payment_amount
  FROM
    {{ source('source', 'order_table') }} o
    JOIN {{ source('source', 'customer') }} c ON o.customer_id = c.customer_id
    JOIN {{ source('source', 'product') }} p ON o.product_id = p.product_id
    JOIN {{ source('source', 'payment') }} py ON py.order_id = o.order_id
)

SELECT *
FROM temp_view
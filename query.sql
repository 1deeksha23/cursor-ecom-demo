-- query.sql
-- Show top orders by order_total with customer info
SELECT
  o.order_id,
  o.order_date,
  c.customer_id,
  c.name AS customer_name,
  c.email,
  o.shipping_city,
  ROUND(SUM(oi.quantity * oi.unit_price), 2) AS order_total,
  COUNT(oi.order_item_id) AS items_in_order
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.order_id
ORDER BY order_total DESC
LIMIT 50;
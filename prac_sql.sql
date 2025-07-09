mysql> SELECT
    ->   s.customer_id,
    ->   SUM(m.price) AS total_spent
    -> FROM sales s
    -> JOIN menu m ON s.product_id = m.product_id
    -> GROUP BY s.customer_id;

mysql> SELECT
    ->   customer_id,
    ->   COUNT(DISTINCT order_date) AS visit_days
    -> FROM sales
    -> GROUP BY customer_id;

mysql> SELECT customer_id, product_name
    -> FROM sales
    -> JOIN menu ON sales.product_id = menu.product_id
    -> WHERE (customer_id, order_date) IN (
    ->   SELECT customer_id, MIN(order_date)
    ->   FROM sales
    ->   GROUP BY customer_id
    -> );


mysql> SELECT
    ->   m.product_name,
    ->   COUNT(*) AS total_orders
    -> FROM sales s
    -> JOIN menu m ON s.product_id = m.product_id
    -> GROUP BY m.product_name
    -> ORDER BY total_orders DESC
    -> LIMIT 1;

mysql> -- Step 1: Count how many times each customer ordered each item
mysql> SELECT customer_id, product_name
    -> FROM (
    ->   SELECT
    ->     s.customer_id,
    ->     m.product_name,
    ->     COUNT(*) AS item_count
    ->   FROM sales s
    ->   JOIN menu m ON s.product_id = m.product_id
    ->   GROUP BY s.customer_id, m.product_name
    -> ) AS item_summary
    ->
    -> -- Step 2: Filter to keep only the item(s) with the highest count per customer
    -> WHERE (customer_id, item_count) IN (
    ->   SELECT
    ->     customer_id,
    ->     MAX(item_count)
    ->   FROM (
    ->     SELECT
    ->       s.customer_id,
    ->       m.product_name,
    ->       COUNT(*) AS item_count
    ->     FROM sales s
    ->     JOIN menu m ON s.product_id = m.product_id
    ->     GROUP BY s.customer_id, m.product_name
    ->   ) AS counts
    ->   GROUP BY customer_id
    -> );


mysql> SELECT s.customer_id, m.product_name, s.order_date
    -> FROM sales s
    -> JOIN menu m ON s.product_id = m.product_id
    -> JOIN members mem ON s.customer_id = mem.customer_id
    -> WHERE s.order_date = (
    ->   SELECT MIN(order_date)
    ->   FROM sales
    ->   WHERE customer_id = s.customer_id AND order_date >= mem.join_date
    -> );


mysql> SELECT s.customer_id, m.product_name, s.order_date
    -> FROM sales s
    -> JOIN menu m ON s.product_id = m.product_id
    -> JOIN members mem ON s.customer_id = mem.customer_id
    -> WHERE s.order_date = (
    ->   SELECT MAX(order_date)
    ->   FROM sales
    ->   WHERE customer_id = s.customer_id AND order_date < mem.join_date
    -> );

mysql> SELECT
    ->   s.customer_id,
    ->   COUNT(*) AS total_items,
    ->   SUM(m.price) AS total_amount
    -> FROM sales s
    -> JOIN menu m ON s.product_id = m.product_id
    -> JOIN members mem ON s.customer_id = mem.customer_id
    -> WHERE s.order_date < mem.join_date
    -> GROUP BY s.customer_id;

mysql> SELECT
    ->   s.customer_id,
    ->   SUM(
    ->     CASE
    ->       WHEN m.product_name = 'sushi' THEN m.price * 20
    ->       ELSE m.price * 10
    ->     END
    ->   ) AS total_points
    -> FROM sales s
    -> JOIN menu m ON s.product_id = m.product_id
    -> GROUP BY s.customer_id;
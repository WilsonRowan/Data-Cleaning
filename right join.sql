SELECT a.customer_id, a.city, o.restaurant_id, o.order_id, o.order_time, o.delivery_time, o.status
FROM customers AS a
RIGHT JOIN orders AS o
ON a.customer_id = o.customer_id;

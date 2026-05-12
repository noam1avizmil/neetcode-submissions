-- Write your query below
select * from customers 
where customer_id in (select customer_id from orders group by customer_id
HAVING COUNT(*) FILTER (WHERE product_name = 'A') > 0
     AND COUNT(*) FILTER (WHERE product_name = 'B') > 0
     AND COUNT(*) FILTER (WHERE product_name = 'C') = 0)
order by customer_name
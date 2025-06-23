# Find dates where temperature is higher than the previous day
SELECT w1.Id
FROM Weather w1
JOIN Weather w2 ON DATEDIFF(w1.RecordDate, w2.RecordDate) = 1
WHERE w1.Temperature > w2.Temperature;

# Find each player's first login date
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;

# Find the second highest salary
SELECT MAX(Salary) AS SecondHighestSalary
FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);

# Find the user with the highest number of ratings
SELECT name
FROM Users u
JOIN (
  SELECT user_id, COUNT(*) AS rating_count
  FROM MovieRating
  GROUP BY user_id
  ORDER BY rating_count DESC, user_id ASC
  LIMIT 1
) r ON u.user_id = r.user_id;

# Find the movie with the highest average rating in Feb 2020
SELECT title
FROM Movies m
JOIN (
  SELECT movie_id, AVG(rating) AS avg_rating
  FROM MovieRating
  WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
  GROUP BY movie_id
  ORDER BY avg_rating DESC, movie_id ASC
  LIMIT 1
) t ON m.movie_id = t.movie_id;

# Find employees who earn more than their managers
SELECT e.name
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;

# Delete duplicate emails keeping only the smallest id
DELETE e1
FROM Person e1
JOIN Person e2
ON e1.email = e2.email AND e1.id > e2.id;

# Find dates with 3 or more consecutive days of 100+ people in stadium
SELECT id, visit_date, people
FROM (
  SELECT id, visit_date, people,
         LEAD(people, 1) OVER (ORDER BY visit_date) AS p1,
         LAG(people, 1) OVER (ORDER BY visit_date) AS p2
  FROM Stadium
) s
WHERE (people >= 100 AND p1 >= 100 AND p2 >= 100)
   OR (people >= 100 AND p1 >= 100)
   OR (people >= 100 AND p2 >= 100);

# Find customers who bought all products
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);

# Top 5 customers based on total spending
SELECT c.customer_id, c.customer_name, SUM(o.total_amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
ORDER BY total_spent DESC
LIMIT 5;

# Number of orders handled by each employee
SELECT e.employee_id, e.employee_name, COUNT(o.order_id) AS orders_handled
FROM Employees e
JOIN Orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.employee_name
ORDER BY orders_handled DESC;

# Highest revenue-generating product per category
SELECT c.category_name, p.product_name, SUM(od.quantity * od.unit_price) AS revenue
FROM OrderDetails od
JOIN Products p ON od.product_id = p.product_id
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name, p.product_id, p.product_name
HAVING SUM(od.quantity * od.unit_price) = (
    SELECT MAX(total_revenue)
    FROM (
        SELECT p2.category_id, p2.product_id, SUM(od2.quantity * od2.unit_price) AS total_revenue
        FROM OrderDetails od2
        JOIN Products p2 ON od2.product_id = p2.product_id
        GROUP BY p2.category_id, p2.product_id
        HAVING p2.category_id = c.category_id
    ) sub
);

# Average delivery time (in days) per shipper
SELECT s.shipper_id, s.shipper_name, AVG(DATEDIFF(o.shipped_date, o.order_date)) AS avg_delivery_days
FROM Orders o
JOIN Shippers s ON o.shipper_id = s.shipper_id
WHERE o.shipped_date IS NOT NULL AND o.order_date IS NOT NULL
GROUP BY s.shipper_id, s.shipper_name;

# Employees earning more than department average
SELECT e.emp_id, e.emp_name, e.salary, e.dept_id
FROM employees e
JOIN (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
) d_avg ON e.dept_id = d_avg.dept_id
WHERE e.salary > d_avg.avg_salary;

# Employees who worked on all projects in their department
SELECT e.emp_id, e.emp_name
FROM employees e
WHERE NOT EXISTS (
    SELECT 1
    FROM projects p
    JOIN employees ep ON p.emp_id = ep.emp_id
    WHERE ep.dept_id = e.dept_id
    AND NOT EXISTS (
        SELECT 1
        FROM projects p2
        WHERE p2.project_id = p.project_id AND p2.emp_id = e.emp_id
    )
);

# Highest-paid employee (after 2020) per department
SELECT dept_id, emp_id, emp_name, salary
FROM (
    SELECT *, 
           RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
    WHERE hire_date > '2020-01-01'
) ranked
WHERE rnk = 1;

# Departments where all employees earn more than 55000
SELECT d.dept_id, d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1
    FROM employees e
    WHERE e.dept_id = d.dept_id AND e.salary <= 55000
);

# Customers spending more than their regional average
SELECT c.customer_id, c.customer_name, c.region, SUM(o.total_amount) AS customer_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.region
HAVING SUM(o.total_amount) > (
    SELECT AVG(o2.total_amount)
    FROM orders o2
    JOIN customers c2 ON o2.customer_id = c2.customer_id
    WHERE c2.region = c.region
);

# Orders that include products from all categories
SELECT o.order_id
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
GROUP BY o.order_id
HAVING COUNT(DISTINCT p.category) = (
    SELECT COUNT(DISTINCT category) FROM products
);

# Most expensive product per customer after 2023
SELECT customer_id, product_id, product_name, max_price
FROM (
    SELECT o.customer_id, p.product_id, p.product_name,
           (od.unit_price * od.quantity) AS max_price,
           RANK() OVER (PARTITION BY o.customer_id ORDER BY od.unit_price * od.quantity DESC) AS rnk
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    JOIN products p ON od.product_id = p.product_id
    WHERE o.order_date > '2023-01-01'
) sub
WHERE rnk = 1;

# Regions with no customers who ordered product ID 202
SELECT DISTINCT c.region
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    JOIN order_details od ON o.order_id = od.order_id
    WHERE o.customer_id = c.customer_id AND od.product_id = 202
);

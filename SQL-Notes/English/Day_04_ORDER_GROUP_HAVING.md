# 🗄️ Day 4 — ORDER BY, ALIASES, GROUP BY & HAVING

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [IS NULL / IS NOT NULL](#null)
2. [ORDER BY](#order-by)
3. [ALIASES (AS)](#aliases)
4. [GROUP BY](#group-by)
5. [Aggregate Functions](#aggregate)
6. [HAVING](#having)
7. [Practice Exercises](#exercises)

---

## 🔲 IS NULL / IS NOT NULL {#null}

`IS NULL` → Selects rows where data has not been entered
`IS NOT NULL` → Selects rows where data is not empty

```sql
CREATE TABLE customers_products
(
  product_id number(10),
  customer_name varchar2(50),
  product_name varchar2(50)
);

INSERT INTO customers_products VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_products VALUES (20, 'John', 'Apple');
INSERT INTO customers_products VALUES (30, 'Amy', 'Palm');
INSERT INTO customers_products(product_id, product_name) VALUES(30, 'Apricot');
-- ↑ customer_name not entered, will be NULL

-- Get rows where customer name is not entered
SELECT *
FROM customers_products
WHERE customer_name IS NULL;

-- Get rows where customer name is NOT empty
SELECT *
FROM customers_products
WHERE customer_name IS NOT NULL;

-- Use IS NULL with UPDATE
UPDATE customers_products
SET customer_name = 'Name not entered'
WHERE customer_name IS NULL;

-- Update product_name where customer_name is NULL
UPDATE customers_products
SET product_name = 'Watermelon'
WHERE customer_name IS NULL;
```

---

## ↕️ ORDER BY {#order-by}

`ORDER BY` sorts data by a specific field.

```sql
-- Sort by product_name (natural order A-Z, default is ASC)
SELECT *
FROM customers_products
ORDER BY product_name;

-- Sort records where customer_name is 'Mark' by product_id
SELECT *
FROM customers_products
WHERE customer_name = 'Mark'
ORDER BY product_id;

-- Field number can also be used (1st column = product_id)
SELECT *
FROM customers_products
WHERE customer_name = 'Mark'
ORDER BY 1;

-- Descending order (largest to smallest)
SELECT *
FROM customers_products
ORDER BY product_id DESC;

-- Multiple sort: product_name descending, customer_name ascending
SELECT *
FROM customers_products
ORDER BY product_name DESC, customer_name ASC;
```

> **Note:** Default sort is `ASC` (ascending). `ORDER BY product_name` = `ORDER BY product_name ASC`

---

## 🏷️ ALIASES (AS) {#aliases}

`AS` is used to display column names differently. **Real column names in the database do NOT change** — you only get a report with new column names.

```sql
-- Rename columns
SELECT product_id AS product_code,
       customer_name AS customer_name_alias,
       product_name AS product_name_alias
FROM customers_products;

-- Combine two columns into one with alias
SELECT customer_name AS customer_name,
       product_id || product_name AS product_code_name
FROM customers_products;
```

---

## 📊 GROUP BY {#group-by}

`GROUP BY` groups data by a specific field.

```sql
CREATE TABLE employees
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  salary number(20),
  company varchar2(20)
);

INSERT INTO employees VALUES(123456789, 'John Walker', 'Florida', 2500, 'IBM');
INSERT INTO employees VALUES(234567890, 'Brad Pitt', 'Florida', 1500, 'APPLE');
INSERT INTO employees VALUES(345678901, 'Eddie Murphy', 'Texas', 3000, 'IBM');
INSERT INTO employees VALUES(456789012, 'Eddie Murphy', 'Virginia', 1000, 'GOOGLE');
INSERT INTO employees VALUES(567890123, 'Eddie Murphy', 'Texas', 7000, 'MICROSOFT');
INSERT INTO employees VALUES(456789012, 'Brad Pitt', 'Texas', 1500, 'GOOGLE');
INSERT INTO employees VALUES(123456710, 'Mark Stone', 'Pennsylvania', 2500, 'IBM');

-- Number of customers per product
SELECT product_name, COUNT(product_name) AS number_of_customers
FROM customers_products
GROUP BY product_name;

-- How many times each product_id is used
SELECT product_id, COUNT(product_id) AS number_of_usage
FROM customers_products
GROUP BY product_id;

-- Total salary per employee
SELECT name, SUM(salary) AS total_salary
FROM employees
GROUP BY name;

-- Number of employees per state
SELECT state, COUNT(name) AS total_worker
FROM employees
GROUP BY state;

-- Number of employees with salary > 2000 per company
SELECT company, COUNT(name) AS number_of_employees
FROM employees
WHERE salary > 2000
GROUP BY company;

-- Min and max salary per company
SELECT company, MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employees
GROUP BY company;
```

---

## 🔢 Aggregate Functions {#aggregate}

| Function | Description |
|----------|-------------|
| `COUNT()` | Returns number of records |
| `SUM()` | Returns total value |
| `AVG()` | Returns average value |
| `MIN()` | Returns minimum value |
| `MAX()` | Returns maximum value |

```sql
-- Highest salary
SELECT MAX(salary) AS max_salary FROM employees;

-- Lowest salary
SELECT MIN(salary) AS min_salary FROM employees;

-- Employee with highest salary (SUBQUERY)
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Employee with lowest salary
SELECT *
FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees);

-- Second highest salary
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Second lowest salary
SELECT MIN(salary)
FROM employees
WHERE salary > (SELECT MIN(salary) FROM employees);
```

---

## 🔒 HAVING {#having}

`HAVING` is used to filter groups after `GROUP BY` using aggregate functions.

> **Note:** `WHERE` filters rows. `HAVING` filters groups.

```sql
-- Show companies where min salary > 2000
SELECT company, MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employees
GROUP BY company
HAVING MIN(salary) > 2000;

-- Show employees whose total income > 2500
SELECT name, SUM(salary) AS total_income
FROM employees
GROUP BY name
HAVING SUM(salary) > 2500;

-- Show states with more than 1 employee
SELECT state, COUNT(name) AS number_of_employees
FROM employees
GROUP BY state
HAVING COUNT(name) > 1;

-- Show states where max salary < 3000
SELECT state, MAX(salary) AS max_salary
FROM employees
GROUP BY state
HAVING MAX(salary) < 3000;
```

### WHERE vs HAVING

```sql
-- WHERE: filters BEFORE GROUP BY
SELECT company, COUNT(name) AS number_of_employees
FROM employees
WHERE salary > 2000       -- ← filter first: only salary > 2000
GROUP BY company;

-- HAVING: filters AFTER GROUP BY
SELECT company, COUNT(name) AS number_of_employees
FROM employees
GROUP BY company
HAVING COUNT(name) > 1;   -- ← then filter: employee count > 1
```

---

## 🏋️ Practice Exercises {#exercises}

```sql
CREATE TABLE employees
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  salary number(20),
  company varchar2(20)
);
-- (Insert same 7 rows as above)
```

**Questions:**

1. Sort all employees by salary from highest to lowest
2. Get names of employees at IBM and GOOGLE, alias the `name` column as `employee_name`
3. Calculate total salary per employee
4. Calculate average salary per state
5. List companies with average salary greater than 2000
6. Get the count of employees at IBM
7. Get all information of the highest-paid employee (use SUBQUERY)
8. Get the second highest salary

```sql
-- Solutions:
-- 1) SELECT * FROM employees ORDER BY salary DESC;

-- 2)
SELECT name AS employee_name
FROM employees
WHERE company IN ('IBM', 'GOOGLE');

-- 3)
SELECT name, SUM(salary) AS total_salary
FROM employees
GROUP BY name;

-- 4)
SELECT state, AVG(salary) AS avg_salary
FROM employees
GROUP BY state;

-- 5)
SELECT company, AVG(salary) AS avg_salary
FROM employees
GROUP BY company
HAVING AVG(salary) > 2000;

-- 6)
SELECT COUNT(name) AS ibm_employees
FROM employees
WHERE company = 'IBM';

-- 7)
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 8)
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

---

*📌 Next lesson: UNION, INTERSECT, MINUS, JOINS*

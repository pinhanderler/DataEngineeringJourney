# 🗄️ Day 7 — PIVOT, DISTINCT & ALTER TABLE

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [PIVOT](#pivot)
2. [DISTINCT](#distinct)
3. [ALTER TABLE](#alter-table)
4. [Practice Exercises](#exercises)

---

## 🔄 PIVOT {#pivot}

`PIVOT` converts rows into columns.

```sql
CREATE TABLE customers_products
(
  product_id number(10),
  customer_name varchar2(50),
  product_name varchar2(50)
);

INSERT INTO customers_products VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_products VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_products VALUES (20, 'John', 'Apple');
INSERT INTO customers_products VALUES (30, 'Amy', 'Palm');
INSERT INTO customers_products VALUES (20, 'Mark', 'Apple');
INSERT INTO customers_products VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');
INSERT INTO customers_products VALUES (20, 'Eddie', 'Apple');

-- Show how many of each product each customer bought
SELECT * FROM (SELECT customer_name, product_name FROM customers_products)
PIVOT
(COUNT(product_name) FOR product_name IN ('Orange', 'Apple', 'Palm', 'Apricot'));

-- Show how many products each customer bought
SELECT * FROM (SELECT customer_name, product_name FROM customers_products)
PIVOT
(COUNT(customer_name) FOR customer_name IN ('Mark', 'Amy', 'Adem', 'John'));

-- Total product_id by product name
SELECT * FROM (SELECT product_id, product_name FROM customers_products)
PIVOT
(SUM(product_id) FOR product_id IN (10, 20, 30, 40));

-- Count of product_id by product name
SELECT * FROM (SELECT product_id, product_name FROM customers_products)
PIVOT
(COUNT(product_id) FOR product_id IN (10, 20, 30, 40));
```

---

## 🔵 DISTINCT {#distinct}

`DISTINCT` filters out duplicate records, showing only unique values.

```sql
-- Unique product names (no duplicates)
SELECT DISTINCT product_name
FROM customers_products;

-- How many different products are there?
SELECT COUNT(DISTINCT product_name) AS number_of_different_products
FROM customers_products;
```

---

## 🔧 ALTER TABLE {#alter-table}

`ALTER TABLE` is used to modify the structure of an existing table.

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
```

### 1) Add a New Column

```sql
-- Add single column
ALTER TABLE employees
ADD gender varchar2(20);

-- Add column with DEFAULT value
-- DEFAULT means automatically filled — e.g. 'The USA' is set for all existing rows
ALTER TABLE employees
ADD country varchar2(50) DEFAULT 'The USA';

-- Add multiple columns at once
ALTER TABLE employees
ADD (number_of_kid number(2),
     marital_status varchar2(30) DEFAULT 'single'
    );
```

### 2) Drop (Delete) a Column

```sql
ALTER TABLE employees
DROP COLUMN country;
```

### 3) Rename a Column

```sql
ALTER TABLE employees
RENAME COLUMN gender TO gender_male_or_female;
```

### 4) Rename the Table

```sql
ALTER TABLE employees
RENAME TO workers;

SELECT * FROM workers;  -- Now accessed as workers
```

### 5) Modify Column Structure

```sql
-- Single column
ALTER TABLE workers
MODIFY id number(9) NOT NULL;

-- Multiple columns at once
ALTER TABLE workers
MODIFY (state char(45) NOT NULL,
        company char(30)
       );
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

1. How many different states are there? (use DISTINCT)
2. Show unique company names
3. Add an `email varchar2(100)` column to employees table
4. Add a `hire_date date DEFAULT SYSDATE` column
5. Drop the `email` column
6. Rename the table to `staff`
7. Make the `id` column NOT NULL

```sql
-- Solutions:

-- 1)
SELECT COUNT(DISTINCT state) AS different_states FROM employees;

-- 2)
SELECT DISTINCT company FROM employees;

-- 3)
ALTER TABLE employees ADD email varchar2(100);

-- 4)
ALTER TABLE employees ADD hire_date date DEFAULT SYSDATE;

-- 5)
ALTER TABLE employees DROP COLUMN email;

-- 6)
ALTER TABLE employees RENAME TO staff;

-- 7)
ALTER TABLE staff MODIFY id number(9) NOT NULL;
```

---

*📌 Next lesson: ROWNUM, OFFSET FETCH, MOD, Advanced Queries*

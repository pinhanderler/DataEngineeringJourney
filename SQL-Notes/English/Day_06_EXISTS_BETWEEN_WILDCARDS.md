# 🗄️ Day 6 — EXISTS, BETWEEN & Wildcards

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [EXISTS Command](#exists)
2. [BETWEEN](#between)
3. [NOT BETWEEN](#not-between)
4. [Wildcards (%, _, [ ])](#wildcards)
5. [NOT LIKE](#not-like)
6. [REGEXP_LIKE](#regexp)
7. [Practice Exercises](#exercises)

---

## ✅ EXISTS Command {#exists}

`EXISTS` is used **together with SUBQUERIES**. It checks whether a subquery returns any results.

> **Important Notes:**
> - `IN` command is basically a written form of multiple `OR` conditions
> - We don't use `IN` alone with subqueries
> - When using a subquery, use `EXISTS`

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
INSERT INTO customers_products VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');
INSERT INTO customers_products VALUES (20, 'Eddie', 'Apple');

CREATE TABLE customers_likes
(
  product_id number(10),
  customer_name varchar2(50),
  liked_product varchar2(50)
);

INSERT INTO customers_likes VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_likes VALUES (50, 'Mark', 'Pineapple');
INSERT INTO customers_likes VALUES (60, 'John', 'Avocado');
INSERT INTO customers_likes VALUES (30, 'Lary', 'Cherries');
INSERT INTO customers_likes VALUES (20, 'Mark', 'Apple');
INSERT INTO customers_likes VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_likes VALUES (40, 'John', 'Apricot');
INSERT INTO customers_likes VALUES (20, 'Eddie', 'Apple');

-- Show names of customers whose product_ids match
SELECT customer_name
FROM customers_products
WHERE EXISTS (SELECT product_id
              FROM customers_likes
              WHERE customers_products.product_id = customers_likes.product_id);

-- Show names of customers whose product_name matches liked_product
SELECT customer_name
FROM customers_products
WHERE EXISTS (SELECT liked_product
              FROM customers_likes
              WHERE customers_products.product_name = customers_likes.liked_product);
```

---

## ↔️ BETWEEN {#between}

`BETWEEN` retrieves data within a range. **Boundaries are inclusive.**

```sql
-- Products with product_id between 20 and 40
SELECT product_name, product_id
FROM customers_products
WHERE product_id BETWEEN 20 AND 40;

-- Same query using AND:
SELECT product_name, product_id
FROM customers_products
WHERE product_id >= 20 AND product_id <= 40;

-- BETWEEN with letters (names starting J through T)
SELECT *
FROM customers_products
WHERE customer_name BETWEEN 'J' AND 'T';
```

> ⚠️ **When using BETWEEN, make sure the first value is smaller than the second!**

---

## ❌ NOT BETWEEN {#not-between}

With `NOT BETWEEN`, the **boundaries are NOT included**.

```sql
-- Products with product_id NOT between 20 and 40
SELECT *
FROM customers_products
WHERE product_id NOT BETWEEN 20 AND 40;

-- Same query using AND/OR:
SELECT *
FROM customers_products
WHERE product_id < 20 OR product_id > 40;

-- Products whose name first letter is NOT between M and S
SELECT *
FROM customers_products
WHERE product_name NOT BETWEEN 'M' AND 'S';
```

---

## 🃏 Wildcards {#wildcards}

### 1) `%` — Zero or more characters

```sql
CREATE TABLE customers
(
  customer_id number(10) UNIQUE,
  customer_name varchar2(50) NOT NULL,
  income number(6)
);

INSERT INTO customers VALUES (1001, 'John', 62000);
INSERT INTO customers VALUES (1002, 'Jane', 57500);
INSERT INTO customers VALUES (1003, 'Brad', 71000);
INSERT INTO customers VALUES (1004, 'Manse', 42000);
INSERT INTO customers VALUES (1005, 'Can', 57500);
INSERT INTO customers VALUES (1006, 'Cin', 71000);
INSERT INTO customers VALUES (1007, 'Con', 42000);

-- Names starting with J
SELECT * FROM customers WHERE customer_name LIKE 'J%';

-- Names ending with e
SELECT customer_name, income FROM customers WHERE customer_name LIKE '%e';

-- Names containing n
SELECT customer_name, income FROM customers WHERE customer_name LIKE '%n%';
```

### 2) `_` — Exactly 1 character

```sql
-- 4-letter names ending in 'ohn' → John
SELECT customer_name, income FROM customers WHERE customer_name LIKE '_ohn';

-- 4-letter names ending in 'ne' → Jane
SELECT customer_name, income FROM customers WHERE customer_name LIKE '__ne';

-- 4-letter names with 3rd letter 'n'
SELECT customer_name, income FROM customers WHERE customer_name LIKE '__n_';

-- Names with 2nd letter 'a'
SELECT customer_name, income FROM customers WHERE customer_name LIKE '_a%';

-- Names with 3rd letter 'n', at least 5 letters long
SELECT customer_name, income FROM customers WHERE customer_name LIKE '__n__%';

-- Names starting with B, 3rd letter is a → Brad
SELECT customer_name, income FROM customers WHERE customer_name LIKE 'B_a%';
```

---

## 🔬 REGEXP_LIKE {#regexp}

For more advanced pattern matching using character classes `[ ]`:

```sql
-- First letter C, last letter n, 2nd letter a or i → Can, Cin
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, 'C[ai]n');

-- First letter C, last letter n, 2nd letter from a to k → Can, Cin
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, 'C[a-k]n');

-- Names containing a or n
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, '[an](*)');

-- Names starting with J or M
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, '^[JM](*)');
```

---

## 🚫 NOT LIKE {#not-like}

```sql
-- Names NOT starting with J
SELECT customer_name, income FROM customers WHERE customer_name NOT LIKE 'J%';

-- Names NOT containing a
SELECT customer_name, income FROM customers WHERE customer_name NOT LIKE '%a%';

-- Names where 2nd letter is NOT a
SELECT customer_name, income FROM customers WHERE customer_name NOT LIKE '_a%';
```

---

## 🏋️ Practice Exercises {#exercises}

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
INSERT INTO customers_products VALUES (20, 'Mark', 'Apple');
INSERT INTO customers_products VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');
INSERT INTO customers_products VALUES (20, 'Eddie', 'Apple');
```

**Questions:**

1. Get products with product_id between 10 and 30 (use BETWEEN)
2. Get all info for products with product_id NOT between 10 and 30 (use NOT BETWEEN)
3. Get customers whose name starts with 'M'
4. Get products whose name starts with 'A' and ends with 'e'
5. Get customers with exactly 4-letter names
6. Get customers whose name contains 'hn'

```sql
-- Solutions:

-- 1)
SELECT product_name, product_id
FROM customers_products
WHERE product_id BETWEEN 10 AND 30;

-- 2)
SELECT *
FROM customers_products
WHERE product_id NOT BETWEEN 10 AND 30;

-- 3)
SELECT * FROM customers_products WHERE customer_name LIKE 'M%';

-- 4)
SELECT * FROM customers_products WHERE product_name LIKE 'A%e';

-- 5)
SELECT * FROM customers_products WHERE customer_name LIKE '____';

-- 6)
SELECT * FROM customers_products WHERE customer_name LIKE '%hn%';
```

---

*📌 Next lesson: PIVOT, DISTINCT, ALTER TABLE*

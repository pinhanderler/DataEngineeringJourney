# 🗄️ Day 3 — UPDATE SET, DELETE, TRUNCATE, DROP & SELECT

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [UPDATE SET](#update-set)
2. [DELETE FROM](#delete-from)
3. [TRUNCATE TABLE](#truncate)
4. [DROP TABLE](#drop)
5. [SELECT Statement](#select)
6. [WHERE Filter](#where)
7. [IN Condition](#in)
8. [SUBQUERY](#subquery)
9. [Practice Exercises](#exercises)

---

## ✏️ UPDATE SET {#update-set}

`UPDATE SET` is used to update existing records in a table.

```sql
CREATE TABLE supplier
(
  supplier_id number(10),
  supplier_name varchar2(50),
  contact_name varchar2(50),
  CONSTRAINT supplier_pk PRIMARY KEY (supplier_id, supplier_name)
);

INSERT INTO supplier VALUES(1, 'IBM', 'John Walker');
INSERT INTO supplier VALUES(2, 'APPLE', 'Steve Max');
INSERT INTO supplier VALUES(3, 'SAMSUNG', 'Tae Shaun');

-- Update single record
UPDATE supplier
SET supplier_name = 'LINUX',
    contact_name = 'Alex Leo'
WHERE supplier_id = 1;

-- Update multiple records
UPDATE supplier
SET supplier_name = 'LG',
    contact_name = 'El Ci'
WHERE supplier_id < 3;
```

### Update Using a Subquery

```sql
CREATE TABLE products
(
  supplier_id number(10),
  product_id number(10),
  product_name varchar2(50),
  customer_name varchar2(50),
  CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);

INSERT INTO products VALUES(1, 11, 'Laptop', 'John Walker');
INSERT INTO products VALUES(2, 22, 'Ipad', 'Eddie Murphy');
INSERT INTO products VALUES(3, 33, 'Galaxy 10', 'Adam Eve');

UPDATE supplier
SET supplier_name = (SELECT product_name
                     FROM products
                     WHERE supplier.contact_name = products.customer_name)
WHERE supplier_id < 3;
```

> **Note:** Updates supplier_name with product_name when contact_name matches customer_name.

---

## 🗑️ DELETE FROM {#delete-from}

`DELETE FROM` removes records but does NOT delete the table structure.

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  last_modification date
);

INSERT INTO students VALUES(123456789, 'John Walker', 'Texas', '14-Apr-2020');
INSERT INTO students VALUES(234567890, 'Eddie Murphy', 'Florida', '15-Apr-2020');
INSERT INTO students VALUES(345678901, 'Adam Eve', 'New York', '16-Apr-2020');

-- Delete ALL records (table structure remains → Empty Table)
DELETE FROM students;

-- Delete a specific record
DELETE FROM students WHERE name = 'John Walker';

-- Delete with multiple conditions
DELETE FROM students WHERE name = 'John Walker' OR state = 'New York';
```

---

## ✂️ TRUNCATE TABLE {#truncate}

`TRUNCATE` is a fast way to clear all records. Cannot be rolled back.

```sql
TRUNCATE TABLE customers;
-- equivalent to: DELETE FROM customers;
```

| Feature | DELETE FROM | TRUNCATE TABLE |
|---------|-------------|----------------|
| Rollback | ✅ Possible | ❌ Not possible |
| WHERE clause | ✅ Supported | ❌ Not supported |
| Speed | Slower | Faster |

---

## 💣 DROP TABLE {#drop}

`DROP` deletes the **entire table including its structure**.

```sql
-- Moves to recycle bin (can be recovered)
DROP TABLE students;

-- Permanently deletes (cannot be recovered)
DROP TABLE students PURGE;
```

| Command | Result |
|---------|--------|
| `DELETE FROM` | Records deleted, table remains |
| `TRUNCATE` | All records deleted, table remains, no rollback |
| `DROP TABLE` | Table + contents go to recycle bin |
| `DROP TABLE PURGE` | Table + contents permanently gone |

---

## 🔍 SELECT Statement {#select}

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  gpa number(2,1)
);

INSERT INTO students VALUES(123456789, 'John Walker', 'Texas', 2.8);
INSERT INTO students VALUES(234567890, 'Eddie Murphy', 'Florida', 3.2);
INSERT INTO students VALUES(345678901, 'Adam Eve', 'New York', 3.5);
INSERT INTO students VALUES(456789012, 'Alex Tien', 'New York', 3.8);
INSERT INTO students VALUES(567890123, 'Chris Matala', 'Virginia', 4);

-- Get all data
SELECT * FROM students;

-- Get all data where GPA > 3.2
SELECT *
FROM students
WHERE gpa > 3.2;

-- Get specific columns
SELECT name, id
FROM students
WHERE state = 'New York' AND gpa = 3.5;
```

---

## 🔎 WHERE Filter {#where}

| Operator | Meaning |
|----------|---------|
| `=` | Equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `<>` | Not equal |
| `AND` | Both conditions true |
| `OR` | At least one condition true |

```sql
-- GPA is 2.8 OR state is Florida
SELECT name FROM students WHERE gpa = 2.8 OR state = 'Florida';

-- State is New York AND GPA is 3.5
SELECT name, id FROM students WHERE state = 'New York' AND gpa = 3.5;
```

---

## 📋 IN Condition {#in}

`IN` reduces the need for multiple OR conditions.

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
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');
INSERT INTO customers_products VALUES (20, 'Eddie', 'Apple');

-- Without IN (longer):
SELECT * FROM customers_products
WHERE product_name = 'Orange' OR product_name = 'Apple' OR product_name = 'Apricot';

-- With IN (shorter, same result):
SELECT * FROM customers_products
WHERE product_name IN ('Orange', 'Apple', 'Apricot');
```

---

## 🔄 SUBQUERY {#subquery}

A **subquery** is a query nested inside another query.

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

CREATE TABLE companies
(
  company_id number(9),
  company varchar2(20),
  number_of_employees number(20)
);

INSERT INTO companies VALUES(100, 'IBM', 12000);
INSERT INTO companies VALUES(101, 'GOOGLE', 18000);
INSERT INTO companies VALUES(102, 'MICROSOFT', 10000);
INSERT INTO companies VALUES(100, 'APPLE', 21000);

-- Find employees whose company has more than 15000 employees
SELECT name, company
FROM employees
WHERE company IN (SELECT company
                  FROM companies
                  WHERE number_of_employees > 15000);

-- Subquery in SELECT clause: company employees count + average salary
SELECT company, number_of_employees,
       (SELECT AVG(salary)
        FROM employees
        WHERE companies.company = employees.company) Average_Salary_Per_Company
FROM companies;
```

---

## 🏋️ Practice Exercises {#exercises}

### Exercise 1

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  gpa number(2,1)
);
-- (Insert same 5 rows as above)
```

1. Get all students whose GPA > 3.1 OR state is "Texas"
2. Get student names whose GPA < 3.5 AND state is "Florida"
3. Get names and IDs where GPA is between 2.8 and 3.5
4. Get all where state is "New York" AND GPA > 3.3 AND GPA < 3.7
5. Get all where state is "New York" AND (GPA > 3.7 OR GPA < 3.3)

```sql
-- Solutions:
-- 1) SELECT * FROM students WHERE gpa > 3.1 OR state = 'Texas';
-- 2) SELECT name FROM students WHERE gpa < 3.5 AND state = 'Florida';
-- 3) SELECT name, id FROM students WHERE gpa BETWEEN 2.8 AND 3.5;
-- 4) SELECT * FROM students WHERE state = 'New York' AND gpa > 3.3 AND gpa < 3.7;
-- 5) SELECT * FROM students WHERE state = 'New York' AND (gpa > 3.7 OR gpa < 3.3);
```

### Review Questions & Answers

| Question | Answer |
|----------|--------|
| DELETE vs TRUNCATE | TRUNCATE: faster, no rollback, no WHERE. DELETE: slower, rollback possible, WHERE supported |
| DELETE vs DROP | DROP removes the whole table. DELETE only removes records |
| DROP vs DROP PURGE | DROP goes to recycle bin. DROP PURGE permanently deletes |

```sql
-- Same result using BETWEEN:
SELECT * FROM students WHERE age BETWEEN 8 AND 17;
-- instead of: WHERE age >= 8 AND age <= 17

-- Same result using NOT BETWEEN:
SELECT * FROM students WHERE age NOT BETWEEN 8 AND 17;
-- instead of: WHERE age < 8 OR age > 17

-- Same result using IN:
SELECT * FROM students WHERE grade IN (6, 7, 8, 9);
-- instead of: WHERE grade=6 OR grade=7 OR grade=8 OR grade=9
```

---

*📌 Next lesson: ORDER BY, ALIASES, GROUP BY, HAVING*

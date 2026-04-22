# 🗄️ Day 5 — UNION, INTERSECT, MINUS & JOINS

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [UNION](#union)
2. [UNION ALL](#union-all)
3. [INTERSECT](#intersect)
4. [MINUS](#minus)
5. [JOINS](#joins)
6. [SELF JOIN](#self-join)
7. [String Functions](#string-functions)
8. [Practice Exercises](#exercises)

---

## 🔗 UNION {#union}

`UNION` combines the results of two queries and **removes duplicate records**.

### UNION Rules:
1. Both queries must have the **same number of columns**
2. Corresponding columns must have **compatible data types**

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

-- States and names where salary > 3000
SELECT state AS name_and_state, salary
FROM employees
WHERE salary > 3000

UNION

SELECT name AS name_and_state, salary
FROM employees
WHERE salary > 3000;

-- Eddie Murphy's salaries + salaries paid in Florida
SELECT name AS name_state, salary
FROM employees
WHERE name = 'Eddie Murphy'

UNION

SELECT state AS name_state, salary
FROM employees
WHERE state = 'Florida'
ORDER BY salary;

-- Salary > 3000 OR salary < 2000 (no duplicates)
SELECT name AS name_and_state, salary
FROM employees
WHERE salary > 3000

UNION

SELECT state AS name_and_state, salary
FROM employees
WHERE salary < 2000;
```

---

## 📋 UNION ALL {#union-all}

`UNION ALL` includes duplicate records.

```sql
CREATE TABLE students
(
  students_id char(9),
  students_name varchar2(50),
  students_address varchar2(80),
  students_grade number(3),
  last_modification_date date,
  CONSTRAINTS id_pk PRIMARY KEY(students_id)
);

INSERT INTO students VALUES('123456789', 'Ali Can','Istanbul', 93, '12-Aug-20');
INSERT INTO students VALUES('234567890', 'Veli Han', 'Istanbul', 95, '13-Aug-20');
INSERT INTO students VALUES('345678901', 'Ayse Tan', 'Berlin', 95, '13-Aug-20');

CREATE TABLE students_information
(
  students_id char(9),
  students_phone char(10) UNIQUE,
  students_avg_score number(4,2) NOT NULL,
  CONSTRAINTS id_fk FOREIGN KEY(students_id) REFERENCES students(students_id)
);

INSERT INTO students_information VALUES('123456789', '4071234567', 78);
INSERT INTO students_information VALUES('234567890', '4071234598', 91);
INSERT INTO students_information VALUES('345678901', '4071230000', 93);

-- UNION: duplicate records shown only once
SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789'

UNION

SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789';
-- Result: ONE row

-- UNION ALL: duplicate records shown multiple times
SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789'

UNION ALL

SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789';
-- Result: TWO rows (same record twice)

-- Combine two different tables
SELECT students_name AS id_name, students_address AS address_phone, students_grade AS avg_score_grade
FROM students
WHERE students_id = '123456789'

UNION

SELECT students_id AS id_name, students_phone AS address_phone, students_avg_score AS avg_score_grade
FROM students_information
WHERE students_id = '123456789';
```

---

## ✂️ INTERSECT {#intersect}

`INTERSECT` shows only the **common results** of two queries.

```sql
-- Intersection of student grades and average scores
SELECT students_grade AS grade_avg_score
FROM students

INTERSECT

SELECT students_avg_score
FROM students_information;

-- Grades < 94 AND average scores > 80 intersection
SELECT students_grade
FROM students
WHERE students_grade < 94

INTERSECT

SELECT students_avg_score
FROM students_information
WHERE students_avg_score > 80;

-- Employees at IBM, APPLE, GOOGLE with salary > 3000
SELECT name
FROM employees
WHERE company IN ('IBM', 'APPLE', 'GOOGLE')

INTERSECT

SELECT name
FROM employees
WHERE salary > 3000;
```

> **Note:** If there are no common elements, no error is thrown — 'no data found' message appears.

---

## ➖ MINUS {#minus}

`MINUS` removes from the first query's results anything found in the second query.

```sql
-- Employees NOT at GOOGLE with salary < 2000
SELECT name, company
FROM employees
WHERE salary < 2000

MINUS

SELECT name, company
FROM employees
WHERE company = 'GOOGLE';

-- Employees named Eddie Murphy who do NOT live in Texas
SELECT name, state
FROM employees
WHERE name = 'Eddie Murphy'

MINUS

SELECT name, state
FROM employees
WHERE state = 'Texas';

-- Salary > 3000 OR salary < 2000, show names without duplicates
SELECT name
FROM employees
WHERE salary > 3000

UNION

SELECT name
FROM employees
WHERE salary < 2000;
```

---

## 🤝 JOINS {#joins}

**JOINS** combine data from two tables. There are 5 types:

| JOIN Type | Description |
|-----------|-------------|
| `INNER JOIN` | Shows **common** data from both tables |
| `LEFT JOIN` | All data from **first** table + matches from second |
| `RIGHT JOIN` | All data from **second** table + matches from first |
| `FULL JOIN` | **All** data from both tables |
| `SELF JOIN` | Table joined with itself |

```sql
CREATE TABLE companies
(
  company_id number(9),
  company_name varchar2(20)
);

INSERT INTO companies VALUES(100, 'IBM');
INSERT INTO companies VALUES(101, 'GOOGLE');
INSERT INTO companies VALUES(102, 'MICROSOFT');
INSERT INTO companies VALUES(103, 'APPLE');

CREATE TABLE orders
(
  order_id number(9),
  company_id number(9),
  order_date date
);

INSERT INTO orders VALUES(11, 101, '17-Apr-2020');
INSERT INTO orders VALUES(22, 102, '18-Apr-2020');
INSERT INTO orders VALUES(33, 103, '19-Apr-2020');
INSERT INTO orders VALUES(44, 104, '20-Apr-2020');  -- company_id=104 doesn't exist!
INSERT INTO orders VALUES(55, 105, '21-Apr-2020');  -- company_id=105 doesn't exist!
```

### INNER JOIN

```sql
-- Only orders where company_id matches in both tables
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies INNER JOIN orders
ON companies.company_id = orders.company_id;

-- Result: Only company_id 101, 102, 103 (104 and 105 excluded)
-- Note: INNER JOIN = JOIN (same thing)
```

### LEFT JOIN

```sql
-- ALL records from companies + matching order info
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies LEFT JOIN orders
ON companies.company_id = orders.company_id;

-- Result: IBM (no order → NULL), GOOGLE, MICROSOFT, APPLE
```

### RIGHT JOIN

```sql
-- ALL records from orders + matching company info
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies RIGHT JOIN orders
ON companies.company_id = orders.company_id;

-- Result: GOOGLE, MICROSOFT, APPLE + NULL (for 104, 105 - no company)
```

### FULL JOIN

```sql
-- ALL records from BOTH tables
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies FULL JOIN orders
ON companies.company_id = orders.company_id;
```

---

## 🪞 SELF JOIN {#self-join}

`SELF JOIN` joins a table **with itself**. Useful for hierarchical relationships (e.g., employee-manager).

```sql
CREATE TABLE workers
(
  id number(2),
  name varchar2(20),
  title varchar2(60),
  boss_id number(2)
);

INSERT INTO workers VALUES(1, 'Ali Can', 'SDET', 2);
INSERT INTO workers VALUES(2, 'John Walker', 'QA', 3);
INSERT INTO workers VALUES(3, 'Angie Star', 'QA Lead', 4);
INSERT INTO workers VALUES(4, 'Amy Sky', 'CEO', 5);

-- Show each employee's boss
SELECT w1.name AS worker_name, w2.name AS boss_name
FROM workers w1 INNER JOIN workers w2
ON w1.boss_id = w2.id;
```

---

## 🔠 String Functions {#string-functions}

```sql
-- LOWER: converts all letters to lowercase
-- UPPER: converts all letters to uppercase
-- INITCAP: capitalizes the first letter of each word

SELECT INITCAP(name), UPPER(state), LOWER(company)
FROM workers;

-- Examples:
-- INITCAP('ali can')  → Ali Can
-- UPPER('sdet')       → SDET
-- LOWER('IBM')        → ibm
```

---

## 🏋️ Practice Exercises {#exercises}

```sql
CREATE TABLE employees (...);
-- (Insert same 7 rows as above)
```

**Questions:**

1. Get employees with salary > 3000 OR salary < 2000 without duplicates (UNION)
2. Get common names of employees at IBM, APPLE, GOOGLE with salary > 3000 (INTERSECT)
3. Get names and companies of employees NOT at GOOGLE with salary < 2000 (MINUS)
4. Show each employee with their boss name (SELF JOIN using workers table)

```sql
-- Solutions:

-- 1)
SELECT *
FROM employees
WHERE salary > 3000
UNION
SELECT *
FROM employees
WHERE salary < 2000;

-- 2)
SELECT name
FROM employees
WHERE company IN ('IBM', 'APPLE', 'GOOGLE')
INTERSECT
SELECT name
FROM employees
WHERE salary > 3000;

-- 3)
SELECT name, company
FROM employees
WHERE salary < 2000
MINUS
SELECT name, company
FROM employees
WHERE company = 'GOOGLE';

-- 4)
SELECT w1.name AS worker_name, w2.name AS boss_name
FROM workers w1 INNER JOIN workers w2
ON w1.boss_id = w2.id;
```

---

*📌 Next lesson: EXISTS, BETWEEN, Wildcards, REGEXP_LIKE*

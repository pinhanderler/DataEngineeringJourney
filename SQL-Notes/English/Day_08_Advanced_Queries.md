# 🗄️ Day 8 — Advanced Queries, ROWNUM & MOD

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [ROWNUM with Ordered Queries](#rownum)
2. [OFFSET FETCH Pagination](#offset)
3. [MOD Function](#mod)
4. [Advanced Subqueries](#subquery-advanced)
5. [String Functions](#string-functions)
6. [Practice Exercises](#exercises)

---

## 🔢 ROWNUM with Ordered Queries {#rownum}

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

-- Show all employees except the one with highest salary, sorted descending
SELECT *
FROM employees
WHERE salary != (SELECT MAX(salary) FROM employees)
ORDER BY salary DESC;

-- Get all details of the employee with the second highest salary
-- Method 1: Using ROWNUM
SELECT *
FROM (SELECT *
      FROM employees
      WHERE salary != (SELECT MAX(salary) FROM employees)
      ORDER BY salary DESC)
WHERE ROWNUM = 1;
```

---

## 📄 OFFSET FETCH Pagination {#offset}

```sql
-- Second highest salary employee details
-- Method 2: Using OFFSET FETCH
SELECT *
FROM employees
ORDER BY salary DESC
OFFSET 1 ROW
FETCH NEXT 1 ROW ONLY;

-- Top 3 highest paid employees
SELECT name, salary
FROM employees
ORDER BY salary DESC
FETCH FIRST 3 ROWS ONLY;
```

---

## ➗ MOD Function {#mod}

`MOD(n, m)` → Returns the remainder when n is divided by m.

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  salary number(20),
  company varchar2(20)
);

INSERT INTO students VALUES(123456789, 'Johnny Walk', 'New Hampshire', 2500, 'IBM');
INSERT INTO students VALUES(234567891, 'Brian Pitt', 'Florida', 1500, 'LINUX');
INSERT INTO students VALUES(245678901, 'Eddie Murphy', 'Texas', 3000, 'WELLS FARGO');
INSERT INTO students VALUES(456789012, 'Teddy Murphy', 'Virginia', 1000, 'GOOGLE');
INSERT INTO students VALUES(567890124, 'Eddie Murphy', 'Massachusetts', 7000, 'MICROSOFT');
INSERT INTO students VALUES(456789012, 'Brad Pitt', 'Texas', 1500, 'TD BANK');
INSERT INTO students VALUES(123456719, 'Adem Stone', 'New Jersey', 2500, 'IBM');

-- Students with even-numbered IDs (MOD = 0 means divisible)
SELECT *
FROM students
WHERE MOD(id, 2) = 0;

-- Students with odd-numbered IDs
SELECT *
FROM students
WHERE MOD(id, 2) = 1;

-- How many records are in the table?
SELECT COUNT(*) AS num_of_records
FROM students;

-- How many different states are there?
SELECT COUNT(DISTINCT state) AS num_of_states
FROM students;
```

---

## 🔍 Advanced Subqueries {#subquery-advanced}

```sql
CREATE TABLE workers01
(
  id number(9),
  name varchar2(50),
  state varchar2(50),
  salary number(20),
  company varchar2(20)
);

INSERT INTO workers01 VALUES(123456789, 'John Walker', 'Florida', 2500, 'IBM');
INSERT INTO workers01 VALUES(234567890, 'Brad Pitt', 'Florida', 1500, 'APPLE');
INSERT INTO workers01 VALUES(345678901, 'Eddie Murphy', 'Texas', 3000, 'IBM');
INSERT INTO workers01 VALUES(456789012, 'Eddie Murphy', 'Virginia', 1000, 'GOOGLE');
INSERT INTO workers01 VALUES(567890123, 'Eddie Murphy', 'Texas', 7000, 'MICROSOFT');
INSERT INTO workers01 VALUES(456789012, 'Brad Pitt', 'Texas', 1500, 'GOOGLE');
INSERT INTO workers01 VALUES(123456710, 'Mark Stone', 'Pennsylvania', 2500, 'IBM');

-- Employee with highest salary
SELECT *
FROM workers01
WHERE salary = (SELECT MAX(salary) FROM workers01);

-- Employee with lowest salary
SELECT *
FROM workers01
WHERE salary = (SELECT MIN(salary) FROM workers01);

-- Second highest salary
SELECT MAX(salary)
FROM workers01
WHERE salary < (SELECT MAX(salary) FROM workers01);

-- Second lowest salary
SELECT MIN(salary)
FROM workers01
WHERE salary > (SELECT MIN(salary) FROM workers01);
```

---

## 🔠 String Functions {#string-functions}

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

-- LOWER: all letters lowercase
-- UPPER: all letters uppercase
-- INITCAP: first letter of each word uppercase
SELECT INITCAP(name), UPPER(title), LOWER(name)
FROM workers;

-- Results:
-- INITCAP('ali can')   → Ali Can
-- UPPER('sdet')        → SDET
-- LOWER('ALI CAN')     → ali can
```

---

## 🏋️ Practice Exercises {#exercises}

```sql
-- Use workers01 table from above
```

**Questions:**

1. Get all details of the employee with the highest salary
2. Get all details of the employee with the lowest salary
3. Get the second highest salary
4. Get the second lowest salary
5. Get employees with even-numbered IDs
6. Get the top 3 highest paid employees (use OFFSET FETCH)
7. Show all names in uppercase and all states in lowercase
8. Get names of employees in the second and third highest salary positions (OFFSET 1, FETCH 2)

```sql
-- Solutions:

-- 1)
SELECT * FROM workers01 WHERE salary = (SELECT MAX(salary) FROM workers01);

-- 2)
SELECT * FROM workers01 WHERE salary = (SELECT MIN(salary) FROM workers01);

-- 3)
SELECT MAX(salary) FROM workers01
WHERE salary < (SELECT MAX(salary) FROM workers01);

-- 4)
SELECT MIN(salary) FROM workers01
WHERE salary > (SELECT MIN(salary) FROM workers01);

-- 5)
SELECT * FROM workers01 WHERE MOD(id, 2) = 0;

-- 6)
SELECT * FROM workers01
ORDER BY salary DESC
FETCH FIRST 3 ROWS ONLY;

-- 7)
SELECT UPPER(name), LOWER(state) FROM workers01;

-- 8)
SELECT name, salary FROM workers01
ORDER BY salary DESC
OFFSET 1 ROW
FETCH NEXT 2 ROWS ONLY;
```

---

*📌 Next lesson: General Review & Comprehensive Exercises*

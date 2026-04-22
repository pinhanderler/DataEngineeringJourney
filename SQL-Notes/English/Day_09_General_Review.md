# 🗄️ Day 9 — General Review & Comprehensive Exercises

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 All Topics Summary

---

## 📋 SQL Commands Quick Reference

### DDL (Data Definition Language)
```sql
CREATE TABLE table_name (column type, ...);
ALTER TABLE table_name ADD column type;
ALTER TABLE table_name DROP COLUMN column;
ALTER TABLE table_name RENAME COLUMN old TO new;
ALTER TABLE table_name RENAME TO new_name;
ALTER TABLE table_name MODIFY column type constraint;
DROP TABLE table_name;
DROP TABLE table_name PURGE;
TRUNCATE TABLE table_name;
```

### DML (Data Manipulation Language)
```sql
INSERT INTO table VALUES (...);
INSERT INTO table (col1, col2) VALUES (...);
UPDATE table SET column = value WHERE condition;
DELETE FROM table WHERE condition;
```

### DQL (Data Query Language)
```sql
SELECT * FROM table;
SELECT col1, col2 FROM table WHERE condition;
SELECT * FROM table ORDER BY column [ASC|DESC];
SELECT column, COUNT(*) FROM table GROUP BY column;
SELECT column, COUNT(*) FROM table GROUP BY column HAVING condition;
```

### Set Operations
```sql
-- Union (no duplicates)
query1 UNION query2;

-- Union (with duplicates)
query1 UNION ALL query2;

-- Intersection
query1 INTERSECT query2;

-- Difference
query1 MINUS query2;
```

### JOINs
```sql
-- Common records only
FROM table1 INNER JOIN table2 ON condition;

-- All from left table
FROM table1 LEFT JOIN table2 ON condition;

-- All from right table
FROM table1 RIGHT JOIN table2 ON condition;

-- All from both tables
FROM table1 FULL JOIN table2 ON condition;

-- Self join
FROM table t1 INNER JOIN table t2 ON t1.col = t2.col;
```

---

## 🔍 Special Operators

```sql
-- Range check
WHERE column BETWEEN value1 AND value2;
WHERE column NOT BETWEEN value1 AND value2;

-- List check
WHERE column IN (value1, value2, value3);
WHERE column NOT IN (value1, value2, value3);

-- Null check
WHERE column IS NULL;
WHERE column IS NOT NULL;

-- Pattern matching
WHERE column LIKE 'J%';       -- starts with J
WHERE column LIKE '%e';       -- ends with e
WHERE column LIKE '%an%';     -- contains an
WHERE column LIKE '_ohn';     -- 4 chars, last 3 are 'ohn'
WHERE column NOT LIKE 'J%';   -- does NOT start with J

-- With subquery
WHERE EXISTS (SELECT ... FROM ... WHERE ...);
```

---

## 📊 Aggregate Functions

```sql
COUNT(*)         -- Total number of records
COUNT(column)    -- Count of non-NULL records
SUM(column)      -- Total
AVG(column)      -- Average
MIN(column)      -- Minimum value
MAX(column)      -- Maximum value
```

---

## 🎯 Comprehensive Exercises

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
```

### Section A — Basic Queries

1. Sort all employees by salary from highest to lowest
2. Get employees in Texas with salary greater than 2000
3. Get names of employees at IBM or GOOGLE (use IN)
4. Get employees with salary between 1500 and 3000 (use BETWEEN)
5. Get employees whose name starts with 'Brad' (use LIKE)

```sql
-- Solutions:
-- 1) SELECT * FROM employees ORDER BY salary DESC;
-- 2) SELECT * FROM employees WHERE state = 'Texas' AND salary > 2000;
-- 3) SELECT name FROM employees WHERE company IN ('IBM', 'GOOGLE');
-- 4) SELECT * FROM employees WHERE salary BETWEEN 1500 AND 3000;
-- 5) SELECT * FROM employees WHERE name LIKE 'Brad%';
```

### Section B — Grouping and Aggregate

1. Get the number of employees per company
2. Get the average salary per company
3. List companies with average salary greater than 2000
4. Get the total salary payment per state
5. List states with at least 2 employees

```sql
-- Solutions:
-- 1) SELECT company, COUNT(*) AS emp_count FROM employees GROUP BY company;
-- 2) SELECT company, AVG(salary) AS avg_salary FROM employees GROUP BY company;
-- 3) SELECT company, AVG(salary) AS avg_salary FROM employees GROUP BY company HAVING AVG(salary) > 2000;
-- 4) SELECT state, SUM(salary) AS total_salary FROM employees GROUP BY state;
-- 5) SELECT state, COUNT(*) AS emp_count FROM employees GROUP BY state HAVING COUNT(*) >= 2;
```

### Section C — Subquery and JOIN

1. Get employees whose company has more than 15000 employees (Subquery)
2. Get all details of the highest-paid employee
3. Get the second highest salary
4. Join companies and employees to show each employee's company size (JOIN)

```sql
-- Solutions:

-- 1)
SELECT name, company FROM employees
WHERE company IN (SELECT company FROM companies WHERE number_of_employees > 15000);

-- 2)
SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);

-- 3)
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- 4)
SELECT e.name, e.company, c.number_of_employees
FROM employees e INNER JOIN companies c
ON e.company = c.company;
```

### Section D — Set Operations

1. Get names of employees with salary > 3000 OR salary < 1500, without duplicates (UNION)
2. Get common names of employees at IBM or GOOGLE with salary > 2500 (INTERSECT)
3. Get employees NOT in Florida with salary < 2000 (MINUS)

```sql
-- Solutions:

-- 1)
SELECT name FROM employees WHERE salary > 3000
UNION
SELECT name FROM employees WHERE salary < 1500;

-- 2)
SELECT name FROM employees WHERE company IN ('IBM', 'GOOGLE')
INTERSECT
SELECT name FROM employees WHERE salary > 2500;

-- 3)
SELECT name, company FROM employees WHERE salary < 2000
MINUS
SELECT name, company FROM employees WHERE state = 'Florida';
```

---

## 📝 Final Quiz

**Q1:** What is the difference between the following three queries?
```sql
-- A)
SELECT * FROM employees WHERE salary > 2000;
GROUP BY company;   -- Syntax error!

-- B)
SELECT company, COUNT(*) FROM employees
WHERE salary > 2000
GROUP BY company;

-- C)
SELECT company, COUNT(*) FROM employees
GROUP BY company
HAVING COUNT(*) > 2;
```

> **Answer:** A has incorrect syntax. B first filters rows where salary > 2000 then groups by company. C first groups by company then filters groups with more than 2 employees.

---

**Q2:** Explain JOIN types.

> **Answer:**
> - **INNER JOIN:** Only records that exist in both tables
> - **LEFT JOIN:** All records from left table + matching records from right (non-matching → NULL)
> - **RIGHT JOIN:** All records from right table + matching records from left (non-matching → NULL)
> - **FULL JOIN:** All records from both tables (non-matching → NULL)
> - **SELF JOIN:** A table joined with itself

---

**Q3:** Show differences between DELETE, TRUNCATE and DROP in a table.

| Feature | DELETE | TRUNCATE | DROP |
|---------|--------|----------|------|
| WHERE clause | ✅ | ❌ | ❌ |
| Rollback | ✅ | ❌ | ❌ |
| Table structure | Remains | Remains | Deleted |
| Speed | Slower | Faster | Faster |

---

🎉 **Congratulations! You have completed the SQL course!**

*Practice more at: www.w3schools.com | https://sqlbolt.com/ | https://www.sqlteaching.com/*

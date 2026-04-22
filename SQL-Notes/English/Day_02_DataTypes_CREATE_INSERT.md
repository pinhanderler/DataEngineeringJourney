# 🗄️ Day 2 — SQL Data Types, CREATE TABLE & INSERT INTO

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [What is SQL?](#what-is-sql)
2. [SQL Sub-Languages](#sub-languages)
3. [SQL Data Types](#data-types)
4. [CREATE TABLE](#create-table)
5. [NOT NULL Constraint](#not-null)
6. [Adding PRIMARY KEY](#primary-key)
7. [Adding FOREIGN KEY](#foreign-key)
8. [INSERT INTO](#insert-into)
9. [INSERT ALL](#insert-all)
10. [Practice Exercises](#exercises)

---

## 🔷 What is SQL? {#what-is-sql}

**SQL = Structured Query Language**

SQL is a language used for interacting with **Relational Database Management Systems (RDBMS)**.

Using SQL we can:
1. Create and manage databases
2. Design database tables
3. Create, Read, Update, Delete data **(CRUD)**
4. Perform administration tasks like security, user management

> **Note:** SQL can be used for all RDBMS (MySQL, SQL Server, PostgreSQL, Oracle). The concepts are the same but implementation may differ slightly.

---

## 📋 SQL Sub-Languages {#sub-languages}

SQL is the combination of 4 different languages:

| Abbreviation | Full Name | Usage |
|--------------|-----------|-------|
| **DCL** | Data Control Language | Controls privileges, manages users and permissions |
| **DDL** | Data Definition Language | Defines structure of tables, columns |
| **DML** | Data Manipulation Language | Manipulates data: INSERT, UPDATE, DELETE |
| **DQL** | Data Query Language | Queries the database: SELECT |

---

## 📦 SQL Data Types {#data-types}

### String Data Types

| Data Type | Description |
|-----------|-------------|
| `char(size)` | Fixed length string. Max 2000 bytes. Ideal for fixed-length data like SSN, ZipCode |
| `nchar(size)` | Fixed length Unicode string. Used for data in different languages |
| `varchar2(size)` | Variable length string. Max 4000 bytes |
| `nvarchar2(size)` | Variable length Unicode string. Max 8000 bytes |

```sql
-- Example: char vs varchar2
-- Value "ab":
-- char(4)    → 'ab  ' (uses 4 bytes)
-- varchar2(4)→ 'ab'   (uses 2 bytes)
```

### Numeric Data Types

| Data Type | Description |
|-----------|-------------|
| `number(p, s)` | Numeric data. p=precision (total digits), s=scale (decimal digits) |

```sql
-- Examples:
number(5, 2)  → 123.45      (3 integer + 2 decimal)
number(7)     → 1234567     (scale zero)
number(7, -2) → 1234600     (rounds to hundreds)
number(4, 2)  → 12.34       -- 123.45 gives error! (precision exceeded)
```

### Date Data Type

| Data Type | Description |
|-----------|-------------|
| `DATE` | Stores date and time with second precision. Standard format: `dd-MMM-yy` |

```sql
-- Change date format:
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';
-- Now: 2020-04-13
```

### BLOB Data Type

| Data Type | Description |
|-----------|-------------|
| `BLOB` | Binary Large Objects. For images, audio, video |

---

## 🏗️ CREATE TABLE {#create-table}

### Method 1: Create from Scratch

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50),
  grade number(2),
  address varchar2(100),
  last_modification date
);
```

### Method 2: Create from an Existing Table

```sql
-- New table with only id and name from students
CREATE TABLE studentsIdName AS
SELECT id, name
FROM students;
```

---

## 🚫 NOT NULL Constraint {#not-null}

`NOT NULL` ensures a column cannot accept empty values.

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50) NOT NULL,   -- ← name cannot be empty
  grade number(2),
  address varchar2(100),
  last_modification date
);

-- Skipping a NOT NULL column gives an ERROR:
INSERT INTO students(id, grade) VALUES(123456789, 11);
-- ORA-01400: cannot insert NULL into "STUDENTS"."NAME"
```

---

## 🔑 Adding PRIMARY KEY {#primary-key}

### Method 1: Inline with column

```sql
CREATE TABLE students
(
  id number(9) PRIMARY KEY,    -- ← primary key here
  name varchar2(50) NOT NULL,
  grade number(2),
  address varchar2(100),
  last_modification date
);
```

### Method 2: Named CONSTRAINT

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50) NOT NULL,
  grade number(2),
  address varchar2(100),
  last_modification date,
  CONSTRAINT id_pk PRIMARY KEY(id)   -- ← named constraint
);
```

---

## 🔗 Adding FOREIGN KEY {#foreign-key}

```sql
-- Parent Table
CREATE TABLE students
(
  id number(9) PRIMARY KEY,
  name varchar2(50),
  grade number(2),
  address varchar2(100),
  last_modification date
);

-- Child Table
CREATE TABLE studentPhoneNumber
(
  studentId number(9),
  PhoneNumber varchar2(10),
  CONSTRAINT studentId_fk FOREIGN KEY(studentId) REFERENCES students(id)
);
```

> ⚠️ **Note 1:** You cannot insert data with an id that doesn't exist in the Parent Table!
> ⚠️ **Note 2:** You cannot drop the Parent Table without dropping the Child Table first!

---

## ➕ INSERT INTO {#insert-into}

### Insert values for all columns

```sql
INSERT INTO students VALUES(123456789, 'John Walker', 11, '1234 W 12th TER Addison Texas 75001', '14-Apr-2020');
```

### Insert values for selected columns

```sql
-- Only id and name, others remain NULL
INSERT INTO students(id, name) VALUES(234567890, 'John Walker');
```

---

## 📥 INSERT ALL {#insert-all}

Insert multiple rows at once:

```sql
-- INSERT ALL into single table
INSERT ALL
  INTO supplier (supplier_id, supplier_name) VALUES (1001, 'IBM')
  INTO supplier (supplier_id, supplier_name) VALUES (2002, 'Microsoft')
  INTO supplier (supplier_id, supplier_name) VALUES (3003, 'Google')
SELECT * FROM dual;
```

```sql
-- INSERT ALL into multiple tables
INSERT ALL
  INTO supplier (supplier_id, supplier_name) VALUES (4004, 'APPLE')
  INTO supplier (supplier_id, supplier_name) VALUES (5005, 'LINUX')
  INTO products (supplier_id, product_id) VALUES (1001, 10011)
  INTO products (supplier_id, product_id) VALUES (2002, 20022)
SELECT * FROM dual;
```

---

## 🏋️ Practice Exercises {#exercises}

### Exercise 1
Create a table called **"suppliers"** that stores `supplier_id`, `name`, and address information with street, city, state, and zip code as separate columns.

```sql
-- Solution:
CREATE TABLE suppliers
(
  supplier_id number(10) PRIMARY KEY,
  name varchar2(50) NOT NULL,
  street varchar2(100),
  city varchar2(50),
  state varchar2(50),
  zip_code char(5)
);
```

### Exercise 2
Create **"suppliers_id_name"** using the `suppliers` table with only `supplier_id` and `name`.

```sql
-- Solution:
CREATE TABLE suppliers_id_name AS
SELECT supplier_id, name
FROM suppliers;
```

### Exercise 3
Create **"cities"** with `area_code` (PRIMARY KEY), `name`, `population`, `state`. Add PRIMARY KEY using method 1.

```sql
-- Solution:
CREATE TABLE cities
(
  area_code number(5) PRIMARY KEY,
  name varchar2(100) NOT NULL,
  population number(15),
  state varchar2(50)
);
```

### Exercise 4
Create **"teachers"** with `SSN`, `name`, `subject`, `gender`. Add PRIMARY KEY using method 2.

```sql
-- Solution:
CREATE TABLE teachers
(
  SSN char(9),
  name varchar2(50) NOT NULL,
  subject varchar2(50),
  gender varchar2(10),
  CONSTRAINT teachers_pk PRIMARY KEY(SSN)
);
```

### Exercise 5
Insert teacher: SSN=234431223, name=Jane Smith, subject=Mathematics, gender=female.

```sql
-- Solution:
INSERT INTO teachers VALUES('234431223', 'Jane Smith', 'Mathematics', 'female');
```

---

*📌 Next lesson: UPDATE SET, DELETE, TRUNCATE, DROP, SELECT, WHERE*

# 🗄️ Day 1 — Database Fundamentals & Introduction to SQL

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Table of Contents

1. [What is a Database?](#what-is-a-database)
2. [Advantages of Storing Data in Computers](#advantages)
3. [Database Management System (DBMS)](#dbms)
4. [Database Validation Test](#validation)
5. [SQL Tables](#tables)
6. [Relational Databases](#relational)
7. [Popular Databases](#popular)
8. [Non-Relational Databases](#nosql)
9. [Primary Key](#primary-key)
10. [Foreign Key](#foreign-key)
11. [Composite Key](#composite-key)
12. [UNIQUE KEY vs PRIMARY KEY](#unique-vs-primary)
13. [Practice Exercises](#exercises)

---

## 🔷 What is a Database? {#what-is-a-database}

A **database** is a collection of related information.

### Examples:
- 📞 Phone book
- ✅ Todo list
- 👥 Names of Facebook users
- 🎓 Names of students in a school

Data can be stored in different ways: paper, computer memory, cloud, etc.

---

## ✅ Advantages of Storing Data in Computers {#advantages}

| # | Advantage |
|---|-----------|
| 1 | Huge amount of data can be stored |
| 2 | Easy to Create, Read, Update, Delete (CRUD) |
| 3 | Easy to access |
| 4 | Quick access |
| 5 | Security |

---

## 🖥️ Database Management System (DBMS) {#dbms}

**DBMS** is a special software program that enables its users to:

1. Access the database
2. Create, Read, Update, Delete **(CRUD)**
3. Get reports from the database
4. Control access to the database **(Security)**
5. Interact with other applications

---

## 🔐 Database Validation Test {#validation}

```
User Interface  ──────────►  API  ──────────►  Database
     (UI)                                          (DB)
```

When a user fills out a form, data flows from the UI through the API to the database.
Test engineers verify that this data flow works correctly.

---

## 📊 SQL Tables {#tables}

Data in a database is stored in **table** format.

```
contactID | name           | company          | email
----------|----------------|------------------|---------------------------
    1     | Bill Gates     | Microsoft        | bill@XBoxOneRocks.com
    2     | Steve Jobs     | Apple            | steve@rememberNewton.com
    3     | Linus Torvalds | Linux Foundation | linus@gnuWho.org
    4     | Andy Harris    | Wiley Press      | andy@aharrisBooks.net
```

- **Row (Record):** A single record
- **Column (Field):** A category of data

---

## 🔗 Relational Databases (SQL Databases) {#relational}

1. A relational database **stores data in tables**
2. The relationship between each data point is **clear and easy** to search
3. The relationship between tables and field types is called a **schema**
4. Relational databases are also called **SQL Databases**

> **SQL = Structured Query Language**

---

## 🏢 Popular Relational Databases {#popular}

### 🔴 SQL Server
- **Developed by:** Microsoft
- ✅ Pro: Rich user interface, can handle large quantities of data
- ❌ Con: Can be expensive (Enterprise level costs thousands of dollars)

### 🐬 MySQL Server
- **Created by:** A Swedish company
- ✅ Pro: Free and open-source, lots of documentation and online support
- ❌ Con: Tends to stop working when given too many operations at once

### 🐘 PostgreSQL Server
- **Created by:** Prof. Michael Stonebraker
- ✅ Pro: You can add additional features yourself
- ❌ Con: Installation and configuration can be difficult

### 🔶 Oracle PL/SQL
- Procedural language designed to embrace SQL statements
- ✅ Pro: High security level, OOP support

---

## 📦 Non-Relational Databases (NoSQL) {#nosql}

A **non-relational** database does not use the tabular schema of rows and columns.

```
SQL (Relational)         NoSQL (Non-Relational)
────────────────         ──────────────────────
Product Price  │         ┌─────────────────────────┐
Product Ingr.  │         │  Price                  │
Buying Rate    │         │  Ingredients            │
               │         │  Rate                   │
               │         │  All other related data │
               │         └─────────────────────────┘
```

---

## 🔑 Primary Key {#primary-key}

- A primary key **uniquely identifies** each record
- A table can have only **one** primary key
- Primary key **cannot contain NULL values**
- Primary key can be a number, string, character, etc.

### Natural Key vs Surrogate Key:
- **Natural Key:** Real values like SSN or email address
- **Surrogate Key:** Sequential numbers like 1, 2, 3, 4...

```sql
-- Example table
StudentID | FirstName | LastName
----------|-----------|----------
   10     | John      | Walker     ← Primary Key: 10
   11     | Tom       | Hanks
   12     | Kevin     | Star
   13     | Carl      | Wall       ← Primary Key: 13
```

---

## 🔗 Foreign Key {#foreign-key}

- Foreign Key is used to **create a link between two tables**
- A column in one table that **refers to the Primary Key** of another table
- A table can have **many Foreign Keys**
- Foreign Key **can have NULL value**

```
Parent Table                     Child Table
────────────────────────         ────────────────────────
StudentID │ FirstName            CourseID │ CourseName
──────────┼──────────            ─────────┼───────────
   10     │ John       ◄───────     200   │ Math
   11     │ Tom                     400   │ Selective
```

> **Note:** You cannot drop the Parent Table without dropping the Child Table first!

---

## 🔑 Composite Key {#composite-key}

A Composite Key is a **combination of two or more columns**. Each column alone doesn't guarantee uniqueness, but together they do.

```sql
-- Combination of Job_ID and Recruiter → Composite Primary Key
Job_ID | Recruiter  | Company
-------|------------|----------
  2    | Mark Eye   | RCG
  3    | John Ted   | RCG
  1    | Mark Eye   | Signature   ← Job_ID=1, Recruiter=Mark Eye → Unique
  1    | John Ted   | InfoLog     ← Job_ID=1, Recruiter=John Ted → Unique
```

---

## 🆚 UNIQUE KEY vs PRIMARY KEY {#unique-vs-primary}

| Feature | Primary Key | Unique Key |
|---------|-------------|------------|
| Count | Only **1** per table | Multiple allowed |
| NULL | **Not accepted** | Only **1** NULL accepted |
| Duplicates | Not allowed | Not allowed |
| Foreign Key Reference | Yes | Yes |

---

## 🏋️ Practice Exercises {#exercises}

### Exercise 1
Answer the following questions using the `employees` and `job` tables:

```
Emp_ID | first_name | last_name | salary  | Job_ID | Manager_ID
-------|------------|-----------|---------|--------|------------
  100  | Jan        | Levinson  | 110,000 |   1    |   NULL
  101  | Michael    | Scott     |  75,000 |   2    |   100
  102  | Josh       | Porter    |  78,000 |   3    |   100
  103  | Angela     | Martin    |  63,000 |   2    |   101
  104  | Andy       | Bernard   |  65,000 |   3    |   101

Job_ID | Job_Name
-------|-------------
   2   | SDET
   3   | Manual Tester
   1   | QE Lead
```

**Questions:**
1. Who is the manager of Michael Scott?
2. What is the job name of Angela Martin?
3. What is the average salary of Manual Testers?
4. What is the job name of the highest salary?

---

### 💡 Quiz Questions

**Question 1:** Which of the following is true about DELETE and DROP?
- A) In both cases, deleted data can be recovered
- B) DROP deletes the table and its records. DELETE only deletes records ✅
- C) `DELETE FROM products PURGE` ensures deleted data cannot be recovered

**Question 2:** The query `WHERE company='APPLE' OR company='GOOGLE'` shows which names?
- A) Brad Pitt, Eddie Murphy, Brad Pitt ✅
- B) Returns an error
- C) Shows no names
- D) Brad Pitt, Eddie Murphy

---

*📌 Next lesson: SQL Data Types, CREATE TABLE, INSERT INTO*

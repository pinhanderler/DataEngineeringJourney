# Azure Data Engineering & Analytics – End-to-End Project  
### Full Data Integration & Analytics: MySQL → Snowflake → MongoDB

---

![Project Architecture](Architecture_End_to_End_Data_Integration_Analytics_Project.png)

---

## 📌 Project Overview

This project demonstrates a **complete data engineering lifecycle** using the **Sakila film rental database**, integrating relational, cloud, and NoSQL architectures.  

The pipeline simulates real-world workflows across three platforms:  

- **MySQL** – Operational relational database  
- **Snowflake** – Cloud-based data warehouse for analytics  
- **MongoDB** – NoSQL document store for flexible data modeling  

Key objectives include:  

- Data modeling (ERD and Star Schema)  
- ETL workflow development  
- Cloud analytics and reporting  
- Document modeling in NoSQL  

---

## 🎯 Objective

Migrate, transform, and analyze the Sakila dataset across multiple platforms, gaining hands-on experience with:

- Relational and NoSQL database design  
- End-to-end ETL processes  
- Cloud data warehousing and analytical queries  
- Aggregation and document modeling  

---

## 🚦 Project Phases

### 🔹 Phase 1 – MySQL

**Goal:** Explore relational schema and extract source data.  

**Tasks:**  

- Install MySQL Workbench  
- Import `sakila-schema.sql` & `sakila-data.sql`  
- Explore tables, relationships, and create ERD  
- Execute analytical SQL queries (e.g., top films, rentals by country)  
- Export `customer`, `rental`, and `payment` tables as CSV  

**Deliverables:**  
- ERD diagram (PNG/PDF)  
- SQL queries screenshots  
- CSV exports  

---

### 🔹 Phase 2 – Snowflake

**Goal:** Transform source data for analytics in a Star Schema.  

**Tasks:**  

- Set up Snowflake account, warehouse, and schema  
- Load CSVs via `STAGE` and `COPY INTO`  
- Design fact and dimension tables (Star Schema)  
- Run analytical queries (monthly revenue, top countries, trends)  

**Deliverables:**  
- Star Schema diagram  
- Snowflake SQL scripts and results  

---

### 🔹 Phase 3 – MongoDB

**Goal:** Model relational data as documents and perform aggregations.  

**Tasks:**  

- Create MongoDB Atlas cluster  
- Import CSVs into collections using Compass  
- Design embedded/referenced document structures  
- Define indexes for optimized queries  
- Write aggregation queries (e.g., total rentals/payments by country)  

**Deliverables:**  
- JSON document structures  
- Aggregation queries and results  

---

## 🧰 Tools & Resources

| Platform | Tool               | Link                                                                 |
|----------|------------------|----------------------------------------------------------------------|
| MySQL    | Workbench          | [Download](https://dev.mysql.com/downloads/workbench)               |
| Snowflake| Web UI/Worksheets  | [Sign Up](https://signup.snowflake.com)                             |
| MongoDB  | Atlas & Compass    | [Atlas](https://www.mongodb.com/atlas) • [Compass](https://www.mongodb.com/products/tools/compass) |

---

## 📦 Deliverables

- ERD and Star Schema diagrams  
- SQL & MongoDB scripts  
- CSV data files  
- Screenshots of key steps  
- Short reflection comparing relational, cloud, and NoSQL architectures  
- Repository uploaded to GitHub  

---

## 🎓 Learning Outcomes

- Design and document relational & NoSQL databases  
- Implement end-to-end ETL workflows  
- Perform analytics with SQL and MongoDB aggregation queries  
- Understand OLTP, OLAP, and NoSQL architecture differences  

---

## 🧑‍🏫 Note

This project simulates a real-world data engineering workflow. Document all steps carefully, analyze data flow, and reflect on differences between relational, cloud, and NoSQL systems.

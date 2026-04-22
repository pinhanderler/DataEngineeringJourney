# 🗄️ Gün 5 — UNION, INTERSECT, MINUS & JOINS

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [UNION](#union)
2. [UNION ALL](#union-all)
3. [INTERSECT](#intersect)
4. [MINUS](#minus)
5. [JOINS](#joins)
6. [SELF JOIN](#self-join)
7. [Alıştırmalar](#alıştırmalar)

---

## 🔗 UNION {#union}

`UNION`, iki farklı sorgunun sonuçlarını birleştirir ve **tekrar eden kayıtları göstermez**.

### UNION Kuralları:
1. Her iki sorgudaki **sütun sayıları eşit** olmalı
2. Karşılıklı sütunların **data type'ları aynı** olmalı

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

-- Maaşı 3000'den fazla olan state ve isimler
SELECT state AS name_and_state, salary
FROM employees
WHERE salary > 3000

UNION

SELECT name AS name_and_state, salary
FROM employees
WHERE salary > 3000;

-- Eddie Murphy'nin maaşları + Florida'daki maaşlar
SELECT name AS name_state, salary
FROM employees
WHERE name = 'Eddie Murphy'

UNION

SELECT state AS name_state, salary
FROM employees
WHERE state = 'Florida'
ORDER BY salary;
```

---

## 📋 UNION ALL {#union-all}

`UNION ALL`, tekrar eden kayıtları da gösterir.

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

CREATE TABLE students_information
(
  students_id char(9),
  students_phone char(10) UNIQUE,
  students_avg_score number(4,2) NOT NULL,
  CONSTRAINTS id_fk FOREIGN KEY(students_id) REFERENCES students(students_id)
);

INSERT INTO students_information VALUES('123456789', '4071234567', 78);
INSERT INTO students_information VALUES('234567890', '4071234598', 91);

-- UNION: tekrar eden kayıtlar 1 kez gösterilir
SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789'

UNION

SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789';
-- Sonuç: Tek satır

-- UNION ALL: tekrar eden kayıtlar gösterilir
SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789'

UNION ALL

SELECT students_name, students_address, students_grade
FROM students
WHERE students_id = '123456789';
-- Sonuç: İki satır (aynı kayıt iki kez)
```

---

## ✂️ INTERSECT {#intersect}

`INTERSECT`, iki sorgunun **ortak sonuçlarını** gösterir.

```sql
-- Öğrenci notları ile ortalama notların kesişimi
SELECT students_grade AS grade_avg_score
FROM students

INTERSECT

SELECT students_avg_score
FROM students_information;

-- IBM, APPLE, GOOGLE'da çalışıp maaşı 3000'den fazla olanlar
SELECT name
FROM employees
WHERE company IN ('IBM', 'APPLE', 'GOOGLE')

INTERSECT

SELECT name
FROM employees
WHERE salary > 3000;
```

> **Not:** Ortak eleman yoksa hata vermez, 'no data found' mesajı verir.

---

## ➖ MINUS {#minus}

`MINUS`, birinci sorgudaki sonuçlardan ikinci sorgudakileri **çıkarır**.

```sql
-- GOOGLE'da çalışmayıp maaşı 2000'den az olanlar
SELECT name, company
FROM employees
WHERE salary < 2000

MINUS

SELECT name, company
FROM employees
WHERE company = 'GOOGLE';

-- Adı Eddie Murphy olup Texas'ta yaşamayanlar
SELECT name, state
FROM employees
WHERE name = 'Eddie Murphy'

MINUS

SELECT name, state
FROM employees
WHERE state = 'Texas';
```

---

## 🤝 JOINS {#joins}

**JOINS**, iki tablodaki verileri birleştirir. 5 çeşit JOIN vardır:

| JOIN Türü | Açıklama |
|-----------|----------|
| `INNER JOIN` | İki tablodaki **ortak** verileri gösterir |
| `LEFT JOIN` | **Birinci** tablodaki tüm veriler + eşleşenler |
| `RIGHT JOIN` | **İkinci** tablodaki tüm veriler + eşleşenler |
| `FULL JOIN` | Her iki tablodaki **tüm** veriler |
| `SELF JOIN` | Tablonun kendisiyle birleşimi |

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
INSERT INTO orders VALUES(44, 104, '20-Apr-2020');  -- company_id=104 yok!
INSERT INTO orders VALUES(55, 105, '21-Apr-2020');  -- company_id=105 yok!
```

### INNER JOIN

```sql
-- İki tabloda company_id eşleşen siparişleri getir
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies INNER JOIN orders
ON companies.company_id = orders.company_id;

-- Sonuç: Sadece company_id 101, 102, 103 olanlar (104 ve 105 yok)
```

### LEFT JOIN

```sql
-- companies tablosundaki TÜM veriler + eşleşen order bilgileri
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies LEFT JOIN orders
ON companies.company_id = orders.company_id;

-- Sonuç: IBM (order yok → NULL), GOOGLE, MICROSOFT, APPLE
```

### RIGHT JOIN

```sql
-- orders tablosundaki TÜM veriler + eşleşen company bilgileri
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies RIGHT JOIN orders
ON companies.company_id = orders.company_id;

-- Sonuç: GOOGLE, MICROSOFT, APPLE + NULL (104, 105 için company yok)
```

### FULL JOIN

```sql
-- Her iki tablodaki TÜM veriler
SELECT companies.company_name, orders.order_id, orders.order_date
FROM companies FULL JOIN orders
ON companies.company_id = orders.company_id;
```

---

## 🪞 SELF JOIN {#self-join}

`SELF JOIN`, bir tablonun **kendisiyle** birleşmesidir. Hiyerarşik ilişkilerde kullanılır (örn. çalışan-müdür).

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

-- Her çalışanın patronunu gösteren tablo
SELECT w1.name AS worker_name, w2.name AS boss_name
FROM workers w1 INNER JOIN workers w2
ON w1.boss_id = w2.id;
```

---

## 🔠 String Fonksiyonları

```sql
-- LOWER: tüm harfleri küçük yap
-- UPPER: tüm harfleri büyük yap
-- INITCAP: her kelimenin ilk harfini büyük yap

SELECT INITCAP(name), UPPER(state), LOWER(company)
FROM workers;
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

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

**Sorular:**

1. Maaşı 3000'den fazla veya 2000'den az olan çalışanların bilgilerini tekrarsız getirin (UNION)
2. IBM, APPLE ve GOOGLE'da çalışıp maaşı 3000'den fazla olan çalışanların ortak isimlerini getirin (INTERSECT)
3. GOOGLE'da çalışmayıp maaşı 2000'den az olan çalışanların isim ve şirketlerini getirin (MINUS)

```sql
-- Çözümler:

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
```

---

*📌 Sonraki ders: EXISTS, BETWEEN, Wildcards, REGEXP_LIKE*

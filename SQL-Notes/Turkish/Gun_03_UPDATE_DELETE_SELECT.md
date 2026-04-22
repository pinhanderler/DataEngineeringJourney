# 🗄️ Gün 3 — UPDATE SET, DELETE, TRUNCATE, DROP & SELECT

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [UPDATE SET](#update-set)
2. [DELETE FROM](#delete-from)
3. [TRUNCATE TABLE](#truncate)
4. [DROP TABLE](#drop)
5. [SELECT Statement](#select)
6. [WHERE Filtresi](#where)
7. [IN Koşulu](#in)
8. [SUBQUERY (Alt Sorgu)](#subquery)
9. [Alıştırmalar](#alıştırmalar)

---

## ✏️ UPDATE SET {#update-set}

`UPDATE SET` mevcut kayıtları güncellemek için kullanılır.

### Temel Kullanım

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

-- supplier_id=1 olan kaydı güncelle
UPDATE supplier
SET supplier_name = 'LINUX',
    contact_name = 'Alex Leo'
WHERE supplier_id = 1;

-- supplier_id < 3 olan tüm kayıtları güncelle
UPDATE supplier
SET supplier_name = 'LG',
    contact_name = 'El Ci'
WHERE supplier_id < 3;
```

### Başka Tablodan Değer ile Güncelleme (Subquery ile)

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

-- supplier tablosundaki supplier_name'i,
-- products tablosundaki product_name ile güncelle
-- (contact_name eşleştiğinde)
UPDATE supplier
SET supplier_name = (SELECT product_name
                     FROM products
                     WHERE supplier.contact_name = products.customer_name)
WHERE supplier_id < 3;
```

> **Not:** Bu örnek; `contact_name` = `customer_name` eşleştiğinde supplier_name'i günceller.

---

## 🗑️ DELETE FROM {#delete-from}

`DELETE FROM` tablodaki kayıtları siler ama tabloyu silmez.

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

-- 1) Tüm kayıtları sil (tablo yapısı kalır)
DELETE FROM students;

-- 2) Belirli bir kaydı sil
DELETE FROM students WHERE name = 'John Walker';

-- 3) Birden fazla koşulla sil
DELETE FROM students WHERE name = 'John Walker' OR state = 'New York';
```

---

## ✂️ TRUNCATE TABLE {#truncate}

`TRUNCATE`, tabloyu hızlıca boşaltır. `DELETE FROM` ile aynı sonucu verir ama farkları var:

```sql
TRUNCATE TABLE customers;
-- = DELETE FROM customers; ile aynı sonuç
```

| Özellik | DELETE FROM | TRUNCATE TABLE |
|---------|-------------|----------------|
| Geri alma (Rollback) | ✅ Mümkün | ❌ Mümkün değil |
| WHERE kullanımı | ✅ Kullanılabilir | ❌ Kullanılamaz |
| Hız | Yavaş | Hızlı |

---

## 💣 DROP TABLE {#drop}

`DROP`, tabloyu **tüm içeriği ve yapısıyla birlikte** siler.

```sql
-- Tabloyu çöp kutusuna taşır (kurtarılabilir)
DROP TABLE students;

-- Tabloyu kalıcı olarak siler (çöp kutusuna bile gitmez)
DROP TABLE students PURGE;
```

| Komut | Sonuç |
|-------|-------|
| `DELETE FROM` | Kayıtları siler, tablo kalır |
| `TRUNCATE TABLE` | Tüm kayıtları siler, tablo kalır, rollback yok |
| `DROP TABLE` | Tablo + içerik silinir, çöp kutusuna gider |
| `DROP TABLE ... PURGE` | Tablo + içerik kalıcı olarak silinir |

---

## 🔍 SELECT Statement {#select}

### Tüm Sütunları Seç

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

-- Tüm veriyi getir
SELECT * FROM students;
```

### Belirli Sütunları Seç

```sql
-- GPA'si 3.2'den büyük öğrencilerin adı ve id'si
SELECT name, id
FROM students
WHERE gpa > 3.2;
```

---

## 🔎 WHERE Filtresi {#where}

`WHERE`, SELECT, INSERT, UPDATE veya DELETE'de sonuçları filtrelemek için kullanılır.

### Operatörler

| Operatör | Anlam |
|----------|-------|
| `=` | Eşit |
| `>` | Büyüktür |
| `<` | Küçüktür |
| `>=` | Büyük veya eşit |
| `<=` | Küçük veya eşit |
| `<>` | Eşit değil |
| `AND` | VE |
| `OR` | VEYA |

```sql
-- GPA 2.8 VEYA state Florida olan öğrencilerin adı
SELECT name
FROM students
WHERE gpa = 2.8 OR state = 'Florida';

-- State New York VE GPA 3.5 olan öğrencilerin adı ve id'si
SELECT name, id
FROM students
WHERE state = 'New York' AND gpa = 3.5;
```

---

## 📋 IN Koşulu {#in}

`IN`, birden fazla `OR` koşulunu kısaltmak için kullanılır.

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

-- IN kullanmadan:
SELECT *
FROM customers_products
WHERE product_name = 'Orange' OR product_name = 'Apple' OR product_name = 'Apricot';

-- IN ile (daha kısa):
SELECT *
FROM customers_products
WHERE product_name IN ('Orange', 'Apple', 'Apricot');
```

---

## 🔄 SUBQUERY (Alt Sorgu) {#subquery}

**Subquery**, bir sorgu içindeki başka bir sorgudur.

### WHERE'de Subquery

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

-- 15000'den fazla çalışanı olan şirketlerin isimlerini getir
SELECT name, company
FROM employees
WHERE company IN (SELECT company
                  FROM companies
                  WHERE number_of_employees > 15000);
```

### SELECT'te Subquery

```sql
-- Her şirketin çalışan sayısı ve ortalama maaşı
SELECT company, number_of_employees,
       (SELECT AVG(salary)
        FROM employees
        WHERE companies.company = employees.company) Average_Salary_Per_Company
FROM companies;
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

### Alıştırma 1
Aşağıdaki tabloyu oluşturun ve işlemleri yapın:

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
```

**Sorular:**
1. GPA'si 3.1'den büyük VEYA state'i "Texas" olan tüm öğrencileri getirin
2. GPA'si 3.5'ten küçük VE state'i "Florida" olan öğrencilerin adını getirin
3. GPA'si 2.8 ile 3.5 arasındaki öğrencilerin adı ve id'sini getirin
4. State'i "New York" VE GPA'si 3.3'ten büyük ve 3.7'den küçük olan tüm öğrencileri getirin
5. State'i "New York" VE GPA 3.7'den büyük VEYA 3.3'ten küçük olan tüm öğrencileri getirin

```sql
-- Çözümler:
-- 1)
SELECT * FROM students WHERE gpa > 3.1 OR state = 'Texas';

-- 2)
SELECT name FROM students WHERE gpa < 3.5 AND state = 'Florida';

-- 3)
SELECT name, id FROM students WHERE gpa BETWEEN 2.8 AND 3.5;

-- 4)
SELECT * FROM students WHERE state = 'New York' AND gpa > 3.3 AND gpa < 3.7;

-- 5)
SELECT * FROM students WHERE state = 'New York' AND (gpa > 3.7 OR gpa < 3.3);
```

---

### Alıştırma 2

```sql
CREATE TABLE students
(
  student_id number(9),
  student_name varchar2(50),
  student_grade number(2),
  student_gpa number(3,1),
  school_name varchar2(50)
);
```

a) GPA'leri: 2.6, 1.9, 3.2, 3.8, 3.5 olan 5 farklı veri ekleyin
b) GPA'si 3.0'dan fazla olan öğrenci adlarını "Gifted Student" olarak güncelleyin

```sql
-- Çözüm:
INSERT INTO students VALUES(1, 'Ali Can', 10, 2.6, 'ABC School');
INSERT INTO students VALUES(2, 'Veli Han', 11, 1.9, 'XYZ School');
INSERT INTO students VALUES(3, 'Ayse Tan', 10, 3.2, 'ABC School');
INSERT INTO students VALUES(4, 'Mehmet Kim', 12, 3.8, 'DEF School');
INSERT INTO students VALUES(5, 'Zeynep Ay', 11, 3.5, 'XYZ School');

UPDATE students
SET student_name = 'Gifted Student'
WHERE student_gpa > 3.0;
```

---

### Alıştırma 3 — Review Soruları

**Soru 1:** DELETE ve TRUNCATE arasındaki fark nedir?

> **Cevap:**
> - TRUNCATE tüm satırları siler, DELETE koşula göre siler
> - TRUNCATE rollback yapılamaz, DELETE rollback yapılabilir
> - TRUNCATE'de WHERE kullanılamaz, DELETE'de kullanılabilir

**Soru 2:** DELETE ve DROP arasındaki fark nedir?

> **Cevap:** DROP tabloyu veritabanından kaldırır, DELETE sadece kayıtları siler.

**Soru 3:** DROP ve DROP PURGE arasındaki fark nedir?

> **Cevap:** DROP tabloyu çöp kutusuna taşır. DROP PURGE ile kalıcı olarak silinir, çöp kutusuna gitmez.

**Soru 4:** Aşağıdaki sorguyla aynı sonucu veren sorguyu yazın:
```sql
SELECT * FROM students WHERE age >= 8 AND age <= 17;
```
```sql
-- Cevap:
SELECT * FROM students WHERE age BETWEEN 8 AND 17;
```

**Soru 5:** Aşağıdaki sorguyla aynı sonucu veren sorguyu yazın:
```sql
SELECT * FROM students WHERE age < 8 OR age > 17;
```
```sql
-- Cevap:
SELECT * FROM students WHERE age NOT BETWEEN 8 AND 17;
```

**Soru 6:** Aşağıdaki sorguyla aynı sonucu veren sorguyu yazın:
```sql
SELECT * FROM students WHERE grade = 6 OR grade = 7 OR grade = 8 OR grade = 9;
```
```sql
-- Cevap:
SELECT * FROM students WHERE grade IN (6, 7, 8, 9);
```

---

*📌 Sonraki ders: ORDER BY, GROUP BY, HAVING, ALIASES, JOINS*

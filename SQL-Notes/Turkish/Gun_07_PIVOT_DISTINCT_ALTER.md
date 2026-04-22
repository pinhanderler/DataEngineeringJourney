# 🗄️ Gün 7 — PIVOT, DISTINCT & ALTER TABLE

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [PIVOT](#pivot)
2. [DISTINCT](#distinct)
3. [ALTER TABLE](#alter-table)
4. [Alıştırmalar](#alıştırmalar)

---

## 🔄 PIVOT {#pivot}

`PIVOT` satırları sütuna dönüştürür.

```sql
CREATE TABLE customers_products
(
  product_id number(10),
  customer_name varchar2(50),
  product_name varchar2(50)
);

INSERT INTO customers_products VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_products VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_products VALUES (20, 'John', 'Apple');
INSERT INTO customers_products VALUES (30, 'Amy', 'Palm');
INSERT INTO customers_products VALUES (20, 'Mark', 'Apple');
INSERT INTO customers_products VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');
INSERT INTO customers_products VALUES (20, 'Eddie', 'Apple');

-- Her müşterinin kaç tane hangi üründen aldığını tablo halinde göster
SELECT * FROM (SELECT customer_name, product_name FROM customers_products)
PIVOT
(COUNT(product_name) FOR product_name IN ('Orange', 'Apple', 'Palm', 'Apricot'));

-- Her ürünün kaç farklı müşteri tarafından alındığını göster
SELECT * FROM (SELECT customer_name, product_name FROM customers_products)
PIVOT
(COUNT(customer_name) FOR customer_name IN ('Mark', 'Amy', 'Adem', 'John'));

-- product_id bazında toplam id değeri
SELECT * FROM (SELECT product_id, product_name FROM customers_products)
PIVOT
(SUM(product_id) FOR product_id IN (10, 20, 30, 40));

-- product_id bazında sayım
SELECT * FROM (SELECT product_id, product_name FROM customers_products)
PIVOT
(COUNT(product_id) FOR product_id IN (10, 20, 30, 40));
```

---

## 🔵 DISTINCT {#distinct}

`DISTINCT` tekrar eden kayıtları filtreler, benzersiz değerleri gösterir.

```sql
-- Tekrarsız ürün adları
SELECT DISTINCT product_name
FROM customers_products;

-- Kaç farklı ürün var?
SELECT COUNT(DISTINCT product_name) AS meyve_cesit_sayisi
FROM customers_products;
```

---

## 🔧 ALTER TABLE {#alter-table}

`ALTER TABLE` mevcut bir tablonun yapısını değiştirmek için kullanılır.

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
```

### 1) Yeni Sütun Ekleme

```sql
-- Tek sütun ekle
ALTER TABLE employees
ADD gender varchar2(20);

-- DEFAULT değerli sütun ekle
ALTER TABLE employees
ADD country varchar2(50) DEFAULT 'The USA';
-- Mevcut kayıtlar otomatik 'The USA' olur

-- Aynı anda birden fazla sütun ekle
ALTER TABLE employees
ADD (number_of_kid number(2),
     marital_status varchar2(30) DEFAULT 'single'
    );
```

### 2) Sütun Silme

```sql
ALTER TABLE employees
DROP COLUMN country;
```

### 3) Sütun Adını Değiştirme

```sql
ALTER TABLE employees
RENAME COLUMN gender TO gender_male_or_female;
```

### 4) Tablo Adını Değiştirme

```sql
ALTER TABLE employees
RENAME TO workers;

SELECT * FROM workers;  -- Artık workers adıyla erişilir
```

### 5) Sütun Yapısını Değiştirme

```sql
-- Tek sütun
ALTER TABLE workers
MODIFY id number(9) NOT NULL;

-- Birden fazla sütun
ALTER TABLE workers
MODIFY (state char(45) NOT NULL,
        company char(30)
       );
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
```

**Sorular:**

1. Kaç farklı state var? (DISTINCT ile)
2. employees tablosuna `email varchar2(100)` sütunu ekleyin
3. employees tablosuna `hire_date date DEFAULT SYSDATE` sütunu ekleyin
4. `email` sütununu silin
5. Tablo adını `staff` olarak değiştirin
6. `id` sütununu NOT NULL yapın

```sql
-- Çözümler:

-- 1)
SELECT COUNT(DISTINCT state) AS different_states FROM employees;

-- 2)
ALTER TABLE employees ADD email varchar2(100);

-- 3)
ALTER TABLE employees ADD hire_date date DEFAULT SYSDATE;

-- 4)
ALTER TABLE employees DROP COLUMN email;

-- 5)
ALTER TABLE employees RENAME TO staff;

-- 6)
ALTER TABLE staff MODIFY id number(9) NOT NULL;
```

---

*📌 Sonraki ders: Genel Tekrar & İleri Düzey Sorgular*

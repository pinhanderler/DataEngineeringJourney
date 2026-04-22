# 🗄️ Gün 4 — ORDER BY, ALIASES, GROUP BY & HAVING

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [IS NULL / IS NOT NULL](#null)
2. [ORDER BY](#order-by)
3. [ALIASES (AS)](#aliases)
4. [GROUP BY](#group-by)
5. [Aggregate Fonksiyonlar](#aggregate)
6. [HAVING](#having)
7. [Alıştırmalar](#alıştırmalar)

---

## 🔲 IS NULL / IS NOT NULL {#null}

`IS NULL` → Boş (veri girilmemiş) satırları seçer
`IS NOT NULL` → Boş olmayan satırları seçer

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
INSERT INTO customers_products(product_id, product_name) VALUES(30, 'Apricot');
-- ↑ customer_name girilmedi, NULL kalacak

-- Müşteri ismi girilmemiş satırları getir
SELECT *
FROM customers_products
WHERE customer_name IS NULL;

-- Müşteri ismi boş olmayan satırları getir
SELECT *
FROM customers_products
WHERE customer_name IS NOT NULL;

-- IS NULL ile UPDATE kullanımı
UPDATE customers_products
SET customer_name = 'Isim girilmemis'
WHERE customer_name IS NULL;

-- NULL olan satırın product_name'ini güncelle
UPDATE customers_products
SET product_name = 'Watermelon'
WHERE customer_name IS NULL;
```

---

## ↕️ ORDER BY {#order-by}

`ORDER BY` verileri belirli bir alana göre sıralar.

```sql
-- product_name'e göre doğal sıra (A-Z)
SELECT *
FROM customers_products
ORDER BY product_name;

-- customer_name'i 'Mark' olan verileri product_id'ye göre sırala
SELECT *
FROM customers_products
WHERE customer_name = 'Mark'
ORDER BY product_id;

-- Alan numarası da kullanılabilir (1. sütun = product_id)
SELECT *
FROM customers_products
WHERE customer_name = 'Mark'
ORDER BY 1;

-- Büyükten küçüğe (DESC = Descending)
SELECT *
FROM customers_products
ORDER BY product_id DESC;

-- Çoklu sıralama: product_name büyükten küçüğe, customer_name A-Z
SELECT *
FROM customers_products
ORDER BY product_name DESC, customer_name ASC;
```

> **Not:** Varsayılan sıralama `ASC` (küçükten büyüğe)'dir. `ORDER BY product_name` = `ORDER BY product_name ASC`

---

## 🏷️ ALIASES (AS) {#aliases}

`AS` komutu, sütun adlarını farklı görüntülemek için kullanılır. **Tablodaki gerçek sütun adları değişmez**, sadece raporda farklı görünür.

```sql
-- Sütun isimlerini Türkçe göster
SELECT product_id AS urun_kodu,
       customer_name AS musteri_ismi,
       product_name AS urun_ismi
FROM customers_products;

-- İki sütunu tek sütunda birleştir ve alias ver
SELECT customer_name AS musteri_ismi,
       product_id || product_name AS urun_kodu_ismi
FROM customers_products;
```

---

## 📊 GROUP BY {#group-by}

`GROUP BY` verileri belirli bir alana göre gruplar.

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

-- Her ürünü alan müşteri sayısı
SELECT product_name, COUNT(product_name) AS number_of_customers
FROM customers_products
GROUP BY product_name;

-- Her product_id'nin kaç kez kullanıldığı
SELECT product_id, COUNT(product_id) AS number_of_usage
FROM customers_products
GROUP BY product_id;

-- Her çalışanın toplam maaşı
SELECT name, SUM(salary) AS total_salary
FROM employees
GROUP BY name;

-- Her state'deki çalışan sayısı
SELECT state, COUNT(name) AS total_worker
FROM employees
GROUP BY state;

-- Maaşı 2000'den fazla olan çalışan sayısı (şirket bazında)
SELECT company, COUNT(name) AS number_of_employees
FROM employees
WHERE salary > 2000
GROUP BY company;

-- Her şirketteki min ve max maaş
SELECT company, MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employees
GROUP BY company;
```

---

## 🔢 Aggregate Fonksiyonlar {#aggregate}

| Fonksiyon | Açıklama |
|-----------|----------|
| `COUNT()` | Kayıt sayısını döndürür |
| `SUM()` | Toplam değeri döndürür |
| `AVG()` | Ortalama değeri döndürür |
| `MIN()` | En küçük değeri döndürür |
| `MAX()` | En büyük değeri döndürür |

```sql
-- En yüksek maaş
SELECT MAX(salary) AS max_salary FROM employees;

-- En düşük maaş
SELECT MIN(salary) AS min_salary FROM employees;

-- En yüksek maaşlı çalışanın tüm bilgileri (SUBQUERY)
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- En düşük maaşlı çalışanın tüm bilgileri
SELECT *
FROM employees
WHERE salary = (SELECT MIN(salary) FROM employees);

-- İkinci en yüksek maaş
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- İkinci en düşük maaş
SELECT MIN(salary)
FROM employees
WHERE salary > (SELECT MIN(salary) FROM employees);
```

---

## 🔒 HAVING {#having}

`HAVING`, `GROUP BY`'dan sonra aggregate fonksiyonlarla filtreleme yapmak için kullanılır.

> **Not:** `WHERE` satırları filtreler. `HAVING` grupları filtreler.

```sql
-- Min maaşı 2000'den fazla olan şirketleri göster
SELECT company, MIN(salary) AS min_salary, MAX(salary) AS max_salary
FROM employees
GROUP BY company
HAVING MIN(salary) > 2000;

-- Toplam geliri 2500'den fazla olan çalışanları göster
SELECT name, SUM(salary) AS total_income
FROM employees
GROUP BY name
HAVING SUM(salary) > 2500;

-- Çalışan sayısı 1'den fazla olan state'leri göster
SELECT state, COUNT(name) AS number_of_employees
FROM employees
GROUP BY state
HAVING COUNT(name) > 1;

-- Max maaşı 3000'den az olan state'leri göster
SELECT state, MAX(salary) AS max_salary
FROM employees
GROUP BY state
HAVING MAX(salary) < 3000;
```

### WHERE vs HAVING

```sql
-- WHERE: GROUP BY'dan ÖNCE filtreler
SELECT company, COUNT(name) AS number_of_employees
FROM employees
WHERE salary > 2000       -- ← önce maaşı 2000'den fazla olanları filtrele
GROUP BY company;

-- HAVING: GROUP BY'dan SONRA filtreler
SELECT company, COUNT(name) AS number_of_employees
FROM employees
GROUP BY company
HAVING COUNT(name) > 1;   -- ← sonra çalışan sayısı 1'den fazla olanları filtrele
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

Aşağıdaki tabloyu kullanarak soruları cevaplayın:

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

1. Verileri maaşa göre büyükten küçüğe sıralayın
2. IBM ve GOOGLE'daki çalışanların adını `name` sütununu `employee_name` alias'ıyla getirin
3. Her çalışanın toplam maaşını hesaplayın
4. Her state'deki ortalama maaşı hesaplayın
5. Ortalama maaşı 2000'den fazla olan şirketleri listeleyin
6. IBM'de çalışan sayısını getirin
7. En yüksek maaşlı çalışanın tüm bilgilerini getirin (SUBQUERY kullanın)
8. İkinci en yüksek maaşı getirin

```sql
-- Çözümler:

-- 1)
SELECT * FROM employees ORDER BY salary DESC;

-- 2)
SELECT name AS employee_name
FROM employees
WHERE company IN ('IBM', 'GOOGLE');

-- 3)
SELECT name, SUM(salary) AS total_salary
FROM employees
GROUP BY name;

-- 4)
SELECT state, AVG(salary) AS avg_salary
FROM employees
GROUP BY state;

-- 5)
SELECT company, AVG(salary) AS avg_salary
FROM employees
GROUP BY company
HAVING AVG(salary) > 2000;

-- 6)
SELECT COUNT(name) AS ibm_employees
FROM employees
WHERE company = 'IBM';

-- 7)
SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- 8)
SELECT MAX(salary)
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

---

*📌 Sonraki ders: UNION, INTERSECT, MINUS, JOINS*

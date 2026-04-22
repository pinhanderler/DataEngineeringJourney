# 🗄️ Gün 6 — EXISTS, BETWEEN, IS NULL & Wildcards

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [EXISTS Komutu](#exists)
2. [BETWEEN](#between)
3. [NOT BETWEEN](#not-between)
4. [Wildcards (%, _, [ ])](#wildcards)
5. [NOT LIKE](#not-like)
6. [REGEXP_LIKE](#regexp)
7. [Alıştırmalar](#alıştırmalar)

---

## ✅ EXISTS Komutu {#exists}

`EXISTS` komutu **SUBQUERY'ler ile** birlikte kullanılır. Bir subquery'nin sonuç döndürüp döndürmediğini kontrol eder.

> **Önemli Notlar:**
> - `IN` komutu `OR` komutunun yazılmış halidir
> - `IN` komutunu tek başına subquery'lerle kullanmayız
> - Subquery kullanacaksanız `EXISTS` kullanın

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
INSERT INTO customers_products VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');

CREATE TABLE customers_likes
(
  product_id number(10),
  customer_name varchar2(50),
  liked_product varchar2(50)
);

INSERT INTO customers_likes VALUES (10, 'Mark', 'Orange');
INSERT INTO customers_likes VALUES (50, 'Mark', 'Pineapple');
INSERT INTO customers_likes VALUES (60, 'John', 'Avocado');
INSERT INTO customers_likes VALUES (20, 'Mark', 'Apple');
INSERT INTO customers_likes VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_likes VALUES (40, 'John', 'Apricot');

-- Product_id'leri aynı olan müşterilerin isimlerini getir
SELECT customer_name
FROM customers_products
WHERE EXISTS (SELECT product_id
              FROM customers_likes
              WHERE customers_products.product_id = customers_likes.product_id);

-- product_name ile liked_product'ı aynı olan müşterilerin isimlerini getir
SELECT customer_name
FROM customers_products
WHERE EXISTS (SELECT liked_product
              FROM customers_likes
              WHERE customers_products.product_name = customers_likes.liked_product);
```

---

## ↔️ BETWEEN {#between}

`BETWEEN` iki değer arasındaki verileri getirir. **Sınırlar dahildir.**

```sql
-- product_id'si 20 ile 40 arasında olanlar
SELECT product_name, product_id
FROM customers_products
WHERE product_id BETWEEN 20 AND 40;

-- Aynı sorgu AND ile:
SELECT product_name, product_id
FROM customers_products
WHERE product_id >= 20 AND product_id <= 40;

-- Harfler için BETWEEN (J'den T'ye kadar isimler)
SELECT *
FROM customers_products
WHERE customer_name BETWEEN 'J' AND 'T';
```

> ⚠️ **BETWEEN kullanırken ilk değerin ikinciden küçük olmasına dikkat edin!**

---

## ❌ NOT BETWEEN {#not-between}

`NOT BETWEEN` ile sınırlar **dahil olmaz**.

```sql
-- product_id 20 ile 40 arasında OLMAYAN ürünler
SELECT *
FROM customers_products
WHERE product_id NOT BETWEEN 20 AND 40;

-- Aynı sorgu AND ile:
SELECT *
FROM customers_products
WHERE product_id < 20 OR product_id > 40;

-- İlk harfi M'den S'ye kadar olmayan ürünler
SELECT *
FROM customers_products
WHERE product_name NOT BETWEEN 'M' AND 'S';
```

---

## 🃏 Wildcards (Joker Karakterler) {#wildcards}

### 1) `%` — Sıfır veya daha fazla karakter

```sql
CREATE TABLE customers
(
  customer_id number(10) UNIQUE,
  customer_name varchar2(50) NOT NULL,
  income number(6)
);

INSERT INTO customers VALUES (1001, 'John', 62000);
INSERT INTO customers VALUES (1002, 'Jane', 57500);
INSERT INTO customers VALUES (1003, 'Brad', 71000);
INSERT INTO customers VALUES (1004, 'Manse', 42000);
INSERT INTO customers VALUES (1005, 'Can', 57500);
INSERT INTO customers VALUES (1006, 'Cin', 71000);
INSERT INTO customers VALUES (1007, 'Con', 42000);

-- J ile başlayan isimler
SELECT * FROM customers WHERE customer_name LIKE 'J%';

-- e ile biten isimler
SELECT customer_name, income FROM customers WHERE customer_name LIKE '%e';

-- İçinde n olan isimler
SELECT customer_name, income FROM customers WHERE customer_name LIKE '%n%';
```

### 2) `_` — Sadece 1 karakter

```sql
-- 4 harfli, son 3 harfi 'ohn' olan isimler → John
SELECT customer_name, income FROM customers WHERE customer_name LIKE '_ohn';

-- 4 harfli, son 2 harfi 'ne' olan isimler → Jane, Manse değil (5 harf)
SELECT customer_name, income FROM customers WHERE customer_name LIKE '__ne';

-- 4 harfli, 3. harfi 'n' olan isimler
SELECT customer_name, income FROM customers WHERE customer_name LIKE '__n_';

-- 2. harfi 'a' olan isimler
SELECT customer_name, income FROM customers WHERE customer_name LIKE '_a%';

-- 3. harfi 'n' olan en az 5 harfli isimler
SELECT customer_name, income FROM customers WHERE customer_name LIKE '__n__%';

-- B ile başlayıp 3. harfi a olan isimler → Brad
SELECT customer_name, income FROM customers WHERE customer_name LIKE 'B_a%';
```

### 3) `[ ]` — REGEXP_LIKE ile karakter sınıfı {#regexp}

```sql
-- İlk harfi C, son harfi n, 2. harfi a veya i olan 3 harfli isimler (Can, Cin)
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, 'C[ai]n');

-- İlk harfi C, son harfi n, 2. harfi a'dan k'ya olan 3 harfli isimler
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, 'C[a-k]n');

-- İçinde a veya n olan isimler
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, '[an](*)');

-- J veya M ile başlayan isimler
SELECT customer_name, income
FROM customers
WHERE REGEXP_LIKE(customer_name, '^[JM](*)');
```

---

## 🚫 NOT LIKE {#not-like}

```sql
-- J ile başlamayan isimler
SELECT customer_name, income FROM customers WHERE customer_name NOT LIKE 'J%';

-- a içermeyen isimler
SELECT customer_name, income FROM customers WHERE customer_name NOT LIKE '%a%';

-- 2. harfi a olmayan isimler
SELECT customer_name, income FROM customers WHERE customer_name NOT LIKE '_a%';
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

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
INSERT INTO customers_products VALUES (20, 'Mark', 'Apple');
INSERT INTO customers_products VALUES (10, 'Adem', 'Orange');
INSERT INTO customers_products VALUES (40, 'John', 'Apricot');
INSERT INTO customers_products VALUES (20, 'Eddie', 'Apple');
```

**Sorular:**

1. product_id'si 10 ile 30 arasında olan ürünlerin adını ve id'sini getirin (BETWEEN)
2. product_id'si 10 ile 30 arasında OLMAYAN ürünlerin tüm bilgilerini getirin (NOT BETWEEN)
3. customer_name'i 'M' ile başlayan müşterileri getirin
4. product_name'i 'A' ile başlayıp 'e' ile biten ürünleri getirin (Apple, Apricot dahil mi?)
5. İsmi 4 harfli olan müşterileri getirin

```sql
-- Çözümler:

-- 1)
SELECT product_name, product_id
FROM customers_products
WHERE product_id BETWEEN 10 AND 30;

-- 2)
SELECT *
FROM customers_products
WHERE product_id NOT BETWEEN 10 AND 30;

-- 3)
SELECT * FROM customers_products WHERE customer_name LIKE 'M%';

-- 4)
SELECT * FROM customers_products WHERE product_name LIKE 'A%e';

-- 5)
SELECT * FROM customers_products WHERE customer_name LIKE '____';
```

---

*📌 Sonraki ders: PIVOT, DISTINCT, ALTER TABLE*

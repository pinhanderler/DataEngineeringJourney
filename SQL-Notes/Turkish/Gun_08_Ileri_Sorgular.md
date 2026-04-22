# 🗄️ Gün 8 — İleri Düzey Sorgular & ROWNUM

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [ROWNUM ile Sıralı Sorgular](#rownum)
2. [OFFSET FETCH ile Sayfalama](#offset)
3. [MOD Fonksiyonu](#mod)
4. [Subquery İleri Düzey](#subquery-advanced)
5. [String Fonksiyonları](#string-functions)
6. [Alıştırmalar](#alıştırmalar)

---

## 🔢 ROWNUM ile Sıralı Sorgular {#rownum}

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

-- En yüksek maaş dışındaki çalışanları büyükten küçüğe sırala
SELECT *
FROM employees
WHERE salary != (SELECT MAX(salary) FROM employees)
ORDER BY salary DESC;

-- İkinci en yüksek maaşlı çalışanın tüm bilgileri
-- Yol 1: ROWNUM ile
SELECT *
FROM (SELECT *
      FROM employees
      WHERE salary != (SELECT MAX(salary) FROM employees)
      ORDER BY salary DESC)
WHERE ROWNUM = 1;
```

---

## 📄 OFFSET FETCH ile Sayfalama {#offset}

```sql
-- İkinci en yüksek maaşlı çalışanın bilgileri
-- Yol 2: OFFSET FETCH ile
SELECT *
FROM employees
ORDER BY salary DESC
OFFSET 1 ROW
FETCH NEXT 1 ROW ONLY;

-- İlk 3 en yüksek maaşlı çalışan
SELECT name, salary
FROM employees
ORDER BY salary DESC
FETCH FIRST 3 ROWS ONLY;
```

---

## ➗ MOD Fonksiyonu {#mod}

`MOD(n, m)` → n sayısının m'ye bölümünden kalanı döndürür.

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

-- ID'si çift sayı olan öğrenciler
SELECT *
FROM students
WHERE MOD(id, 2) = 0;

-- ID'si tek sayı olan öğrenciler
SELECT *
FROM students
WHERE MOD(id, 2) = 1;

-- Tabloda kaç kayıt var?
SELECT COUNT(*) AS num_of_records
FROM students;

-- Kaç farklı state var?
SELECT COUNT(DISTINCT state) AS num_of_states
FROM students;
```

---

## 🔍 Subquery İleri Düzey {#subquery-advanced}

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

-- En yüksek maaşlı çalışan (SUBQUERY)
SELECT *
FROM workers01
WHERE salary = (SELECT MAX(salary) FROM workers01);

-- En düşük maaşlı çalışan (SUBQUERY)
SELECT *
FROM workers01
WHERE salary = (SELECT MIN(salary) FROM workers01);

-- İkinci en yüksek maaş
SELECT MAX(salary)
FROM workers01
WHERE salary < (SELECT MAX(salary) FROM workers01);

-- İkinci en düşük maaş
SELECT MIN(salary)
FROM workers01
WHERE salary > (SELECT MIN(salary) FROM workers01);
```

---

## 🔠 String Fonksiyonları {#string-functions}

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

-- LOWER: tüm harfleri küçük yap
-- UPPER: tüm harfleri büyük yap
-- INITCAP: her kelimenin ilk harfini büyük yap
SELECT INITCAP(name), UPPER(title), LOWER(name)
FROM workers;

-- Sonuç:
-- INITCAP('ali can')   → Ali Can
-- UPPER('sdet')        → SDET
-- LOWER('ALI CAN')     → ali can
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

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
```

**Sorular:**

1. En yüksek maaşlı çalışanın tüm bilgilerini getirin
2. En düşük maaşlı çalışanın tüm bilgilerini getirin
3. İkinci en yüksek maaşı getirin
4. İkinci en düşük maaşı getirin
5. ID'si çift olan çalışanları getirin
6. İlk 3 en yüksek maaşlı çalışanı getirin (OFFSET FETCH)
7. Tüm isimleri büyük harf, tüm state'leri küçük harf yapın

```sql
-- Çözümler:

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
```

---

*📌 Sonraki ders: Genel Tekrar & Kapsamlı Alıştırmalar*

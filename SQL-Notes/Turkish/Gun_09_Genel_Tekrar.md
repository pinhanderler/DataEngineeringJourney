# 🗄️ Gün 9 — Genel Tekrar & Kapsamlı Alıştırmalar

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 Tüm Konuların Özeti

---

## 📋 SQL Komutları Hızlı Referans

### DDL (Data Definition Language)
```sql
CREATE TABLE tablo_adi (sütun tip, ...);
ALTER TABLE tablo_adi ADD sütun tip;
ALTER TABLE tablo_adi DROP COLUMN sütun;
ALTER TABLE tablo_adi RENAME COLUMN eski TO yeni;
ALTER TABLE tablo_adi RENAME TO yeni_isim;
ALTER TABLE tablo_adi MODIFY sütun tip kısıt;
DROP TABLE tablo_adi;
DROP TABLE tablo_adi PURGE;
TRUNCATE TABLE tablo_adi;
```

### DML (Data Manipulation Language)
```sql
INSERT INTO tablo VALUES (...);
INSERT INTO tablo (sütun1, sütun2) VALUES (...);
UPDATE tablo SET sütun = değer WHERE koşul;
DELETE FROM tablo WHERE koşul;
```

### DQL (Data Query Language)
```sql
SELECT * FROM tablo;
SELECT sütun1, sütun2 FROM tablo WHERE koşul;
SELECT * FROM tablo ORDER BY sütun [ASC|DESC];
SELECT sütun, COUNT(*) FROM tablo GROUP BY sütun;
SELECT sütun, COUNT(*) FROM tablo GROUP BY sütun HAVING koşul;
```

### Set Operasyonları
```sql
-- Birleşim (tekrarsız)
sorgu1 UNION sorgu2;

-- Birleşim (tekrarlı)
sorgu1 UNION ALL sorgu2;

-- Kesişim
sorgu1 INTERSECT sorgu2;

-- Fark
sorgu1 MINUS sorgu2;
```

### JOIN'ler
```sql
-- Ortak kayıtlar
FROM tablo1 INNER JOIN tablo2 ON koşul;

-- Sol tablo tümü
FROM tablo1 LEFT JOIN tablo2 ON koşul;

-- Sağ tablo tümü
FROM tablo1 RIGHT JOIN tablo2 ON koşul;

-- Her iki tablo tümü
FROM tablo1 FULL JOIN tablo2 ON koşul;

-- Kendi kendine
FROM tablo t1 INNER JOIN tablo t2 ON t1.sütun = t2.sütun;
```

---

## 🔍 Özel Operatörler

```sql
-- Aralık kontrolü
WHERE sütun BETWEEN değer1 AND değer2;
WHERE sütun NOT BETWEEN değer1 AND değer2;

-- Liste kontrolü
WHERE sütun IN (değer1, değer2, değer3);
WHERE sütun NOT IN (değer1, değer2, değer3);

-- Boş değer kontrolü
WHERE sütun IS NULL;
WHERE sütun IS NOT NULL;

-- Desen eşleşmesi
WHERE sütun LIKE 'J%';        -- J ile başlayan
WHERE sütun LIKE '%e';        -- e ile biten
WHERE sütun LIKE '%an%';      -- an içeren
WHERE sütun LIKE '_ohn';      -- 4 harfli, son 3 harfi 'ohn'
WHERE sütun NOT LIKE 'J%';    -- J ile başlamayan

-- Alt sorgu ile
WHERE EXISTS (SELECT ... FROM ... WHERE ...);
```

---

## 📊 Aggregate Fonksiyonlar

```sql
COUNT(*)         -- Toplam kayıt sayısı
COUNT(sütun)     -- NULL olmayan kayıt sayısı
SUM(sütun)       -- Toplam
AVG(sütun)       -- Ortalama
MIN(sütun)       -- Minimum
MAX(sütun)       -- Maksimum
```

---

## 🎯 Kapsamlı Alıştırmalar

Aşağıdaki tabloları oluşturun ve soruları cevaplayın:

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

### Bölüm A — Temel Sorgular

1. Tüm çalışanları maaşa göre büyükten küçüğe sıralayın
2. Texas'ta çalışan ve maaşı 2000'den fazla olan çalışanları getirin
3. IBM veya GOOGLE'da çalışanların adını getirin (IN kullanın)
4. Maaşı 1500 ile 3000 arasındaki çalışanları getirin (BETWEEN)
5. Adı 'Brad' ile başlayan çalışanları getirin (LIKE)

```sql
-- Çözümler:
-- 1) SELECT * FROM employees ORDER BY salary DESC;
-- 2) SELECT * FROM employees WHERE state = 'Texas' AND salary > 2000;
-- 3) SELECT name FROM employees WHERE company IN ('IBM', 'GOOGLE');
-- 4) SELECT * FROM employees WHERE salary BETWEEN 1500 AND 3000;
-- 5) SELECT * FROM employees WHERE name LIKE 'Brad%';
```

### Bölüm B — Gruplama ve Aggregate

1. Her şirketteki çalışan sayısını getirin
2. Her şirketteki ortalama maaşı getirin
3. Ortalama maaşı 2000'den fazla olan şirketleri listeleyin
4. Her state'deki toplam maaş ödemesini getirin
5. En az 2 çalışanı olan state'leri listeleyin

```sql
-- Çözümler:
-- 1) SELECT company, COUNT(*) AS emp_count FROM employees GROUP BY company;
-- 2) SELECT company, AVG(salary) AS avg_salary FROM employees GROUP BY company;
-- 3) SELECT company, AVG(salary) AS avg_salary FROM employees GROUP BY company HAVING AVG(salary) > 2000;
-- 4) SELECT state, SUM(salary) AS total_salary FROM employees GROUP BY state;
-- 5) SELECT state, COUNT(*) AS emp_count FROM employees GROUP BY state HAVING COUNT(*) >= 2;
```

### Bölüm C — Subquery ve JOIN

1. 15000'den fazla çalışanı olan şirketlerdeki çalışanları getirin (Subquery)
2. En yüksek maaşlı çalışanın tüm bilgilerini getirin
3. İkinci en yüksek maaşı getirin
4. companies ve employees tablolarını birleştirerek her çalışanın şirket çalışan sayısını getirin (JOIN)

```sql
-- Çözümler:
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

### Bölüm D — Set Operasyonları

1. Maaşı 3000'den fazla VEYA 1500'den az olan çalışanların adlarını tekrarsız getirin (UNION)
2. IBM veya GOOGLE'da çalışıp maaşı 2500'den fazla olan ortak isimleri getirin (INTERSECT)
3. Florida'da çalışmayıp maaşı 2000'den az olanları getirin (MINUS)

```sql
-- Çözümler:
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

**Soru 1:** Aşağıdaki sorgular arasındaki fark nedir?
```sql
-- A)
SELECT * FROM employees WHERE salary > 2000;
GROUP BY company;

-- B)
SELECT company, COUNT(*) FROM employees
WHERE salary > 2000
GROUP BY company;

-- C)
SELECT company, COUNT(*) FROM employees
GROUP BY company
HAVING COUNT(*) > 2;
```

> **Cevap:** A yanlış syntax. B, maaşı 2000'den fazla olanları filtreler sonra şirkete göre gruplar. C, önce şirkete göre gruplar sonra çalışan sayısı 2'den fazla olanları filtreler.

---

**Soru 2:** JOIN türlerini açıklayın.

> **Cevap:**
> - **INNER JOIN:** İki tabloda ortak olan kayıtlar
> - **LEFT JOIN:** Sol tablonun tümü + sağ tablodan eşleşenler (eşleşmeyenler NULL)
> - **RIGHT JOIN:** Sağ tablonun tümü + sol tablodan eşleşenler (eşleşmeyenler NULL)
> - **FULL JOIN:** Her iki tablonun tümü (eşleşmeyenler NULL)
> - **SELF JOIN:** Tablonun kendisiyle birleşimi

---

**Soru 3:** DELETE, TRUNCATE ve DROP arasındaki farkları bir tablo ile gösterin.

| Özellik | DELETE | TRUNCATE | DROP |
|---------|--------|----------|------|
| WHERE kullanımı | ✅ | ❌ | ❌ |
| Rollback | ✅ | ❌ | ❌ |
| Tablo yapısı | Kalır | Kalır | Silinir |
| Hız | Yavaş | Hızlı | Hızlı |

---

🎉 **Tebrikler! SQL kursunu tamamladınız!**

*Daha fazla pratik için: www.w3schools.com, https://sqlbolt.com/, https://www.sqlteaching.com/*

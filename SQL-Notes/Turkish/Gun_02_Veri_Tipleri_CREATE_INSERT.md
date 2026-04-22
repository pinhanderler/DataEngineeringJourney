# 🗄️ Gün 2 — SQL Veri Tipleri, Tablo Oluşturma & Veri Ekleme

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [SQL Nedir?](#sql-nedir)
2. [SQL'in Alt Dilleri](#alt-diller)
3. [SQL Veri Tipleri](#veri-tipleri)
4. [Tablo Oluşturma (CREATE TABLE)](#create-table)
5. [NOT NULL Kısıtı](#not-null)
6. [PRIMARY KEY Ekleme](#primary-key)
7. [FOREIGN KEY Ekleme](#foreign-key)
8. [Veri Ekleme (INSERT INTO)](#insert-into)
9. [INSERT ALL](#insert-all)
10. [Alıştırmalar](#alıştırmalar)

---

## 🔷 SQL Nedir? {#sql-nedir}

**SQL = Structured Query Language (Yapısal Sorgu Dili)**

SQL, **İlişkisel Veritabanı Yönetim Sistemleri (RDBMS)** ile etkileşim kurmak için kullanılan bir dildir.

SQL kullanarak şunları yapabiliriz:
1. Veritabanları oluşturma ve yönetme
2. Veritabanı tabloları tasarlama
3. Veri oluşturma, okuma, güncelleme ve silme **(CRUD)**
4. Güvenlik, kullanıcı yönetimi gibi yönetimsel görevler

> **Not:** SQL tüm RDBMS sistemlerde (MySQL, SQL Server, PostgreSQL, Oracle) kullanılabilir. Konseptler aynıdır ancak uygulama küçük farklılıklar gösterebilir.

---

## 📋 SQL'in Alt Dilleri {#alt-diller}

SQL, 4 farklı dilin kombinasyonudur:

| Kısaltma | Açılım | Kullanım |
|----------|--------|----------|
| **DCL** | Data Control Language | Veritabanı yetkilerini kontrol eder, kullanıcı ve izin yönetimi |
| **DDL** | Data Definition Language | Tablo, sütun gibi veritabanı nesnelerinin yapısını tanımlar |
| **DML** | Data Manipulation Language | Veriyi işler: INSERT, UPDATE, DELETE |
| **DQL** | Data Query Language | Veritabanından veri sorgular: SELECT |

---

## 📦 SQL Veri Tipleri {#veri-tipleri}

### String (Metin) Veri Tipleri

| Veri Tipi | Açıklama |
|-----------|----------|
| `char(size)` | Sabit uzunluklu metin. Maks. 2000 byte. SSN, ZipCode gibi sabit uzunluklu veriler için ideal |
| `nchar(size)` | Sabit uzunluklu Unicode metin. Farklı dillerdeki veriler için kullanılır |
| `varchar2(size)` | Değişken uzunluklu metin. Maks. 4000 byte |
| `nvarchar2(size)` | Değişken uzunluklu Unicode metin. Maks. 8000 byte |

```sql
-- Örnek: char vs varchar2
-- "ab" değeri için:
-- char(4)    → 'ab  ' (4 byte kullanır)
-- varchar2(4)→ 'ab'   (2 byte kullanır)
```

### Sayısal Veri Tipleri

| Veri Tipi | Açıklama |
|-----------|----------|
| `number(p, s)` | Sayısal veri. p=precision (toplam basamak), s=scale (ondalık basamak) |

```sql
-- Örnekler:
number(5, 2)  → 123.45      (3 tam + 2 ondalık)
number(7)     → 1234567     (ölçek sıfır)
number(7, -2) → 1234600     (yüzlere yuvarlar)
number(4, 2)  → 12.34       -- 123.45 hata verir! (precision aşıldı)
```

### Tarih Veri Tipi

| Veri Tipi | Açıklama |
|-----------|----------|
| `DATE` | Tarih ve saat bilgisini saniye hassasiyetiyle saklar. Standart format: `dd-MMM-yy` |

```sql
-- Tarih formatını değiştirme:
ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD';
-- Artık: 2020-04-13
```

### BLOB Veri Tipi

| Veri Tipi | Açıklama |
|-----------|----------|
| `BLOB` | Binary Large Objects. Resim, ses, video gibi dijital veriler için |

---

## 🏗️ Tablo Oluşturma (CREATE TABLE) {#create-table}

### Yöntem 1: Sıfırdan Tablo Oluşturma

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

### Yöntem 2: Mevcut Tablodan Tablo Oluşturma

```sql
-- students tablosundan sadece id ve name sütunlarıyla yeni tablo
CREATE TABLE studentsIdName AS
SELECT id, name
FROM students;
```

---

## 🚫 NOT NULL Kısıtı {#not-null}

`NOT NULL`, bir sütunun boş değer kabul etmemesini sağlar.

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50) NOT NULL,   -- ← name boş olamaz
  grade number(2),
  address varchar2(100),
  last_modification date
);

-- NOT NULL olan sütunu atlarsak HATA alırız:
INSERT INTO students(id, grade) VALUES(123456789, 11);
-- ORA-01400: cannot insert NULL into "STUDENTS"."NAME"
```

---

## 🔑 PRIMARY KEY Ekleme {#primary-key}

### Yöntem 1: Sütun yanına yazma

```sql
CREATE TABLE students
(
  id number(9) PRIMARY KEY,    -- ← primary key burada
  name varchar2(50) NOT NULL,
  grade number(2),
  address varchar2(100),
  last_modification date
);
```

### Yöntem 2: CONSTRAINT ile isimlendirme

```sql
CREATE TABLE students
(
  id number(9),
  name varchar2(50) NOT NULL,
  grade number(2),
  address varchar2(100),
  last_modification date,
  CONSTRAINT id_pk PRIMARY KEY(id)   -- ← isimli constraint
);
```

---

## 🔗 FOREIGN KEY Ekleme {#foreign-key}

```sql
-- Parent Table (Üst Tablo)
CREATE TABLE students
(
  id number(9) PRIMARY KEY,
  name varchar2(50),
  grade number(2),
  address varchar2(100),
  last_modification date
);

-- Child Table (Alt Tablo)
CREATE TABLE studentPhoneNumber
(
  studentId number(9),
  PhoneNumber varchar2(10),
  CONSTRAINT studentId_fk FOREIGN KEY(studentId) REFERENCES students(id)
);
```

> ⚠️ **Not 1:** Parent tabloda olmayan bir id ile Child tabloya veri ekleyemezsiniz!
> ⚠️ **Not 2:** Child tabloyu silmeden Parent tabloyu silemezsiniz!

### Composite Foreign Key

```sql
CREATE TABLE supplier
(
  supplier_id number(10) not null,
  supplier_name varchar2(50) not null,
  contact_name varchar2(50),
  CONSTRAINT supplier_pk PRIMARY KEY (supplier_id, supplier_name)
);

CREATE TABLE products
(
  product_id number(10),
  supplier_id number(10),
  supplier_name varchar2(50) not null,
  CONSTRAINT fk_supplier FOREIGN KEY (supplier_id, supplier_name)
                          REFERENCES supplier(supplier_id, supplier_name)
);
```

---

## ➕ Veri Ekleme (INSERT INTO) {#insert-into}

### Tüm Sütunlara Veri Ekleme

```sql
INSERT INTO students VALUES(123456789, 'John Walker', 11, '1234 W 12th TER Addison Texas 75001', '14-Apr-2020');
```

### Seçili Sütunlara Veri Ekleme

```sql
-- Sadece id ve name sütununa ekle, diğerleri NULL kalır
INSERT INTO students(id, name) VALUES(234567890, 'John Walker');
```

---

## 📥 INSERT ALL {#insert-all}

Birden fazla satırı tek seferde eklemek için:

```sql
-- Tek tabloya INSERT ALL
INSERT ALL
  INTO supplier (supplier_id, supplier_name) VALUES (1001, 'IBM')
  INTO supplier (supplier_id, supplier_name) VALUES (2002, 'Microsoft')
  INTO supplier (supplier_id, supplier_name) VALUES (3003, 'Google')
SELECT * FROM dual;
```

```sql
-- Birden fazla tabloya INSERT ALL
INSERT ALL
  INTO supplier (supplier_id, supplier_name) VALUES (4004, 'APPLE')
  INTO supplier (supplier_id, supplier_name) VALUES (5005, 'LINUX')
  INTO supplier (supplier_id, supplier_name) VALUES (6006, 'SAMSUNG')
  INTO products (supplier_id, product_id) VALUES (1001, 10011)
  INTO products (supplier_id, product_id) VALUES (2002, 20022)
SELECT * FROM dual;
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

### Alıştırma 1
`supplier_id`, `name`, `address` (street, city, state, zipcode ayrı sütunlar) bilgilerini saklayan **"suppliers"** tablosunu oluşturun.

```sql
-- Çözüm:
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

---

### Alıştırma 2
`suppliers` tablosunu kullanarak sadece `supplier_id` ve `name` sütunlarını içeren **"suppliers_id_name"** tablosunu oluşturun.

```sql
-- Çözüm:
CREATE TABLE suppliers_id_name AS
SELECT supplier_id, name
FROM suppliers;
```

---

### Alıştırma 3
`area_code` (PRIMARY KEY), `name`, `population`, `state` sütunlarını içeren **"cities"** tablosunu oluşturun. PRIMARY KEY'i 1. yöntemle ekleyin.

```sql
-- Çözüm:
CREATE TABLE cities
(
  area_code number(5) PRIMARY KEY,
  name varchar2(100) NOT NULL,
  population number(15),
  state varchar2(50)
);
```

---

### Alıştırma 4
`SSN`, `name`, `subject`, `gender` sütunlarını içeren **"teachers"** tablosunu oluşturun. PRIMARY KEY'i 2. yöntemle ekleyin.

```sql
-- Çözüm:
CREATE TABLE teachers
(
  SSN char(9),
  name varchar2(50) NOT NULL,
  subject varchar2(50),
  gender varchar2(10),
  CONSTRAINT teachers_pk PRIMARY KEY(SSN)
);
```

---

### Alıştırma 5
`supplier_id` (PRIMARY KEY), `supplier_name`, `contact_name` içeren **"supplier"** tablosu ve `supplier_id` (FOREIGN KEY), `product_id` içeren **"products"** tablosunu oluşturun.

```sql
-- Çözüm:
CREATE TABLE supplier
(
  supplier_id number(10) not null,
  supplier_name varchar2(50) not null,
  contact_name varchar2(50),
  CONSTRAINT supplier_pk PRIMARY KEY (supplier_id)
);

CREATE TABLE products
(
  supplier_id number(10),
  product_id number(10),
  CONSTRAINT fk_supplier FOREIGN KEY (supplier_id) REFERENCES supplier(supplier_id)
);
```

---

### Alıştırma 6
`SSN` = 234 43 1223, `name` = Jane Smith, `subject` = Mathematics, `gender` = female olan öğretmeni **teachers** tablosuna ekleyin.

```sql
-- Çözüm:
INSERT INTO teachers VALUES('234431223', 'Jane Smith', 'Mathematics', 'female');
```

---

### Alıştırma 7
`SSN` = 567 59 7624, `name` = Leo Mark olan öğretmeni sadece bu iki alanla **teachers** tablosuna ekleyin.

```sql
-- Çözüm:
INSERT INTO teachers(SSN, name) VALUES('567597624', 'Leo Mark');
```

---

*📌 Sonraki ders: UPDATE SET, DELETE, TRUNCATE, DROP, SELECT, WHERE*

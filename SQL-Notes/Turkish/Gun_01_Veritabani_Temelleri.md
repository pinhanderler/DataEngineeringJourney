# 🗄️ Gün 1 — Veritabanı Temelleri & SQL'e Giriş

> **TechProEd | SQL Tutoring Summer 2020**

---

## 📚 İçindekiler

1. [Veritabanı Nedir?](#veritabanı-nedir)
2. [Verinin Bilgisayarda Saklanmasının Avantajları](#avantajlar)
3. [Veritabanı Yönetim Sistemi (DBMS)](#dbms)
4. [Database Validation Testi](#validation)
5. [SQL Tabloları](#tablolar)
6. [İlişkisel Veritabanları](#ilişkisel)
7. [Popüler Veritabanları](#popüler)
8. [Non-Relational Veritabanları](#nosql)
9. [Primary Key](#primary-key)
10. [Foreign Key](#foreign-key)
11. [Composite Key](#composite-key)
12. [UNIQUE KEY vs PRIMARY KEY](#unique-vs-primary)
13. [Alıştırmalar](#alıştırmalar)

---

## 🔷 Veritabanı Nedir? {#veritabanı-nedir}

**Veritabanı**, birbiriyle ilişkili bilgilerin koleksiyonudur.

### Örnekler:
- 📞 Telefon rehberi
- ✅ Yapılacaklar listesi
- 👥 Facebook kullanıcı isimleri
- 🎓 Bir okuldaki öğrenci isimleri

Veriler farklı şekillerde saklanabilir: kağıt, bilgisayar hafızası, bulut vb.

---

## ✅ Verinin Bilgisayarda Saklanmasının Avantajları {#avantajlar}

| # | Avantaj |
|---|---------|
| 1 | Çok büyük miktarda veri saklanabilir |
| 2 | Oluşturma, Okuma, Güncelleme, Silme işlemleri kolaydır (CRUD) |
| 3 | Veriye erişim kolaydır |
| 4 | Hızlı erişim sağlanır |
| 5 | Güvenlik sağlanır |

---

## 🖥️ Veritabanı Yönetim Sistemi (DBMS) {#dbms}

**DBMS**, kullanıcıların aşağıdakileri yapmasına olanak tanıyan özel bir yazılım programıdır:

1. Veritabanına erişim
2. Oluşturma, Okuma, Güncelleme, Silme **(CRUD)**
3. Veritabanından raporlar alma
4. Veritabanına erişimi kontrol etme **(Güvenlik)**
5. Diğer uygulamalarla etkileşim kurma

---

## 🔐 Database Validation (Doğrulama) Testi {#validation}

```
Kullanıcı Arayüzü  ──────────►  API  ──────────►  Veritabanı
     (UI)                                              (DB)
```

Kullanıcı bir form doldurduğunda, veri UI'dan API'ye, oradan da veritabanına gider.
Test mühendisleri bu veri akışının doğru çalışıp çalışmadığını doğrular.

---

## 📊 SQL Tabloları {#tablolar}

Veritabanındaki veriler **tablo** formatında saklanır.

```
contactID | name           | company          | email
----------|----------------|------------------|---------------------------
    1     | Bill Gates     | Microsoft        | bill@XBoxOneRocks.com
    2     | Steve Jobs     | Apple            | steve@rememberNewton.com
    3     | Linus Torvalds | Linux Foundation | linus@gnuWho.org
    4     | Andy Harris    | Wiley Press      | andy@aharrisBooks.net
```

- **Satır (Row / Record):** Tek bir kayıt
- **Sütun (Column / Field):** Bir veri kategorisi

---

## 🔗 İlişkisel Veritabanları (SQL Databases) {#ilişkisel}

1. İlişkisel veritabanı, verileri **tablolarda** saklar
2. Her veri noktası arasındaki ilişki **açık ve net**tir
3. Tablolar ve alan tipleri arasındaki ilişkiye **schema** denir
4. İlişkisel veritabanları aynı zamanda **SQL Databases** olarak da adlandırılır

> **SQL = Structured Query Language (Yapısal Sorgu Dili)**

---

## 🏢 Popüler İlişkisel Veritabanları {#popüler}

### 🔴 SQL Server
- **Geliştiren:** Microsoft
- ✅ Avantaj: Zengin kullanıcı arayüzü, büyük veri kümelerini işleyebilir
- ❌ Dezavantaj: Pahalı olabilir (Enterprise sürümü binlerce dolar)

### 🐬 MySQL Server
- **Geliştiren:** İsveçli bir şirket
- ✅ Avantaj: Ücretsiz ve açık kaynak, geniş dokümantasyon
- ❌ Dezavantaj: Çok fazla eş zamanlı işlemde sorun çıkarabilir

### 🐘 PostgreSQL Server
- **Geliştiren:** Prof. Michael Stonebraker
- ✅ Avantaj: Ek özellikler eklenebilir
- ❌ Dezavantaj: Kurulum ve yapılandırma zor olabilir

### 🔶 Oracle PL/SQL
- SQL ifadelerini kendi sözdiziminde barındıran prosedürel dil
- ✅ Avantaj: Yüksek güvenlik, OOP desteği

---

## 📦 Non-Relational Veritabanları (NoSQL) {#nosql}

**Non-relational** veritabanı, satır ve sütunlardan oluşan tablo şemasını **kullanmaz**.

```
SQL (İlişkisel)          NoSQL (İlişkisel Olmayan)
──────────────────       ──────────────────────────
Product Price  │         ┌─────────────────────────┐
Product Ingr.  │         │  Price                  │
Buying Rate    │         │  Ingredients            │
               │         │  Rate                   │
               │         │  All other related data │
               │         └─────────────────────────┘
```

---

## 🔑 Primary Key (Birincil Anahtar) {#primary-key}

- Primary key, bir kaydı **benzersiz şekilde tanımlayan** tek alan veya alan kombinasyonudur
- Bir tabloda yalnızca **bir tane** primary key olabilir
- Primary key **NULL değer içeremez**
- Primary key sayı, metin, karakter vb. olabilir

### Natural Key vs Surrogate Key:
- **Natural Key:** SSN veya e-posta gibi gerçek değerler
- **Surrogate Key:** 1, 2, 3, 4... gibi sıralı sayılar

```sql
-- Örnek tablo
StudentID | FirstName | LastName
----------|-----------|----------
   10     | John      | Walker     ← Primary Key: 10
   11     | Tom       | Hanks
   12     | Kevin     | Star
   13     | Carl      | Wall       ← Primary Key: 13
```

---

## 🔗 Foreign Key (Yabancı Anahtar) {#foreign-key}

- Foreign Key, **iki tablo arasında bağlantı kurmak** için kullanılır
- Bir tablodaki sütun(lar), başka bir tablonun Primary Key'ine atıfta bulunur
- Bir tablonun **birden fazla** Foreign Key'i olabilir
- Foreign Key **NULL değer alabilir**

```
Parent Table (Üst Tablo)         Child Table (Alt Tablo)
────────────────────────         ────────────────────────
StudentID │ FirstName            CourseID │ CourseName
──────────┼──────────            ─────────┼───────────
   10     │ John       ◄───────     200   │ Math
   11     │ Tom                     400   │ Selective
```

> **Not:** Parent Table silinmeden Child Table silinemez!

---

## 🔑 Composite Key (Bileşik Anahtar) {#composite-key}

Composite Key, bir tablodaki **iki veya daha fazla sütunun kombinasyonu**dur. Her sütun tek başına benzersizliği garantilemez, ancak birlikte benzersizliği sağlar.

```sql
-- Job_ID ve Recruiter kombinasyonu → Composite Primary Key
Job_ID | Recruiter  | Company
-------|------------|----------
  2    | Mark Eye   | RCG
  3    | John Ted   | RCG
  1    | Mark Eye   | Signature   ← Job_ID=1, Recruiter=Mark Eye → Benzersiz
  1    | John Ted   | InfoLog     ← Job_ID=1, Recruiter=John Ted → Benzersiz
```

---

## 🆚 UNIQUE KEY vs PRIMARY KEY {#unique-vs-primary}

| Özellik | Primary Key | Unique Key |
|---------|-------------|------------|
| Sayı | Tabloda yalnızca **1 tane** | Birden fazla olabilir |
| NULL | **Kabul etmez** | Sadece **1 tane** NULL kabul eder |
| Tekrar | İzin vermez | İzin vermez |
| Foreign Key Referansı | Evet | Evet |

---

## 🏋️ Alıştırmalar {#alıştırmalar}

### Alıştırma 1
Aşağıdaki soruları `employees` ve `job` tablosunu kullanarak cevaplayın:

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

**Sorular:**
1. Michael Scott'ın müdürü kim?
2. Angela Martin'in iş unvanı nedir?
3. Manual Tester'ların ortalama maaşı nedir?
4. En yüksek maaşlı çalışanın iş unvanı nedir?

---

### Alıştırma 2
Aşağıdaki tabloları inceleyin ve soruları cevaplayın:

**One-to-One Relation:**
1. Tom Hanks'ın adresini bulun
2. John Walker'ın adresini bulun
3. ID'si 17 olan öğrencinin adresini bulun

**One-to-Many Relation:**
1. Biology dersini alan öğrencilerin isimlerini bulun
2. Selective dersini alan öğrencilerin isimlerini bulun
3. Ders ücreti 600 olan dersi alan öğrencilerin isimlerini bulun

---

### 💡 Quiz Soruları

**Soru 1:** DELETE ve DROP hakkında aşağıdakilerden hangisi doğrudur?
- A) Her iki durumda da silinen veriler geri alınabilir
- B) DROP tabloyu ve içindeki kayıtları siler. DELETE sadece kayıtları siler ✅
- C) `DELETE FROM products PURGE` silinen verinin geri alınamaz şekilde silinmesini sağlar

**Soru 2:** `WHERE company='APPLE' OR company='GOOGLE'` sorgusu hangi isimleri gösterir?
```
ID       | NAME         | SALARY | COMPANY
---------|--------------|--------|----------
234567890| Brad Pitt    | 1500   | APPLE
456789012| Eddie Murphy | 1000   | GOOGLE
456789012| Brad Pitt    | 1500   | GOOGLE
```
- A) Brad Pitt, Eddie Murphy, Brad Pitt ✅
- B) Hata verir
- C) Hiçbir isim göstermez
- D) Brad Pitt, Eddie Murphy

---

*📌 Sonraki ders: SQL Data Types, CREATE TABLE, INSERT INTO*

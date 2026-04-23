<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:e94560,50:0f3460,100:16213e&height=130&section=header" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=24&duration=3000&pause=800&color=e94560&center=true&vCenter=true&width=760&lines=API+Testing+with+Rest+Assured+%F0%9F%8C%90;Java+%7C+JUnit+%7C+TestNG+%7C+GSON;GET+%7C+POST+%7C+PUT+%7C+PATCH+%7C+DELETE;TechProEd+Summer+2020" alt="Typing SVG" />

<br/>

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)
![Rest Assured](https://img.shields.io/badge/Rest_Assured-4.3.0-e94560?style=for-the-badge)
![JUnit](https://img.shields.io/badge/JUnit-4.11-25A162?style=for-the-badge&logo=junit5&logoColor=white)
![TestNG](https://img.shields.io/badge/TestNG-7.1.0-0f3460?style=for-the-badge)
![Maven](https://img.shields.io/badge/Maven-C71A36?style=for-the-badge&logo=apachemaven&logoColor=white)

</div>

---

## 📌 About This Repository

This repository contains **API Testing course notes** using **REST Assured** with Java, developed during TechProEd Summer 2020 program.

It covers everything from basic GET requests to advanced POJO-based testing, GSON serialization, and all HTTP methods.

> 🇹🇷 [Türkçe](#-türkçe) &nbsp;|&nbsp; 🇬🇧 [English](#-english)

---

## 🇹🇷 Türkçe

### 📚 Türkçe İçerik

| Gün | Konu | Dosya |
|-----|------|-------|
| 🗓️ Gün 1 | GET Request, TestBase, QueryParams | [Gun_01](./Turkish/GET/Gun_01_GET_Request_ve_TestBase.md) |
| 🗓️ Gün 2 | JsonPath, SoftAssert, GSON, Filtreleme | [Gun_02](./Turkish/GET/Gun_02_JsonPath_SoftAssert_GSON.md) |
| 🗓️ Gün 3 | POST Request — 4 Farklı Yol | [Gun_03](./Turkish/POST/Gun_03_POST_Request.md) |
| 🗓️ Gün 4 | PUT, PATCH, DELETE, ObjectMapper | [Gun_04](./Turkish/PUT_PATCH_DELETE/Gun_04_PUT_PATCH_DELETE.md) |
| 🗓️ Gün 5 | POJO, pom.xml, Proje Yapısı | [Gun_05](./Turkish/POJO_GSON/Gun_05_POJO_pom_Proje_Yapisi.md) |

---

## 🇬🇧 English

### 📚 English Content

| Day | Topic | File |
|-----|-------|------|
| 🗓️ Day 1 | GET Request, TestBase, QueryParams | [Day_01](./English/GET/Day_01_GET_Request_and_TestBase.md) |
| 🗓️ Day 2 | JsonPath, SoftAssert, GSON, Filtering | [Day_02](./English/GET/Day_02_JsonPath_SoftAssert_GSON.md) |
| 🗓️ Day 3 | POST Request — 4 Different Ways | [Day_03](./English/POST/Day_03_POST_Request.md) |
| 🗓️ Day 4 | PUT, PATCH, DELETE, ObjectMapper | [Day_04](./English/PUT_PATCH_DELETE/Day_04_PUT_PATCH_DELETE.md) |
| 🗓️ Day 5 | POJO, pom.xml, Project Structure | [Day_05](./English/POJO_GSON/Day_05_POJO_pom_Project_Structure.md) |

---

## 🗺️ Learning Path

```
GET Request (Basic)
        ↓
TestBase + RequestSpecification
        ↓
JsonPath + SoftAssert + GPath Filtering
        ↓
GSON De-Serialization (HashMap / List<Map>)
        ↓
POST Request (4 ways: String / JSONObject / HashMap / POJO)
        ↓
PUT · PATCH · DELETE
        ↓
ObjectMapper (JsonUtil)
        ↓
🎯 Full POJO + pom.xml Setup
```

---

## 🛠️ Tech Stack

```xml
<!-- pom.xml Dependencies -->
junit          4.11    → @Test, @Before annotations
rest-assured   4.3.0   → given / when / then API
org.json       latest  → JSONObject body creation
testng         7.1.0   → SoftAssert
gson           2.8.6   → JSON ↔ Java Object
jackson        1.9.13  → ObjectMapper / POJO serialization
```

---

## 📋 HTTP Methods Summary

| Method | Purpose | Body Required | Auth |
|--------|---------|---------------|------|
| `GET` | Read data | ❌ | Optional |
| `POST` | Create data | ✅ | Usually required |
| `PUT` | Full update | ✅ | Usually required |
| `PATCH` | Partial update | ✅ (changed fields only) | Usually required |
| `DELETE` | Delete data | ❌ | Usually required |

---

## 📂 Repository Structure

```
API-Testing/
├── Turkish/
│   ├── GET/
│   │   ├── Gun_01_GET_Request_ve_TestBase.md
│   │   └── Gun_02_JsonPath_SoftAssert_GSON.md
│   ├── POST/
│   │   └── Gun_03_POST_Request.md
│   ├── PUT_PATCH_DELETE/
│   │   └── Gun_04_PUT_PATCH_DELETE.md
│   └── POJO_GSON/
│       └── Gun_05_POJO_pom_Proje_Yapisi.md
├── English/
│   ├── GET/
│   │   ├── Day_01_GET_Request_and_TestBase.md
│   │   └── Day_02_JsonPath_SoftAssert_GSON.md
│   ├── POST/
│   │   └── Day_03_POST_Request.md
│   ├── PUT_PATCH_DELETE/
│   │   └── Day_04_PUT_PATCH_DELETE.md
│   └── POJO_GSON/
│       └── Day_05_POJO_pom_Project_Structure.md
└── README.md
```

---

## 🔑 Key Concepts

### Rest Assured Test Structure
```java
given()              // Setup: headers, auth, body, spec
    .spec(spec01)
    .contentType(ContentType.JSON)
    .auth().basic("admin", "password")
    .body(requestBody)
.when()              // Action: HTTP method
    .post("/booking")
.then()              // Verification: assertions
    .assertThat()
    .statusCode(200)
    .body("firstname", equalTo("John"));
```

### SoftAssert 3 Steps
```java
SoftAssert sa = new SoftAssert();  // 1. Create
sa.assertEquals(actual, expected); // 2. Assert
sa.assertAll();                    // 3. Report all
```

### POJO 5 Rules
```
1. Private variables for each JSON key
2. Getter + Setter methods for each variable
3. No-arg constructor (no super() inside!)
4. All-args constructor (no super() inside!)
5. toString() method
```

---

## 👩‍💻 About

<div align="center">

**Gamzenur Uzunlu**
*Data Engineer | TechProEd API Testing Graduate*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-gamzenuruzunlu-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gamzenuruzunlu/)
[![GitHub](https://img.shields.io/badge/GitHub-pinhanderler-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pinhanderler)

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:16213e,50:0f3460,100:e94560&height=80&section=footer" width="100%"/>

</div>

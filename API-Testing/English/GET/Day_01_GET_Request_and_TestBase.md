# 🌐 Day 1 — GET Request & TestBase

> **TechProEd | API Testing with Rest Assured — Summer 2020**

---

## 📚 Table of Contents

1. [What is a GET Request?](#get-nedir)
2. [TestBase Class](#testbase)
3. [GetRequest04 — Employees API](#getrequest04)
4. [GetRequest05 — Booking API](#getrequest05)
5. [GetRequest06 — TestBase ile GET](#getrequest06)
6. [GetRequest07 — Query Parameters](#getrequest07)
7. [Practice Exercises](#alıştırmalar)

---

## 🔷 What is a GET Request? {#get-nedir}

GET Request, bir API'dan veri **okumak/çekmek** için kullanılır.

```
GET isteği göndermek için yeterli olan tek şey: ENDPOINT
```

| Özellik | Explanation |
|---------|----------|
| Metod | `GET` |
| Amaç | Veri okuma |
| Request Body | ❌ Gerekmez |
| Authorization | İsteğe bağlı |
| Status Code | 200 OK |

---

## 🏗️ TestBase Class {#testbase}

`TestBase`, her testte tekrar yazılan ortak konfigürasyonları tek bir yerde toplar. Test sınıfları bu sınıfı **extend** ederek kullanır.

```java
package techproedturkish01.techproedturkish01api;

import org.junit.Before;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.specification.RequestSpecification;

public class TestBase {

    protected RequestSpecification spec01; // https://restful-booker.herokuapp.com
    protected RequestSpecification spec02; // http://dummy.restapiexample.com/api/v1/employees
    protected RequestSpecification spec03; // https://jsonplaceholder.typicode.com/todos

    @Before
    public void setUp01() {
        spec01 = new RequestSpecBuilder()
                     .setBaseUri("https://restful-booker.herokuapp.com")
                     .build();
    }

    @Before
    public void setUp02() {
        spec02 = new RequestSpecBuilder()
                     .setBaseUri("http://dummy.restapiexample.com/api/v1/employees")
                     .build();
    }

    @Before
    public void setUp03() {
        spec03 = new RequestSpecBuilder()
                     .setBaseUri("https://jsonplaceholder.typicode.com/todos")
                     .build();
    }
}
```

> 💡 **NOT:** TestBase sınıfı extend edilmeden `spec01`, `spec02`, `spec03`'e erişilemez!

---

## 📋 GetRequest04 — Employees API {#getrequest04}

**Test Senaryosu:**
- URL: `http://dummy.restapiexample.com/api/v1/employees`
- 24 çalışan olduğunu doğrula
- "Ashton Cox" çalışanlar arasında olsun
- 21, 61, 23 yaşların olduğunu doğrula

```java
package techproedturkish01.techproedturkish01api;

import org.hamcrest.Matchers;
import org.junit.Test;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

public class GetRequest04 {

    @Test
    public void get01() {
        Response response = given()
                                .accept(ContentType.JSON)
                            .when()
                                .get("http://dummy.restapiexample.com/api/v1/employees");

        response.prettyPrint();

        response.then()
                .assertThat()
                .statusCode(200)
                .contentType(ContentType.JSON)
                .body("data.id", Matchers.hasSize(24))                        // 24 çalışan
                .body("data.employee_name", Matchers.hasItem("Ashton Cox"))   // isim kontrolü
                .body("data.employee_age", Matchers.hasItems("21", "61", "23")); // yaş kontrolü
    }
}
```

### 🔍 Explanation

| Metod | What it does |
|-------|-----------|
| `given().accept(ContentType.JSON)` | Kabul tipi JSON olarak ayarla |
| `when().get(url)` | GET isteği gönder |
| `then().assertThat()` | Doğrulama başlat |
| `statusCode(200)` | HTTP 200 bekle |
| `body("data.id", hasSize(24))` | data dizisinde 24 eleman bekle |
| `body("...", hasItem("Ashton Cox"))` | Listede bu isim olsun |
| `body("...", hasItems("21","61","23"))` | Bu yaşlar listede olsun |

---

## 📋 GetRequest05 — Booking API {#getrequest05}

**Test Senaryosu:**
- URL: `https://restful-booker.herokuapp.com/booking/5`
- firstname = "Mark", totalprice = 892, checkin = "2018-03-21"

```java
package techproedturkish01.techproedturkish01api;

import static io.restassured.RestAssured.*;
import org.hamcrest.Matchers;
import org.junit.Test;
import io.restassured.http.ContentType;
import io.restassured.response.Response;

public class GetRequest05 {

    @Test
    public void getMethod01() {
        Response response = given()
                            .when()
                                .get("https://restful-booker.herokuapp.com/booking/5");

        response.prettyPrint();

        response.then()
                .assertThat()
                .statusCode(200)
                .contentType(ContentType.JSON)
                .body("firstname",               Matchers.equalTo("Mark"),
                      "totalprice",              Matchers.equalTo(892),
                      "bookingdates.checkin",    Matchers.equalTo("2018-03-21"));
    }
}
```

> 💡 **NOT:** `bookingdates.checkin` şeklinde nokta ile iç içe JSON alanlarına ulaşılır.

---

## 📋 GetRequest06 — TestBase ile GET {#getrequest06}

`TestBase` kullanarak `spec01`'den base URI alınır, sadece path yazılır.

```java
package techproedturkish01.techproedturkish01api;

import static org.hamcrest.Matchers.*;
import org.junit.Test;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

public class GetRequest06 extends TestBase {  // ← TestBase extend edildi

    @Test
    public void get01() {
        Response response = given()
                                .spec(spec01)         // ← base URI: restful-booker
                            .when()
                                .get("/booking/5");   // ← sadece path yeterli

        response.prettyPrint();

        response.then()
                .assertThat()
                .statusCode(200)
                .contentType(ContentType.JSON)
                .body("firstname",                 equalTo("Eric"),
                      "lastname",                  equalTo("Jackson"),
                      "totalprice",                equalTo(249),
                      "depositpaid",               equalTo(false),
                      "bookingdates.checkin",       equalTo("2016-04-18"),
                      "bookingdates.checkout",      equalTo("2019-07-02"),
                      "additionalneeds",            equalTo("Breakfast"));
    }
}
```

---

## 📋 GetRequest07 — Query Parameters {#getrequest07}

URL'e parametreleri 2 şekilde ekleyebilirsiniz:

```java
public class GetRequest07 extends TestBase {

    // ❌ Bad Way: Parametreleri URL'ye doğrudan yaz
    @Test
    public void get01() {
        Response response = given()
                                .spec(spec01)
                                .get("/booking?firstname=Susan&depositpaid=true");
        response.prettyPrint();
        assertTrue(response.getBody().asString().contains("bookingid"));
    }

    // ✅ Good Way: queryParams ile yaz
    @Test
    public void get02() {
        spec01.queryParams("firstname",   "Susan",
                           "depositpaid", true);

        Response response = given()
                                .spec(spec01)
                                .get("/booking");
        response.prettyPrint();
        assertTrue(response.getBody().asString().contains("bookingid"));
    }
}
```

### ✅ vs ❌ Comparison

| Yöntem | Why? |
|--------|--------|
| `?firstname=Susan` URL'de | ❌ Bakımı zor, özel karakterlerde sorun çıkabilir |
| `.queryParams("firstname","Susan")` | ✅ Okunabilir, encode otomatik, bakımı kolay |

---

## 🏋️ Practice Exercises {#alıştırmalar}

### Alıştırma 1
`https://restful-booker.herokuapp.com/booking/3` adresine GET isteği gönder:
- Status code 200 olsun
- firstname ve lastname doğrula
- totalprice doğrula

### Alıştırma 2
`http://dummy.restapiexample.com/api/v1/employees` adresine GET isteği gönder:
- 24 çalışan olsun
- "Tiger Nixon" çalışanlar arasında olsun
- En yüksek maaşın 725000 olduğunu doğrula

```java
// Alıştırma 1 Çözümü:
Response response = given()
                        .spec(spec01)
                    .when()
                        .get("/booking/3");

response.then()
        .assertThat()
        .statusCode(200)
        .body("firstname", equalTo("Jim"))
        .body("lastname",  equalTo("Jones"))
        .body("totalprice", equalTo(596));
```

---

*📌 Next lesson: JsonPath, SoftAssert, GSON De-Serialization*

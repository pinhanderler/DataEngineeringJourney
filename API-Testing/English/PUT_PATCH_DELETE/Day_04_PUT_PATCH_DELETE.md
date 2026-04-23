# 🌐 Day 4 — PUT, PATCH & DELETE Request

> **TechProEd | API Testing with Rest Assured — Summer 2020**

---

## 📚 İçindekiler

1. [PUT vs PATCH vs DELETE](#farklar)
2. [PutRequest01 — Basic PUT](#putrequest01)
3. [PutRequest02 — PUT with Verify](#putrequest02)
4. [PatchRequest01 — PATCH](#patchrequest01)
5. [Delete01 — DELETE](#delete01)
6. [ObjectMapper — JsonUtil](#objectmapper)
7. [Practice Exercises](#alıştırmalar)

---

## 🆚 PUT vs PATCH vs DELETE {#farklar}

| Metod | Amaç | Body | Authorization |
|-------|------|------|---------------|
| `PUT` | Tüm kaydı güncelle | ✅ Şart | Genellikle şart |
| `PATCH` | Kısmi güncelleme | ✅ (Sadece değişen) | Genellikle şart |
| `DELETE` | Kaydı sil | ❌ Gerekmez | Genellikle şart |

---

## 📋 PutRequest01 — Basic PUT {#putrequest01}

```java
package techproedturkish01.techproedturkish01api;

import org.json.JSONObject;
import org.junit.Test;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

public class PutRequest01 extends TestBase {

    @Test
    public void put01() {

        // Önce mevcut veriyi gör
        Response response = given()
                                .spec(spec03)
                            .when()
                                .get("/200");
        response.prettyPrint();
        // → {"userId":10, "id":200, "title":"ipsam aperiam...", "completed":false}

        // Güncelleme için yeni body oluştur
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("title",     "Suleyman");
        jsonObject.put("userId",    88);
        jsonObject.put("completed", true);

        // PUT isteği gönder
        Response responseAfterPut = given()
                                        .contentType(ContentType.JSON)
                                        .spec(spec03)
                                        .body(jsonObject.toString())
                                    .when()
                                        .put("/200");

        responseAfterPut.prettyPrint();
        // → {"userId":88, "id":200, "title":"Suleyman", "completed":true}
    }
}
```

---

## 📋 PutRequest02 — PUT with Verify {#putrequest02}

```java
public class PutRequest02 extends TestBase {

    @Test
    public void put01() {

        // Önce GET ile mevcut veriyi al
        Response response = given()
                                .spec(spec03)
                            .when()
                                .get("/200");
        response.prettyPrint();

        // Güncellenecek data
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("title",     "Suleyman");
        jsonObject.put("userId",    88);
        jsonObject.put("completed", true);

        // PUT isteği
        Response responseAfterPut = given()
                                        .contentType(ContentType.JSON)
                                        .spec(spec03)
                                        .body(jsonObject.toString())
                                    .when()
                                        .put("/200");

        responseAfterPut.prettyPrint();

        // Status code doğrula
        responseAfterPut.then().assertThat().statusCode(200);

        JsonPath json = responseAfterPut.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        // Güncellenmiş değerleri doğrula
        softAssert.assertEquals(json.getBoolean("completed"), jsonObject.get("completed"));
        softAssert.assertEquals(json.getString("title"),      jsonObject.get("title"));
        softAssert.assertEquals(json.getInt("userId"),        jsonObject.get("userId"));

        softAssert.assertAll();
    }
}
```

---

## 📋 PatchRequest01 — Partial Update {#patchrequest01}

**PATCH**, sadece belirli bir alanı günceller. PUT tüm kaydı günceller.

```java
public class PatchRequest01 extends TestBase {

    @Test
    public void patch01() {

        // Önce mevcut veriyi gör
        Response responseBeforePatch = given()
                                           .spec(spec03)
                                       .when()
                                           .get("/200");
        responseBeforePatch.prettyPrint();
        // → {"userId":10, "id":200, "title":"ipsam aperiam...", "completed":false}

        // Sadece title'ı güncelle
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("title", "Kemal Can");   // ← Sadece bu alan değişiyor

        Response responseAfterPatch = given()
                                          .contentType(ContentType.JSON)
                                          .spec(spec03)
                                          .body(jsonObject.toString())
                                      .when()
                                          .patch("/200");   // ← patch() metodu

        responseAfterPatch.prettyPrint();
        // → {"userId":10, "id":200, "title":"Kemal Can", "completed":false}
        //    Sadece title değişti, diğerleri aynı kaldı!

        // Doğrulama
        responseAfterPatch.then().assertThat().statusCode(200);

        JsonPath json = responseAfterPatch.jsonPath();

        // Hard assertion
        assertEquals(jsonObject.get("title"), json.get("title"));

        // Soft assertion
        SoftAssert softAssert = new SoftAssert();
        softAssert.assertEquals(json.getString("title"), jsonObject.get("title"));
        softAssert.assertAll();
    }
}
```

### PUT vs PATCH Davranış Farkı

```
Mevcut kayıt:
{ "userId":10, "id":200, "title":"ipsam aperiam...", "completed":false }

PUT { "title":"Yeni" }  →  { "title":"Yeni" }  (userId, id, completed kaybolur!)
PATCH { "title":"Yeni" }  →  { "userId":10, "id":200, "title":"Yeni", "completed":false }
```

---

## 📋 Delete01 — DELETE Request {#delete01}

```java
public class Delete01 extends TestBase {

    @Test
    public void delete01() {

        // 1) Silmeden önce kaydın var olduğunu doğrula
        Response responseBeforeDelete = given()
                                            .spec(spec03)
                                        .when()
                                            .get("/198");
        responseBeforeDelete.prettyPrint();
        // → {"userId":10, "id":198, "title":"quis eius est...", "completed":true}

        // 2) DELETE isteği gönder
        Response responseAfterDelete = given()
                                           .spec(spec03)
                                       .when()
                                           .delete("/198");   // ← delete() metodu
        responseAfterDelete.prettyPrint();
        // → {}  (boş response)

        // 3) Silindikten sonra GET ile kontrol et
        Response getResponseAfterDelete = given()
                                              .spec(spec03)
                                          .when()
                                              .get("/198");
        getResponseAfterDelete.prettyPrint();

        // 4) Status code doğrula
        responseAfterDelete.then().assertThat().statusCode(200);

        // 5) Response body boş mu?
        assertTrue(responseAfterDelete.getBody().asString().equals("{}"));
    }
}
```

---

## 🔷 ObjectMapper — JsonUtil Utility {#objectmapper}

`ObjectMapper`, JSON ↔ Java Object dönüşümü için güçlü bir araçtır.

```java
package Utilities;

import org.codehaus.jackson.map.ObjectMapper;

public class JsonUtil {

    private static ObjectMapper mapper = new ObjectMapper();

    // Java Object → JSON (Serialization)
    public static String convertJavaToJson(Object object) {
        try {
            return mapper.writeValueAsString(object);
        } catch (Exception e) {
            System.out.println("Hata: " + e.getMessage());
            return "";
        }
    }

    // JSON → Java Object (De-Serialization)
    public static <T> T convertJsonToJava(String json, Class<T> cls) {
        try {
            return mapper.readValue(json, cls);
        } catch (Exception e) {
            System.out.println("Hata: " + e.getMessage());
            return null;
        }
    }
}
```

### ObjectMapper ile Test

```java
public class ObjectMapperTestWithPojo extends TestBase {

    @Test
    public void javaToJson() {
        BookingDates bookingDates = new BookingDates("2020-11-03", "2020-11-08");

        // Serialization: POJO → JSON
        String jsonFromPojo = JsonUtil.convertJavaToJson(bookingDates);
        System.out.println(jsonFromPojo);
        // → {"checkin":"2020-11-03","checkout":"2020-11-08"}
    }

    @Test
    public void jsonToJava() {
        Response response = given()
                                .spec(spec01)
                            .when()
                                .get("/booking/3");

        // De-Serialization: JSON → POJO
        Booking jsonToPojoApi = JsonUtil.convertJsonToJava(response.asString(), Booking.class);
        System.out.println(jsonToPojoApi);
        // → Booking [firstname=Jim, lastname=Ericsson, ...]

        // Test case data
        BookingDates bookingDates = new BookingDates("2015-06-07", "2020-08-10");
        Booking booking = new Booking("Susan", "Jones", 277, true, bookingDates, "Breakfast");

        response.then().assertThat().statusCode(200);

        // Sadece tarih alanlarını doğrula
        assertEquals(booking.getBookingdates().getCheckin(),
                     jsonToPojoApi.getBookingdates().getCheckin());
        assertEquals(booking.getBookingdates().getCheckout(),
                     jsonToPojoApi.getBookingdates().getCheckout());
    }
}
```

---

## 📊 All Request Types Summary

```
GET    → Veri OKU     → given().when().get(url)
POST   → Veri EKLE    → given().body(...).when().post(url)
PUT    → Veri GÜNCELLE (tam) → given().body(...).when().put(url)
PATCH  → Veri GÜNCELLE (kısmi) → given().body(...).when().patch(url)
DELETE → Veri SİL     → given().when().delete(url)
```

---

## 🏋️ Practice Exercises {#alıştırmalar}

### Alıştırma 1
`https://jsonplaceholder.typicode.com/todos/100` adresine PUT isteği gönder:
- title: "Updated Title", completed: true, userId: 5
- Response'un status code 200 olduğunu doğrula
- Güncellenen değerleri verify et

### Alıştırma 2
`https://jsonplaceholder.typicode.com/todos/50` adresine PATCH isteği gönder:
- Sadece `completed` değerini `true` yap
- Diğer alanların değişmediğini doğrula

```java
// Alıştırma 1 Çözümü:
JSONObject body = new JSONObject();
body.put("title",     "Updated Title");
body.put("completed", true);
body.put("userId",    5);

Response response = given()
                        .contentType(ContentType.JSON)
                        .spec(spec03)
                        .body(body.toString())
                    .when()
                        .put("/100");

response.then().assertThat().statusCode(200);

JsonPath json = response.jsonPath();
SoftAssert sa = new SoftAssert();
sa.assertEquals(json.getString("title"), body.get("title"));
sa.assertEquals(json.getBoolean("completed"), body.get("completed"));
sa.assertEquals(json.getInt("userId"), body.get("userId"));
sa.assertAll();
```

---

*📌 Next lesson: POJO oluşturma, pom.xml bağımlılıkları*

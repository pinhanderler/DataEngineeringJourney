# 🌐 Day 3 — POST Request (4 Farklı Yol)

> **TechProEd | API Testing with Rest Assured — Summer 2020**

---

## 📚 İçindekiler

1. [What is a POST Request?](#post-nedir)
2. [GET vs POST Differences](#get-vs-post)
3. [PostRequest01 — String Body](#postrequest01)
4. [PostRequest02 — JSONObject Class](#postrequest02)
5. [PostRequest03 — HashMap](#postrequest03)
6. [PostRequest04 — POJO (En İyi Yol)](#postrequest04)
7. [PostRequest05 — POJO + Getter for Verify](#postrequest05)
8. [Practice Exercises](#alıştırmalar)

---

## 🔷 What is a POST Request? {#post-nedir}

POST Request, API'ya **yeni veri oluşturmak** için kullanılır.

### POST Request için Requirements:

| # | Gereksinim | Required? |
|---|-----------|-------------|
| 1 | Endpoint | ✅ Required |
| 2 | Request Body | ✅ Required |
| 3 | Authorization | ✅ Required |
| 4 | Accept Type | ⚡ Optional |
| 5 | Content Type | ⚡ Optional |

> ⚠️ **NOT:** API developer bazı alanların boş bırakılmamasını zorunlu tutmuşsa, o alanlar dolu gönderilmezse **400 Bad Request** alınır!

---

## 🆚 GET vs POST Differences {#get-vs-post}

| Özellik | GET | POST |
|---------|-----|------|
| Amaç | Veri okuma | Yeni veri oluşturma |
| Request Body | ❌ Gerekmez | ✅ Zorunlu |
| Authorization | Optional | Genellikle zorunlu |
| Idempotent | ✅ Evet | ❌ Hayır |

---

## 📋 PostRequest01 — String Body (Bad Way) {#postrequest01}

```java
package techproedturkish01.techproedturkish01api;

import org.junit.Test;
import org.testng.asserts.SoftAssert;
import io.restassured.http.ContentType;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

public class PostRequest01 extends TestBase {

    @Test
    public void post01() {

        // ❌ Kötü Yol: String olarak body yaz
        String jsonRequestBody = "{\n" +
            "\"firstname\": \"Suleyman\",\n" +
            "\"lastname\": \"Alptekin\",\n" +
            "\"totalprice\": 123,\n" +
            "\"depositpaid\": true,\n" +
            "\"bookingdates\": {\n" +
            "    \"checkin\": \"2020-05-02\",\n" +
            "    \"checkout\": \"2020-05-05\"\n" +
            "},\n" +
            "\"additionalneeds\": \"Wifi\"\n" +
            "}";

        Response response = given()
                                .contentType(ContentType.JSON)   // ← POST'ta bu önemli!
                                .spec(spec01)
                                .auth().basic("admin", "password123")  // ← Authorization
                                .body(jsonRequestBody)
                            .when()
                                .post("/booking");

        response.prettyPrint();

        response.then().assertThat().statusCode(200);

        JsonPath json = response.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        softAssert.assertEquals(json.getString("booking.firstname"),   "Suleyman");
        softAssert.assertEquals(json.getString("booking.lastname"),    "Alptekin");
        softAssert.assertEquals(json.getInt("booking.totalprice"),     123);
        softAssert.assertEquals(json.getBoolean("booking.depositpaid"), true);
        softAssert.assertEquals(json.getString("booking.bookingdates.checkin"),  "2020-05-02");
        softAssert.assertEquals(json.getString("booking.bookingdates.checkout"), "2020-05-05");
        softAssert.assertEquals(json.getString("booking.additionalneeds"), "Wifi");

        softAssert.assertAll();
    }
}
```

---

## 📋 PostRequest02 — JSONObject Class {#postrequest02}

`TestBase`'deki `createRequestBodyByJsonObjectClass()` metodu:

```java
// TestBase içinde:
protected Response createRequestBodyByJsonObjectClass() {

    JSONObject jsonBookingDatesBody = new JSONObject();
    jsonBookingDatesBody.put("checkin",  "2020-05-02");
    jsonBookingDatesBody.put("checkout", "2020-05-05");

    JSONObject jsonRequestBody = new JSONObject();
    jsonRequestBody.put("firstname",      "Kemal");
    jsonRequestBody.put("lastname",       "Can");
    jsonRequestBody.put("totalprice",     888);
    jsonRequestBody.put("depositpaid",    false);
    jsonRequestBody.put("bookingdates",   jsonBookingDatesBody);  // ← iç içe JSON
    jsonRequestBody.put("additionalneeds","Wifi");

    Response response = given()
                            .contentType(ContentType.JSON)
                            .spec(spec01)
                            .auth().basic("admin", "password123")
                            .body(jsonRequestBody.toString())
                        .when()
                            .post("/booking");
    return response;
}
```

```java
// Test sınıfı:
public class PostRequest02 extends TestBase {

    @Test
    public void post01() {
        Response response = createRequestBodyByJsonObjectClass(); // ← TestBase metodu

        response.prettyPrint();
        response.then().assertThat().statusCode(200);

        JsonPath json = response.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        softAssert.assertEquals(json.getString("booking.firstname"), "Kemal");
        softAssert.assertEquals(json.getString("booking.lastname"),  "Can");
        softAssert.assertEquals(json.getInt("booking.totalprice"),   888);
        // ...
        softAssert.assertAll();
    }
}
```

---

## 📋 PostRequest03 — Using HashMap {#postrequest03}

```java
// TestBase içinde:
protected Response createRequestBodyByMap() {

    Map<String, String> bookingDatesMap = new HashMap<>();
    bookingDatesMap.put("checkin",  "2020-05-02");
    bookingDatesMap.put("checkout", "2020-05-05");

    Map<String, Object> requestBodyMap = new HashMap<>();
    requestBodyMap.put("firstname",      "Ahmet");
    requestBodyMap.put("lastname",       "Yildiz");
    requestBodyMap.put("totalprice",     123);
    requestBodyMap.put("depositpaid",    true);
    requestBodyMap.put("bookingdates",   bookingDatesMap);  // ← Map içinde Map
    requestBodyMap.put("additionalneeds","Wifi");

    Response response = given()
                            .contentType(ContentType.JSON)
                            .spec(spec01)
                            .auth().basic("admin", "password123")
                            .body(requestBodyMap)           // ← Map direkt body olarak
                        .when()
                            .post("/booking");
    return response;
}
```

---

## 📋 PostRequest04 — POJO (Best Way!) {#postrequest04}

**POJO (Plain Old Java Object)**, JSON yapısını temsil eden Java sınıfıdır.

### Booking.java (POJO)

```java
package techproedturkish01.techproedturkish01api;

import org.codehaus.jackson.annotate.JsonProperty;

public class Booking {

    @JsonProperty("firstname")
    private String firstname;

    @JsonProperty("lastname")
    private String lastname;

    @JsonProperty("totalprice")
    private int totalprice;

    @JsonProperty("depositpaid")
    private boolean depositpaid;

    @JsonProperty("bookingdates")
    private BookingDates bookingdates;

    @JsonProperty("additionalneeds")
    private String additionalneeds;

    // Getter'lar
    public String getFirstname()       { return firstname; }
    public String getLastname()        { return lastname; }
    public int getTotalprice()         { return totalprice; }
    public boolean getDepositpaid()    { return depositpaid; }
    public BookingDates getBookingdates() { return bookingdates; }
    public String getAdditionalneeds() { return additionalneeds; }

    // Setter'lar
    public void setFirstname(String firstname)          { this.firstname = firstname; }
    public void setLastname(String lastname)            { this.lastname = lastname; }
    public void setTotalprice(Integer totalprice)       { this.totalprice = totalprice; }
    public void setDepositpaid(Boolean depositpaid)     { this.depositpaid = depositpaid; }
    public void setBookingdates(BookingDates bookingdates) { this.bookingdates = bookingdates; }
    public void setAdditionalneeds(String additionalneeds){ this.additionalneeds = additionalneeds; }

    // Parametresiz constructor
    public Booking() {}

    // Parametreli constructor
    public Booking(String firstname, String lastname, Integer totalprice,
                   Boolean depositpaid, BookingDates bookingdates, String additionalneeds) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.totalprice = totalprice;
        this.depositpaid = depositpaid;
        this.bookingdates = bookingdates;
        this.additionalneeds = additionalneeds;
    }

    @Override
    public String toString() {
        return "Booking [firstname=" + firstname + ", lastname=" + lastname +
               ", totalprice=" + totalprice + ", depositpaid=" + depositpaid +
               ", bookingdates=" + bookingdates + ", additionalneeds=" + additionalneeds + "]";
    }
}
```

### BookingDates.java (POJO)

```java
public class BookingDates {

    @JsonProperty("checkin")
    private String checkin;

    @JsonProperty("checkout")
    private String checkout;

    public String getCheckin()  { return checkin; }
    public String getCheckout() { return checkout; }
    public void setCheckin(String checkin)   { this.checkin = checkin; }
    public void setCheckout(String checkout) { this.checkout = checkout; }

    public BookingDates() {}

    public BookingDates(String checkin, String checkout) {
        this.checkin = checkin;
        this.checkout = checkout;
    }

    @Override
    public String toString() {
        return "BookingDates [checkin=" + checkin + ", checkout=" + checkout + "]";
    }
}
```

### PostRequest04 — POJO ile Test

```java
public class PostRequest04 extends TestBase {

    @Test
    public void post01() {

        // ✅ En İyi Yol: POJO ile
        BookingDates bookingDates = new BookingDates("2020-05-02", "2020-05-05");
        Booking booking = new Booking("Suleyman", "Alptekin", 123, true, bookingDates, "Wifi");

        Response response = given()
                                .contentType(ContentType.JSON)
                                .spec(spec01)
                                .auth().basic("admin", "password123")
                                .body(booking)   // ← POJO direkt body olarak!
                            .when()
                                .post("/booking");

        response.prettyPrint();
        response.then().assertThat().statusCode(200);

        JsonPath json = response.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        softAssert.assertEquals(json.getString("booking.firstname"),   "Suleyman");
        softAssert.assertEquals(json.getString("booking.lastname"),    "Alptekin");
        softAssert.assertEquals(json.getInt("booking.totalprice"),     123);
        softAssert.assertEquals(json.getBoolean("booking.depositpaid"), true);
        softAssert.assertEquals(json.getString("booking.bookingdates.checkin"),  "2020-05-02");
        softAssert.assertEquals(json.getString("booking.bookingdates.checkout"), "2020-05-05");
        softAssert.assertEquals(json.getString("booking.additionalneeds"), "Wifi");

        softAssert.assertAll();
    }
}
```

---

## 📋 PostRequest05 — POJO + Getter for Verify {#postrequest05}

```java
public class PostRequest05 extends TestBase {

    @Test
    public void post01() {

        BookingDates bookingDates = new BookingDates("2020-05-02", "2020-05-05");
        Booking booking = new Booking("Ayse", "Yildiz", 333, true, bookingDates, "Wifi");

        Response response = given()
                                .contentType(ContentType.JSON)
                                .spec(spec01)
                                .auth().basic("admin", "password123")
                                .body(booking)
                            .when()
                                .post("/booking");

        JsonPath json = response.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        // ✅ Getter ile verify — sabit değer yazmak yerine obje kullan!
        softAssert.assertEquals(json.getString("booking.firstname"),
                                booking.getFirstname());  // ← "Ayse"

        softAssert.assertEquals(json.getString("booking.lastname"),
                                booking.getLastname());   // ← "Yildiz"

        softAssert.assertEquals(json.getInt("booking.totalprice"),
                                booking.getTotalprice()); // ← 333

        softAssert.assertEquals(json.getBoolean("booking.depositpaid"),
                                booking.getDepositpaid()); // ← true

        softAssert.assertEquals(json.getString("booking.bookingdates.checkin"),
                                booking.getBookingdates().getCheckin()); // ← "2020-05-02"

        softAssert.assertEquals(json.getString("booking.bookingdates.checkout"),
                                booking.getBookingdates().getCheckout()); // ← "2020-05-05"

        softAssert.assertEquals(json.getString("booking.additionalneeds"),
                                booking.getAdditionalneeds()); // ← "Wifi"

        softAssert.assertAll();
    }
}
```

---

## 📊 4 Ways Comparison

| Yol | Advantage | Disadvantage |
|-----|---------|------------|
| String body | Basit | ❌ Hard to maintain, hata yapımı kolay |
| JSONObject | Daha düzenli | ⚠️ Boilerplate kod |
| HashMap | Esnek | ⚠️ Type safety yok |
| POJO ✅ | Type-safe, bakımı kolay, getter/setter | Sınıf yazmak gerekiyor |

---

## 🏋️ Practice Exercises {#alıştırmalar}

### Alıştırma 1
POJO kullanarak yeni bir booking oluştur:
- firstname: "Gamze", lastname: "Nur"
- totalprice: 500, depositpaid: false
- checkin: "2024-01-10", checkout: "2024-01-15"
- additionalneeds: "Breakfast"
- Response body ile request body'nin aynı olduğunu verify et

---

*📌 Next lesson: PUT, PATCH, DELETE Request'ler*

# 🌐 Day 5 — POJO, pom.xml & Project Structure

> **TechProEd | API Testing with Rest Assured — Summer 2020**

---

## 📚 İçindekiler

1. [What is POJO?](#pojo)
2. [POJO Creation Rules](#pojo-kurallar)
3. [pom.xml Dependencies](#pom)
4. [Project Structure](#proje)
5. [Full TestBase Class](#testbase-tam)
6. [Practice Exercises](#alıştırmalar)

---

## 🔷 What is POJO? {#pojo}

**POJO = Plain Old Java Object**

JSON yapısını temsil eden sıradan bir Java sınıfıdır. API test süreçlerinde request/response body'sini Java nesnesi olarak kullanmak için tercih edilir.

```
JSON                          ←→   POJO
{ "firstname": "Ali" }        ←→   booking.getFirstname() → "Ali"
{ "totalprice": 123 }         ←→   booking.getTotalprice() → 123
{ "depositpaid": true }       ←→   booking.getDepositpaid() → true
```

> 💡 **POJO'yu otomatik oluşturmak için:** http://www.jsonschema2pojo.org/

---

## 📋 POJO Creation Rules {#pojo-kurallar}

5 kural:

```
1) JSON'daki key'ler için private değişken tanımla
2) Her değişken için getter ve setter metotları oluştur
3) Parametresiz constructor oluştur (içinde super() olmasın!)
4) Tüm değişkenleri parametre alan parametreli constructor oluştur
5) toString() metodu oluştur
```

### Tam Booking.java POJO

```java
package techproedturkish01.techproedturkish01api;

import org.codehaus.jackson.annotate.JsonProperty;

public class Booking {

    // 1) Private değişkenler
    @JsonProperty("firstname")    private String firstname;
    @JsonProperty("lastname")     private String lastname;
    @JsonProperty("totalprice")   private int totalprice;
    @JsonProperty("depositpaid")  private boolean depositpaid;
    @JsonProperty("bookingdates") private BookingDates bookingdates;
    @JsonProperty("additionalneeds") private String additionalneeds;

    // 2) Getter'lar
    @JsonProperty("firstname")    public String getFirstname()       { return firstname; }
    @JsonProperty("lastname")     public String getLastname()        { return lastname; }
    @JsonProperty("totalprice")   public int getTotalprice()         { return totalprice; }
    @JsonProperty("depositpaid")  public boolean getDepositpaid()    { return depositpaid; }
    @JsonProperty("bookingdates") public BookingDates getBookingdates() { return bookingdates; }
    @JsonProperty("additionalneeds") public String getAdditionalneeds() { return additionalneeds; }

    // 2) Setter'lar
    @JsonProperty("firstname")    public void setFirstname(String v)      { this.firstname = v; }
    @JsonProperty("lastname")     public void setLastname(String v)       { this.lastname = v; }
    @JsonProperty("totalprice")   public void setTotalprice(Integer v)    { this.totalprice = v; }
    @JsonProperty("depositpaid")  public void setDepositpaid(Boolean v)   { this.depositpaid = v; }
    @JsonProperty("bookingdates") public void setBookingdates(BookingDates v) { this.bookingdates = v; }
    @JsonProperty("additionalneeds") public void setAdditionalneeds(String v) { this.additionalneeds = v; }

    // 3) Parametresiz constructor
    public Booking() {}

    // 4) Parametreli constructor
    public Booking(String firstname, String lastname, Integer totalprice,
                   Boolean depositpaid, BookingDates bookingdates, String additionalneeds) {
        this.firstname      = firstname;
        this.lastname       = lastname;
        this.totalprice     = totalprice;
        this.depositpaid    = depositpaid;
        this.bookingdates   = bookingdates;
        this.additionalneeds = additionalneeds;
    }

    // 5) toString()
    @Override
    public String toString() {
        return "Booking [firstname=" + firstname + ", lastname=" + lastname +
               ", totalprice=" + totalprice + ", depositpaid=" + depositpaid +
               ", bookingdates=" + bookingdates + ", additionalneeds=" + additionalneeds + "]";
    }
}
```

### Tam BookingDates.java POJO

```java
package techproedturkish01.techproedturkish01api;

import org.codehaus.jackson.annotate.JsonProperty;

public class BookingDates {

    @JsonProperty("checkin")  private String checkin;
    @JsonProperty("checkout") private String checkout;

    @JsonProperty("checkin")  public String getCheckin()  { return checkin; }
    @JsonProperty("checkout") public String getCheckout() { return checkout; }

    @JsonProperty("checkin")  public void setCheckin(String checkin)   { this.checkin = checkin; }
    @JsonProperty("checkout") public void setCheckout(String checkout) { this.checkout = checkout; }

    public BookingDates() {}

    public BookingDates(String checkin, String checkout) {
        this.checkin  = checkin;
        this.checkout = checkout;
    }

    @Override
    public String toString() {
        return "BookingDates [checkin=" + checkin + ", checkout=" + checkout + "]";
    }
}
```

---

## 📦 pom.xml Dependencies {#pom}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                             http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>techproedturkish01</groupId>
  <artifactId>techproedturkish01api</artifactId>
  <version>0.0.1-SNAPSHOT</version>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

  <dependencies>

    <!-- JUnit - Test Framework -->
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.11</version>
    </dependency>

    <!-- REST Assured - API Test Kütüphanesi -->
    <dependency>
      <groupId>io.rest-assured</groupId>
      <artifactId>rest-assured</artifactId>
      <version>4.3.0</version>
    </dependency>

    <!-- org.json - JSONObject için -->
    <dependency>
      <groupId>org.json</groupId>
      <artifactId>json</artifactId>
      <version>20190722</version>
    </dependency>

    <!-- TestNG - SoftAssert için -->
    <dependency>
      <groupId>org.testng</groupId>
      <artifactId>testng</artifactId>
      <version>7.1.0</version>
    </dependency>

    <!-- GSON - Serialization/De-Serialization -->
    <dependency>
      <groupId>com.google.code.gson</groupId>
      <artifactId>gson</artifactId>
      <version>2.8.6</version>
    </dependency>

    <!-- Jackson - ObjectMapper için -->
    <dependency>
      <groupId>org.codehaus.jackson</groupId>
      <artifactId>jackson-mapper-asl</artifactId>
      <version>1.9.13</version>
    </dependency>

    <dependency>
      <groupId>org.codehaus.jackson</groupId>
      <artifactId>jackson-core-asl</artifactId>
      <version>1.9.13</version>
    </dependency>

  </dependencies>
</project>
```

### Purpose of Dependencies

| Kütüphane | Versiyon | Amaç |
|-----------|---------|------|
| `junit` | 4.11 | Test framework, `@Test`, `@Before` |
| `rest-assured` | 4.3.0 | API test kütüphanesi, `given/when/then` |
| `org.json` | 20190722 | `JSONObject` ile body oluşturma |
| `testng` | 7.1.0 | `SoftAssert` için |
| `gson` | 2.8.6 | JSON ↔ Java Object dönüşümü |
| `jackson-mapper-asl` | 1.9.13 | `ObjectMapper`, POJO serialization |

---

## 🏗️ Project Structure {#proje}

```
techproedturkish01api/
├── pom.xml
└── src/
    └── test/
        └── java/
            ├── techproedturkish01/
            │   └── techproedturkish01api/
            │       ├── TestBase.java         ← Common configuration
            │       ├── Booking.java          ← POJO
            │       ├── BookingDates.java     ← POJO
            │       ├── GetRequest04.java
            │       ├── GetRequest05.java
            │       ├── GetRequest06.java
            │       ├── GetRequest07.java
            │       ├── GetRequest08.java
            │       ├── GetRequest09.java
            │       ├── GetRequest10.java
            │       ├── GetRequest11.java
            │       ├── GetRequest12.java
            │       ├── GetRequest13.java
            │       ├── PostRequest01.java
            │       ├── PostRequest02.java
            │       ├── PostRequest03.java
            │       ├── PostRequest04.java
            │       ├── PostRequest05.java
            │       ├── PutRequest01.java
            │       ├── PutRequest02.java
            │       ├── PatchRequest01.java
            │       ├── Delete01.java
            │       ├── ObjectMapperTestWithMap.java
            │       └── ObjectMapperTestWithPojo.java
            └── Utilities/
                └── JsonUtil.java             ← ObjectMapper utility
```

---

## 📋 Full TestBase Class {#testbase-tam}

```java
package techproedturkish01.techproedturkish01api;

import static io.restassured.RestAssured.given;
import java.util.HashMap;
import java.util.Map;
import org.json.JSONObject;
import org.junit.Before;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import io.restassured.specification.RequestSpecification;

public class TestBase {

    protected RequestSpecification spec01;  // restful-booker
    protected RequestSpecification spec02;  // dummy employees
    protected RequestSpecification spec03;  // jsonplaceholder todos

    protected Map<String, String>  bookingDatesMap;
    protected Map<String, Object>  requestBodyMap;
    protected JSONObject           jsonBookingDatesBody;
    protected JSONObject           jsonRequestBody;

    @Before public void setUp01() {
        spec01 = new RequestSpecBuilder()
                     .setBaseUri("https://restful-booker.herokuapp.com")
                     .build();
    }

    @Before public void setUp02() {
        spec02 = new RequestSpecBuilder()
                     .setBaseUri("http://dummy.restapiexample.com/api/v1/employees")
                     .build();
    }

    @Before public void setUp03() {
        spec03 = new RequestSpecBuilder()
                     .setBaseUri("https://jsonplaceholder.typicode.com/todos")
                     .build();
    }

    // JSONObject ile request body oluştur
    protected Response createRequestBodyByJsonObjectClass() {
        jsonBookingDatesBody = new JSONObject();
        jsonBookingDatesBody.put("checkin",  "2020-05-02");
        jsonBookingDatesBody.put("checkout", "2020-05-05");

        jsonRequestBody = new JSONObject();
        jsonRequestBody.put("firstname",       "Kemal");
        jsonRequestBody.put("lastname",        "Can");
        jsonRequestBody.put("totalprice",      888);
        jsonRequestBody.put("depositpaid",     false);
        jsonRequestBody.put("bookingdates",    jsonBookingDatesBody);
        jsonRequestBody.put("additionalneeds", "Wifi");

        return given()
                   .contentType(ContentType.JSON)
                   .spec(spec01)
                   .auth().basic("admin", "password123")
                   .body(jsonRequestBody.toString())
               .when()
                   .post("/booking");
    }

    // HashMap ile request body oluştur
    protected Response createRequestBodyByMap() {
        bookingDatesMap = new HashMap<>();
        bookingDatesMap.put("checkin",  "2020-05-02");
        bookingDatesMap.put("checkout", "2020-05-05");

        requestBodyMap = new HashMap<>();
        requestBodyMap.put("firstname",       "Ahmet");
        requestBodyMap.put("lastname",        "Yildiz");
        requestBodyMap.put("totalprice",      123);
        requestBodyMap.put("depositpaid",     true);
        requestBodyMap.put("bookingdates",    bookingDatesMap);
        requestBodyMap.put("additionalneeds", "Wifi");

        return given()
                   .contentType(ContentType.JSON)
                   .spec(spec01)
                   .auth().basic("admin", "password123")
                   .body(requestBodyMap)
               .when()
                   .post("/booking");
    }
}
```

---

## 🏋️ Practice Exercises {#alıştırmalar}

### Alıştırma 1
Aşağıdaki JSON için POJO oluşturun:
```json
{
  "userId": 1,
  "id": 2,
  "title": "sample task",
  "completed": false
}
```

### Alıştırma 2
`jsonschema2pojo.org` sitesini kullanarak şu JSON için otomatik POJO üretin ve koda ekleyin:
```json
{
  "name": "John",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "NYC"
  }
}
```

---

*✅ API Testing kursu tamamlandı!*

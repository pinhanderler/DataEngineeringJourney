# 🌐 Gün 2 — JsonPath, SoftAssert & GSON

> **TechProEd | API Testing with Rest Assured — Summer 2020**

---

## 📚 İçindekiler

1. [JsonPath Nedir?](#jsonpath)
2. [GetRequest08 — JsonPath ile Doğrulama](#getrequest08)
3. [SoftAssert vs HardAssert](#softassert)
4. [GetRequest09 — SoftAssert & Liste](#getrequest09)
5. [GetRequest10 — Filtreleme ile Liste](#getrequest10)
6. [GSON — Serialization & De-Serialization](#gson)
7. [GetRequest11 — HashMap ile](#getrequest11)
8. [GetRequest12 — List of Maps](#getrequest12)
9. [GetRequest13 — 3 Farklı Yol](#getrequest13)
10. [Alıştırmalar](#alıştırmalar)

---

## 🔷 JsonPath Nedir? {#jsonpath}

**JsonPath**, JSON formatındaki verilerin içinde gezmeyi kolaylaştıran bir kütüphanedir.

```java
JsonPath json = response.jsonPath();

// Tek değer al
json.getString("firstname")         // → "Jim"
json.getInt("totalprice")           // → 596
json.getBoolean("depositpaid")      // → false

// İç içe JSON
json.getString("bookingdates.checkin")  // → "2015-06-07"

// Liste
json.getList("data.employee_name")      // → ["Tiger Nixon", ...]

// İndeksli erişim
json.getString("data[0].employee_name") // → "Tiger Nixon"
json.getString("data[1].employee_name") // → "Garrett Winters"
```

---

## 📋 GetRequest08 — JsonPath ile Doğrulama {#getrequest08}

**pathParam** kullanımı ve JsonPath ile `assertEquals`:

```java
package techproedturkish01.techproedturkish01api;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

public class GetRequest08 extends TestBase {

    @Test
    public void get01() {

        spec01.pathParam("bookingid", 5);  // ← path parametresi ayarla

        Response response = given()
                                .spec(spec01)
                            .when()
                                .get("/booking/{bookingid}");  // ← {bookingid} yerine 5 gelir

        response.prettyPrint();

        JsonPath json = response.jsonPath();  // ← JsonPath objesi oluştur

        // Hard Assertion ile doğrulama
        System.out.println(json.getString("firstname"));
        assertEquals("firstname istenilen gibi değil", "Jim", json.getString("firstname"));

        System.out.println(json.getString("lastname"));
        assertEquals("lastname istenilen gibi değil", "Jones", json.getString("lastname"));

        System.out.println(json.getInt("totalprice"));
        assertEquals("totalprice istenilen gibi değil", 596, json.getInt("totalprice"));

        System.out.println(json.getBoolean("depositpaid"));
        assertEquals("depositpaid istenilen gibi değil", true, json.getBoolean("depositpaid"));

        System.out.println(json.getString("bookingdates.checkin"));
        assertEquals("checkin istenilen gibi değil", "2019-07-20",
                     json.getString("bookingdates.checkin"));

        System.out.println(json.getString("bookingdates.checkout"));
        assertEquals("checkout istenilen gibi değil", "2019-05-18",
                     json.getString("bookingdates.checkout"));
    }
}
```

---

## 🆚 SoftAssert vs HardAssert {#softassert}

| Özellik | Hard Assertion (`assertEquals`) | Soft Assertion (`SoftAssert`) |
|---------|--------------------------------|-------------------------------|
| Hata olunca | ❌ Test hemen durur | ✅ Devam eder, sonunda raporlar |
| Kullanım amacı | Kritik kontroller | Birden fazla kontrol |
| assertAll() | Gerekmiyor | ✅ Sonunda çağrılmalı |
| Kütüphane | JUnit | TestNG |

### SoftAssert 3 Adımı:
```java
// 1) SoftAssert objesi oluştur
SoftAssert softAssert = new SoftAssert();

// 2) Doğrulama yap
softAssert.assertEquals(actual, expected, "mesaj");
softAssert.assertTrue(koşul, "mesaj");

// 3) Sonunda mutlaka çağır!
softAssert.assertAll();
```

---

## 📋 GetRequest09 — SoftAssert & Liste {#getrequest09}

```java
package techproedturkish01.techproedturkish01api;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import org.testng.asserts.SoftAssert;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;
import static io.restassured.RestAssured.*;

public class GetRequest09 extends TestBase {

    @Test
    public void get01() {
        Response response = given()
                                .spec(spec02)
                            .when()
                                .get();

        response.prettyPrint();

        JsonPath json = response.jsonPath();

        // Tüm çalışan isimlerini yazdır
        System.out.println(json.getList("data.employee_name"));

        // Hard Assertion (verify değil assertion → kötü)
        assertEquals("isim istenilen gibi değil", "Garrett Winters",
                     json.getString("data[1].employee_name"));

        // Soft Assertion ile verify (3 adım!)
        SoftAssert softAssert = new SoftAssert();

        // 2. çalışanın adı Garrett Winters mı?
        softAssert.assertEquals(json.getString("data[1].employee_name"),
                                "Garrett Winters",
                                "İsim istenilen gibi değil");

        // Herrod Chandler listede var mı?
        softAssert.assertTrue(
            json.getList("data.employee_name").contains("Herrod Chandler"),
            "Herrod Chandler yok"
        );

        // 24 çalışan var mı?
        softAssert.assertEquals(json.getList("data.id").size(), 24, "24 çalışan yok");

        // 7. çalışanın (index 6) maaşı 137500 mı?
        softAssert.assertEquals(json.getString("data[6].employee_salary"),
                                "137500",
                                "Maaş istenilen gibi değil");

        softAssert.assertAll(); // ← UNUTMA!
    }
}
```

---

## 📋 GetRequest10 — Filtreleme ile Liste {#getrequest10}

**GPath** (Groovy Path) kullanarak JSON içinde filtreleme:

```java
package techproedturkish01.techproedturkish01api;

import org.junit.Test;
import org.testng.asserts.SoftAssert;
import static io.restassured.RestAssured.*;
import java.util.Collections;
import java.util.List;
import io.restassured.path.json.JsonPath;
import io.restassured.response.Response;

public class GetRequest10 extends TestBase {

    @Test
    public void get01() {
        Response response = given()
                                .spec(spec02)
                            .when()
                                .get();

        response.then().assertThat().statusCode(200);

        JsonPath json = response.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        // 1) ID'si 10'dan büyük olanları filtrele
        List<String> idList = json.getList(
            "data.findAll{Integer.valueOf(it.id)>10}.id"  // ← GPath filtresi
        );
        System.out.println("ID > 10: " + idList);
        softAssert.assertEquals(idList.size(), 14, "Eleman sayısı istenilen gibi değil");

        // 2) Yaşı 30'dan küçük olanları filtrele
        List<String> yasList = json.getList(
            "data.findAll{Integer.valueOf(it.employee_age)<30}.employee_age"
        );
        System.out.println("Yaş < 30: " + yasList);
        Collections.sort(yasList);  // Sırala: [19, 21, 22, 22, 23, 23]
        // En büyük yaşın 23 olduğunu doğrula
        softAssert.assertTrue(
            yasList.get(yasList.size()-1).equals("23"),
            "Yaş istenilen gibi değil"
        );

        softAssert.assertAll();
    }
}
```

### 🔍 GPath Filtre Sözdizimi

```
"data.findAll{koşul}.alan"

Örnekler:
"data.findAll{Integer.valueOf(it.id)>10}.id"
"data.findAll{Integer.valueOf(it.employee_age)<30}.employee_age"
"data.findAll{Integer.valueOf(it.employee_salary)>350000}.employee_name"
```

---

## 🔷 GSON — Serialization & De-Serialization {#gson}

**GSON**, JSON ↔ Java Object dönüşümü yapar.

```
JSON  →  Java Object  =  De-Serialization
Java Object  →  JSON  =  Serialization
```

| Yön | İsim | Açıklama |
|-----|------|----------|
| JSON → Java | De-Serialization | `response.as(HashMap.class)` |
| Java → JSON | Serialization | `new Gson().toJson(map)` |

---

## 📋 GetRequest11 — HashMap ile De-Serialization {#getrequest11}

```java
package techproedturkish01.techproedturkish01api;

import static io.restassured.RestAssured.given;
import java.util.HashMap;
import org.junit.Test;
import org.testng.asserts.SoftAssert;
import com.google.gson.Gson;
import io.restassured.response.Response;

public class GetRequest11 extends TestBase {

    @Test
    public void get01() {
        Response response = given()
                                .spec(spec03)
                            .when()
                                .get("/2");

        response.prettyPrint();

        // De-Serialization: JSON → HashMap
        HashMap<String, Object> map = response.as(HashMap.class);
        System.out.println(map);
        System.out.println(map.keySet());   // [id, completed, title, userId]
        System.out.println(map.values());   // [2.0, false, quis ut..., 1.0]

        SoftAssert softAssert = new SoftAssert();

        softAssert.assertEquals(map.get("completed"), false, "false olmalıydı");
        softAssert.assertEquals(map.get("userId"), 1.0, "userId istenilen gibi değil");
        softAssert.assertEquals(map.get("id"), 2.0);
        softAssert.assertEquals(map.get("title"),
            "quis ut nam facilis et officia qui", "title istenilen gibi değil");
        softAssert.assertAll();

        // Serialization: HashMap → JSON
        Gson gson = new Gson();
        String jsonFromMap = gson.toJson(map);
        System.out.println(jsonFromMap);
        // → {"id":2,"completed":false,"title":"quis ut nam facilis et officia qui","userId":1}
    }
}
```

---

## 📋 GetRequest12 — List of Maps {#getrequest12}

```java
public class GetRequest12 extends TestBase {

    @Test
    public void get01() {
        Response response = given()
                                .spec(spec03)
                            .when()
                                .get();

        response.prettyPrint();

        // De-Serialization: JSON Array → List<Map>
        List<Map<String, Object>> listOfMaps = response.as(ArrayList.class);

        SoftAssert softAssert = new SoftAssert();

        // 200 id olduğunu doğrula
        softAssert.assertTrue(listOfMaps.size() == 200, "Id sayısı istenilen gibi değil");

        // 121. elemanın (index 120) completed değeri true mu?
        softAssert.assertEquals(listOfMaps.get(120).get("completed"), true, "İstenilen gibi değil");

        // Sondan bir önceki elemanın title'ı
        softAssert.assertEquals(
            listOfMaps.get(listOfMaps.size()-2).get("title"),
            "numquam repellendus a magnam"
        );

        softAssert.assertAll();
    }
}
```

---

## 📋 GetRequest13 — 3 Farklı Doğrulama Yolu {#getrequest13}

```java
public class GetRequest13 extends TestBase {

    @Test
    public void get01() {
        Response response = given()
                                .spec(spec02)
                            .when()
                                .get();

        JsonPath json = response.jsonPath();
        SoftAssert softAssert = new SoftAssert();

        // ❌ 1. Yol — Tavsiye Edilmez (tekrarlı kod)
        softAssert.assertEquals(json.getString("data[0].employee_name"), "Tiger Nixon");
        softAssert.assertEquals(json.getString("data[1].employee_name"), "Garrett Winters");
        softAssert.assertEquals(json.getString("data[2].employee_name"), "Ashton Cox");
        softAssert.assertEquals(json.getString("data[3].employee_name"), "Cedric Kelly");
        softAssert.assertEquals(json.getString("data[4].employee_name"), "Airi Satou");

        // ⚠️ 2. Yol — Döngü ile (daha iyi)
        List<String> isimList = new ArrayList<>();
        isimList.add("Tiger Nixon");
        isimList.add("Garrett Winters");
        isimList.add("Ashton Cox");
        isimList.add("Cedric Kelly");
        isimList.add("Airi Satou");

        for (int i = 0; i < isimList.size(); i++) {
            softAssert.assertEquals(
                json.getString("data[" + i + "].employee_name"),
                isimList.get(i)
            );
        }

        // ✅ 3. Yol — Map ile (En İyi!)
        List<Map> actualList = json.getList("data");

        Map<Integer, String> expectedMap = new HashMap<>();
        expectedMap.put(0, "Tiger Nixon");
        expectedMap.put(1, "Garrett Winters");
        expectedMap.put(2, "Ashton Cox");
        expectedMap.put(3, "Cedric Kelly");
        expectedMap.put(4, "Airi Satou");

        for (int i = 0; i < expectedMap.size(); i++) {
            softAssert.assertEquals(
                actualList.get(i).get("employee_name"),
                expectedMap.get(i)
            );
        }

        softAssert.assertAll();
    }
}
```

---

## 🏋️ Alıştırmalar {#alıştırmalar}

### Alıştırma 1
`http://dummy.restapiexample.com/api/v1/employees` API'sından:
- Maaşı 350,000'den fazla olan çalışanların isimlerini ekrana yazdır
- Charde Marshall'ın maaşının 350,000'den büyük olduğunu verify et

```java
// Çözüm:
List<String> highSalaryNames = json.getList(
    "data.findAll{Integer.valueOf(it.employee_salary)>350000}.employee_name"
);
System.out.println(highSalaryNames);
softAssert.assertTrue(highSalaryNames.contains("Charde Marshall"),
    "Charde Marshall listede yok");
softAssert.assertAll();
```

### Alıştırma 2
`https://jsonplaceholder.typicode.com/todos/1` adresinden:
- Tüm alanları HashMap'e çevir
- userId = 1 doğrula
- completed = false doğrula
- title doğrula

---

*📌 Sonraki ders: POST Request — 4 Farklı Yol*

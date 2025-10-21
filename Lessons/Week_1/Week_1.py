# ===============================
#  PYTHON DERS 1 - TEMEL ALIŞTIRMALAR
# ===============================

# -------------------------------
# Soru 1: Girilen metnin harflerini alt alta yazdırınız.
# -------------------------------

def soru1():
    metin = input("Metninizi yazınız: ")
    for i, harf in enumerate(metin):
        print(i, harf)


# -------------------------------
# Soru 2: 1-100 arası hem 3'e hem 4'e tam bölünen sayılar
# -------------------------------

def soru2():
    print("1-100 arası hem 3'e hem 4'e tam bölünen sayılar:")
    for i in range(12, 101, 12):
        print(i)


# -------------------------------
# Soru 3: Girilen sayının işaretini belirleme
# -------------------------------

def soru3():
    sayı = float(input("Bir sayı giriniz: "))
    if sayı == 0:
        print("Sıfır")
    elif sayı < 0:
        print("Negatif")
    else:
        print("Pozitif")


# -------------------------------
# Soru 4: Sayı Tahmin Oyunu 
# -------------------------------

def soru4():
    dogru_sayı = 7
    deneme = 0
    while True:
        tahmin = int(input("Bir sayı giriniz: "))
        deneme += 1
        if tahmin < dogru_sayı:
            print("Daha büyük bir sayı giriniz.")
        elif tahmin > dogru_sayı:
            print("Daha küçük bir sayı giriniz.")
        else:
            print(f"Tebrikler! {deneme}. denemede doğru bildiniz ")
            break


# -------------------------------
# Soru 5: Basit Hesap Makinesi 
# -------------------------------

def soru5():
    print("Basit Hesap Makinesi")
    print("İşlemler: +, -, *, /")

    s1 = float(input("Birinci sayıyı gir: "))
    islem = input("İşlem seç (+, -, *, /): ")
    s2 = float(input("İkinci sayıyı gir: "))

    try:
        if islem == "+":
            sonuc = s1 + s2
        elif islem == "-":
            sonuc = s1 - s2
        elif islem == "*":
            sonuc = s1 * s2
        elif islem == "/":
            sonuc = s1 / s2
        else:
            print("Geçersiz işlem seçtiniz!")
            return
        print("Sonuç:", sonuc)
    except ZeroDivisionError:
        print("Hata: Sıfıra bölme yapılamaz!")


# -------------------------------
# Soru 6: Çift/Tek Sayı Kontrolü
# -------------------------------

def soru6():
    sayı = int(input("Bir sayı giriniz: "))
    if sayı == 0:
        print("0 nötr bir sayıdır.")
    elif sayı % 2 == 0:
        print("Çift sayı")
    else:
        print("Tek sayı")


# -------------------------------
# Soru 7: BMI (Vücut Kitle İndeksi)
# -------------------------------

def soru7():
    boy = float(input("Boyunuzu giriniz (metre): "))
    kilo = float(input("Kilonuzu giriniz (kg): "))
    bmi = kilo / (boy ** 2)
    print("BMI:", round(bmi, 2))

    if bmi < 18.5:
        print("Zayıf")
    elif bmi <= 24.9:
        print("Normal")
    elif bmi <= 29.9:
        print("Fazla kilolu")
    else:
        print("Obez")


# -------------------------------
# Soru 8: Öğrenci Yaş Listesi
# -------------------------------

def soru8():
    student = ["Ali", "Ayşe", "Mehmet"]
    age = [14, 15, 14]
    for isim, yas in zip(student, age):
        print(f"{isim} - {yas} yaşında")


# -------------------------------
# Soru 9: Çift Sayıların Karesi
# -------------------------------

def soru9():
    print([i ** 2 for i in range(1, 20) if i % 2 == 0])


# -------------------------------
# Soru 10: Favori Filmler 
# -------------------------------

def soru10():
    film_listesi = [input(f"{i+1}. favori filminizi giriniz: ") for i in range(3)]
    print("\nFilm listeniz:", film_listesi)
    print("İlk film:", film_listesi[0])
    print("Son film:", film_listesi[-1])
    print("Toplam film sayısı:", len(film_listesi))


# -------------------------------
# Soru 11: Sınıf Yoklaması 
# -------------------------------

def soru11():
    öğrenciler = ["Ali", "Ayşe", "Mehmet"]
    gelenler, gelmeyenler = [], []
    for öğrenci in öğrenciler:
        cevap = input(f"{öğrenci} derse geldi mi? (Evet/Hayır): ").lower()
        (gelenler if cevap == "evet" else gelmeyenler).append(öğrenci)
    print("\n--- Yoklama Sonucu ---")
    print("Gelenler:", gelenler)
    print("Gelmeyenler:", gelmeyenler)


# -------------------------------
# Soru 12: Benzersiz Katılımcı Listesi
# -------------------------------

def soru12():
    isimler = ["Ali", "Zeynep", "Ali", "Fatma"]
    print("Benzersiz isimler:", set(isimler))


# -------------------------------
# Soru 13: Kelime Analizi Aracı 
# -------------------------------

from collections import Counter

def soru13():
    sentence = input("Cümle giriniz: ").strip()
    words = sentence.split()
    char_count = len(sentence.replace(" ", ""))
    word_count = len(words)
    unique_words = set(words)
    longest = max(words, key=len)
    freq_word, freq = Counter(words).most_common(1)[0]

    print(f"\nToplam harf: {char_count}")
    print(f"Toplam kelime: {word_count}")
    print(f"Eşsiz kelimeler: {sorted(unique_words)}")
    print(f"En uzun kelime: {longest}")
    print(f"En sık geçen kelime: {freq_word} ({freq} kez)")


# -------------------------------
# Soru 14: Harf Sayacı
# -------------------------------

def soru14():
    cumle = input("Cümle giriniz: ").lower()
    sayac = {}
    for harf in cumle:
        if harf.isalpha():
            sayac[harf] = sayac.get(harf, 0) + 1
    print(sayac)


# -------------------------------
# Soru 15: Kullanıcı Bilgi Kartı 
# -------------------------------

def soru15():
    bilgi = {
        "ad": input("Ad: ").title(),
        "soyad": input("Soyad: ").title(),
        "yas": input("Yaş: "),
        "sehir": input("Şehir: ").title()
    }
    print(f"\nMerhaba {bilgi['ad']} {bilgi['soyad']}, "
          f"{bilgi['yas']} yaşındasın ve {bilgi['sehir']}'da yaşıyorsun.")


# -------------------------------
# Soru 16: Mini Market Sepeti 
# -------------------------------

def soru16():
    products = {"apple": 3, "banana": 5, "bread": 2, "milk": 4}
    basket, total = [], 0

    print("Mini Market (Çıkmak için 'exit' yazın)\n")
    while True:
        item = input("Ürün ekle: ").lower()
        if item == "exit":
            break
        elif item in products:
            basket.append(item)
            total += products[item]
            print(f"{item} eklendi ({products[item]} €)")
        else:
            print("Ürün bulunamadı!")

    print("\nSepetiniz:", ", ".join(basket))
    print(f"Toplam fiyat: {total} €")


# -------------------------------
# Ana Menü
# -------------------------------

def menu():
    while True:
        print("\n=== PYTHON ALIŞTIRMALAR MENÜ ===")
        print("1-16 arası soru numarası girin, '0' çıkış yapar.")
        secim = input("Seçim: ")
        if secim == "0":
            print("Programdan çıkılıyor...")
            break
        elif secim.isdigit() and 1 <= int(secim) <= 16:
            globals()[f"soru{secim}"]()
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    menu()

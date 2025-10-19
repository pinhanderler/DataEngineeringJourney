# ===========================================
#  PYTHON 3 DERSLERİ - ÖZET (YAZILIM BİLİMİ)
# ===========================================


# -------------------------------------------
#   PYTHON'A GİRİŞ ve KURULUM
# -------------------------------------------
# Python 3'ü https://python.org adresinden indirebilirsin.
# IDLE veya VSCode gibi bir editörle çalışabilirsin.
print("Merhaba Python!")  # İlk program


# -------------------------------------------
#   MATEMATİK İŞLEMLERİ
# -------------------------------------------
print(3 + 5)     # Toplama
print(10 - 4)    # Çıkarma
print(2 * 3)     # Çarpma
print(8 / 2)     # Bölme (float döner)
print(8 // 3)    # Tam sayı bölme
print(2 ** 3)    # Üs alma
print(10 % 3)    # Mod alma (kalan)

# İşlem önceliği: Parantez -> Üs -> Çarpma/Bölme -> Toplama/Çıkarma
print((2 + 3) * 4)  # 20


# -------------------------------------------
#   STRİNGLER (METİNLER)
# -------------------------------------------
isim = "Gamze"
print(isim)
print("Merhaba " + isim)
print('Python öğreniyorum!')
metin = """Bu
çok
satırlı
bir stringdir."""
print(metin)


# -------------------------------------------
#   PRINT FONKSİYONU
# -------------------------------------------
print("Python", "Java", "C++")             # Varsayılan aralık boşluk
print("Python", "Java", sep="-")           # Ayracı değiştir
print("Satır bitimi", end="...")           # Satır sonunu değiştir
print("Bitti!")


# -------------------------------------------
#   STRING İŞLEMLERİ
# -------------------------------------------
kelime = "Python"
print(len(kelime))      # Uzunluk
print(kelime[0])        # İlk karakter
print(kelime[-1])       # Son karakter
print(kelime[0:3])      # Dilimleme (0'dan 3'e kadar)
print(kelime * 3)       # Tekrarlama
print(kelime + "3")     # Birleştirme


# -------------------------------------------
#   DEĞİŞKENLER
# -------------------------------------------
x = 10
y = 5
isim = "Gamze"
print(x + y)
print("Merhaba", isim)
# Değişken isimleri: harf veya alt çizgi ile başlar, boşluk içermez.


# -------------------------------------------
#   LİSTELER
# -------------------------------------------
liste = [1, 2, 3, "elma", "armut"]
print(liste)
print(liste[0])      # İlk eleman
liste.append("muz")  # Eleman ekleme
print(liste)
liste.remove(2)      # Eleman silme
print(liste)
print(len(liste))    # Uzunluk


# -------------------------------------------
#    input() ve format()
# -------------------------------------------
# Kullanıcıdan veri alma
# isim = input("Adınızı girin: ")
# yaş = int(input("Yaşınızı girin: "))
# print("Merhaba {}, {} yaşındasınız.".format(isim, yaş))


# -------------------------------------------
#   KOŞULLU DURUMLAR (if-elif-else)
# -------------------------------------------
sayi = 10
if sayi > 0:
    print("Pozitif sayı")
elif sayi == 0:
    print("Sıfır")
else:
    print("Negatif sayı")


# -------------------------------------------
#   KOŞULLU DURUM ÖRNEĞİ
# -------------------------------------------
not_ort = 65
if not_ort >= 50:
    print("Tebrikler, geçtiniz!")
else:
    print("Üzgünüm, kaldınız.")


# -------------------------------------------
#   WHILE DÖNGÜSÜ
# -------------------------------------------
sayaç = 1
while sayaç <= 5:
    print("Sayı:", sayaç)
    sayaç += 1  # sayaç = sayaç + 1


# -------------------------------------------
#   WHILE DÖNGÜSÜ ÖRNEĞİ
# -------------------------------------------
# Basit tahmin oyunu
# gizli = 7
# tahmin = 0
# while tahmin != gizli:
#     tahmin = int(input("Tahmininiz: "))
#     if tahmin < gizli:
#         print("Daha büyük bir sayı deneyin.")
#     elif tahmin > gizli:
#         print("Daha küçük bir sayı deneyin.")
# print("Tebrikler! Bildiniz.")


# -------------------------------------------
#   FOR DÖNGÜSÜ
# -------------------------------------------
for i in range(5):  # 0,1,2,3,4
    print("i:", i)

for meyve in ["elma", "armut", "muz"]:
    print("Meyve:", meyve)


# -------------------------------------------
#   FOR DÖNGÜSÜ ÖRNEĞİ
# -------------------------------------------
toplam = 0
for i in range(1, 6):
    toplam += i
print("1'den 5'e kadar toplam:", toplam)


# -------------------------------------------
#   BREAK ve CONTINUE
# -------------------------------------------
for i in range(1, 10):
    if i == 5:
        continue  # 5'i atla
    if i == 8:
        break     # 8'de döngüyü kes
    print("i:", i)
print("Döngü bitti.")


# -------------------------------------------
#   RANDOM MODÜLÜ
# -------------------------------------------
import random
rastgele_sayi = random.randint(1, 10)
print("1-10 arasında rastgele sayı:", rastgele_sayi)

liste = ["elma", "armut", "muz"]
secim = random.choice(liste)
print("Rastgele meyve:", secim)
import os
import time
import üye_işlemleri
import kitap_işlemleri

# Terminali temizle
def temizle():
    os.system('cls' if os.name == 'nt' else 'clear')

# Ana menü
def ana_menu():
    temizle()
    print("=" * 80)
    print(f"{'KÜTÜPHANE OTOMASYONU':^80}")
    print("=" * 80)
    print("1 - Üye İşlemleri")
    print("2 - Kitap İşlemleri")
    print("0 - Çıkış")
    print("=" * 80)

# Üye işlemleri menüsü
def uye_menu():
    temizle()
    print("=" * 80)
    print(f"{'ÜYE İŞLEMLERİ':^80}")
    print("=" * 80)
    print("1 - Üyeleri Listele")
    print("2 - Üye Ekle")
    print("3 - Üye Güncelle")
    print("4 - Üye Sil")
    print("5 - Kitap Ödünç Ver")
    print("6 - Kitap Teslim Al")
    print("0 - Ana Menüye Dön")
    print("=" * 80)

# Kitap işlemleri menüsü
def kitap_menu():
    temizle()
    print("=" * 80)
    print(f"{'KİTAP İŞLEMLERİ':^80}")
    print("=" * 80)
    print("1 - Kitapları Listele")
    print("2 - Kitap Ara")
    print("3 - Kitap Ekle")
    print("4 - Kitap Sil")
    print("0 - Ana Menüye Dön")
    print("=" * 80)

# Ana akış
def calistir():
    while True:
        ana_menu()
        secim = input("Lütfen işlem numarasını giriniz: ").strip()

        if secim == "1":  # Üye İşlemleri
            while True:
                uye_menu()
                secim_uye = input("Lütfen işlem numarasını giriniz: ").strip()

                if secim_uye == "1":
                    üye_işlemleri.uyeleri_listele()
                elif secim_uye == "2":
                    uye_id = input("Üye ID: ").strip()
                    ad_soyad = input("Ad Soyad: ").strip()
                    adres = input("Adres: ").strip()
                    telefon = input("Telefon: ").strip()
                    üye_işlemleri.uye_ekle(uye_id, ad_soyad, adres, telefon)
                elif secim_uye == "3":
                    uye_id = input("Güncellenecek üye ID: ").strip()
                    üye_işlemleri.uye_guncelle(uye_id)
                elif secim_uye == "4":
                    uye_id = input("Silinecek üye ID: ").strip()
                    üye_işlemleri.uye_sil(uye_id)
                elif secim_uye == "5":
                    uye_id = input("Kitap verilecek üye ID: ").strip()
                    üye_işlemleri.kitap_odunc_ver(uye_id)
                elif secim_uye == "6":
                    uye_id = input("Kitap teslim alınacak üye ID: ").strip()
                    üye_işlemleri.kitap_teslim_al(uye_id)
                elif secim_uye == "0":
                    break
                else:
                    print(" Geçersiz seçim. Lütfen 0-6 arasında bir değer giriniz.")
                input("\nDevam etmek için Enter'a basın...")

        elif secim == "2":  # Kitap İşlemleri
            while True:
                kitap_menu()
                secim_kitap = input("Lütfen işlem numarasını giriniz: ").strip()

                if secim_kitap == "1":
                    kitap_işlemleri.kitaplari_listele()
                elif secim_kitap == "2":
                    aranan = input("Aranacak kelime (kitap adı veya yazar): ").strip()
                    kitap_işlemleri.kitap_ara(aranan)
                elif secim_kitap == "3":
                    try:
                        barkod = input("Barkod: ").strip()
                        ad = input("Kitap Adı: ").strip()
                        yazar = input("Yazar: ").strip()
                        fiyat = float(input("Fiyat: ").strip())
                        yayinevi = input("Yayınevi: ").strip()
                        dil = input("Dil (varsayılan Türkçe): ").strip() or "Türkçe"
                        kitap_işlemleri.kitap_ekle(barkod, ad, yazar, fiyat, yayinevi, dil)
                    except ValueError:
                        print(" Hatalı giriş! Fiyat ondalıklı sayı olmalıdır.")
                elif secim_kitap == "4":
                    barkod = input("Silinecek kitabın barkodu: ").strip()
                    kitap_işlemleri.kitap_sil(barkod)
                elif secim_kitap == "0":
                    break
                else:
                    print(" Geçersiz seçim. Lütfen 0-4 arasında bir değer giriniz.")
                input("\nDevam etmek için Enter'a basın...")

        elif secim == "0":
            print(" Kütüphane sisteminden çıkılıyor, iyi günler dileriz...")
            time.sleep(1)
            break
        else:
            print("Geçersiz seçim. Lütfen 0-2 arasında bir değer giriniz.")
            input("\nDevam etmek için Enter'a basın...")

# Programı çalıştır
if __name__ == "__main__":
    calistir()

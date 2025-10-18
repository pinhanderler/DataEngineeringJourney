import json
import os
from datetime import datetime, timedelta

# JSON dosyasının adı
DOSYA_ADI = os.path.join(os.path.dirname(__file__), "uye.json")

# Türkçe hafta günü isimleri
TURKCE_GUNLER = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# JSON dosyasını oku
def dosya_oku():
    if not os.path.exists(DOSYA_ADI):
        print("uye.json bulunamadı, yeni dosya oluşturuluyor...")
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=4)
        return []
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("JSON formatı beklenenden farklı. Boş listeyle başlatılıyor.")
                return []
    except json.JSONDecodeError:
        print("JSON dosyası okunamadı. Boş listeyle devam ediliyor.")
        return []

# JSON dosyasına yaz
def dosya_yaz(veri):
    with open(DOSYA_ADI, "w", encoding="utf-8") as f:
        json.dump(veri, f, ensure_ascii=False, indent=4)

# Üyeleri listele
def uyeleri_listele():
    uyeler = dosya_oku()
    if not uyeler:
        print("Henüz kayıtlı üye bulunmuyor.")
        return
    print(f"\nToplam {len(uyeler)} üye listelendi:\n")
    for u in uyeler:
        print(f"ID: {u.get('Uye_ID', '-') } | Ad Soyad: {u.get('Ad_Soyad', '-') } | "
              f"Adres: {u.get('Adres', '-') } | Telefon: {u.get('Telefon', '-') } | "
              f"Kayıt Tarihi: {u.get('Kayit_Tarihi', '-')}")
        odunclar = u.get("Odunc_Kitaplar", []) or []
        if odunclar:
            for k in odunclar:
                kitap_adi = k.get('Kitap_Adi', 'Bilinmiyor')
                alis = k.get('Alis_Tarihi', '-')
                teslim = k.get('Teslim_Tarihi', '-')
                teslim_gunu = k.get('Teslim_Gunu', '-')
                print(f"   📘 {kitap_adi} - Alış: {alis} - Teslim: {teslim} ({teslim_gunu})")
        print("-" * 70)

# Üye ekle
def uye_ekle(uye_id, ad_soyad, adres, telefon):
    uyeler = dosya_oku()
    if any(str(u.get("Uye_ID")) == str(uye_id) for u in uyeler):
        print("Bu ID ile kayıtlı bir üye zaten var!")
        return
    if not ad_soyad or not adres or not telefon:
        print("Eksik bilgi! Lütfen tüm alanları doldurunuz.")
        return

    yeni_uye = {
        "Uye_ID": str(uye_id),
        "Ad_Soyad": ad_soyad,
        "Adres": adres,
        "Telefon": telefon,
        "Kayit_Tarihi": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Odunc_Kitaplar": []
    }
    uyeler.append(yeni_uye)
    dosya_yaz(uyeler)
    print(f"'{ad_soyad}' adlı üye başarıyla eklendi.")

# Üye güncelle
def uye_guncelle(uye_id):
    uyeler = dosya_oku()
    for u in uyeler:
        if str(u.get("Uye_ID")) == str(uye_id):
            print(f"Güncellenecek üye bulundu: {u.get('Ad_Soyad')}")
            yeni_adres = input("Yeni adres (boş bırakırsan değişmez): ").strip()
            yeni_telefon = input("Yeni telefon (boş bırakırsan değişmez): ").strip()
            if yeni_adres:
                u["Adres"] = yeni_adres
            if yeni_telefon:
                u["Telefon"] = yeni_telefon
            dosya_yaz(uyeler)
            print("Üye bilgileri güncellendi.")
            return
    print("Bu ID ile kayıtlı bir üye bulunamadı.")

# Üye sil
def uye_sil(uye_id):
    uyeler = dosya_oku()
    yeni_liste = [u for u in uyeler if str(u.get("Uye_ID")) != str(uye_id)]
    if len(uyeler) == len(yeni_liste):
        print("Bu ID ile kayıtlı bir üye bulunamadı.")
    else:
        dosya_yaz(yeni_liste)
        print(f"ID {uye_id} olan üye başarıyla silindi.")

# Kitap ödünç verme
def kitap_odunc_ver(uye_id):
    uyeler = dosya_oku()
    for u in uyeler:
        if str(u.get("Uye_ID")) == str(uye_id):
            kitap_adi = input("Kitap adı: ").strip()
            if not kitap_adi:
                print("Kitap adı boş olamaz.")
                return

            # Teslim tarihi otomatik hesapla (14 gün sonrası)
            teslim_tarihi = datetime.now() + timedelta(days=14)
            teslim_str = teslim_tarihi.strftime("%Y-%m-%d")
            # Türkçe gün ismi
            teslim_gunu = TURKCE_GUNLER[teslim_tarihi.weekday()]

            odunc = {
                "Kitap_Adi": kitap_adi,
                "Alis_Tarihi": datetime.now().strftime("%Y-%m-%d"),
                "Teslim_Tarihi": teslim_str,
                "Teslim_Gunu": teslim_gunu
            }

            # Ensure field exists
            if "Odunc_Kitaplar" not in u or u["Odunc_Kitaplar"] is None:
                u["Odunc_Kitaplar"] = []

            u["Odunc_Kitaplar"].append(odunc)
            dosya_yaz(uyeler)

            print(f"'{kitap_adi}' adlı kitap {u.get('Ad_Soyad', 'Üye')} adlı üyeye ödünç verildi.")
            print(f"Teslim tarihi: {teslim_str} ({teslim_gunu})")
            return
    print("Bu ID ile kayıtlı bir üye bulunamadı.")

# Kitap teslim alma
def kitap_teslim_al(uye_id):
    uyeler = dosya_oku()
    for u in uyeler:
        if str(u.get("Uye_ID")) == str(uye_id):
            odunclar = u.get("Odunc_Kitaplar", []) or []
            if not odunclar:
                print("Bu üyenin ödünç aldığı kitap yok.")
                return
            print("Ödünç alınan kitaplar:")
            for i, k in enumerate(odunclar, 1):
                kitap_adi = k.get('Kitap_Adi', 'Bilinmiyor')
                teslim = k.get('Teslim_Tarihi', '-')
                teslim_gunu = k.get('Teslim_Gunu', '-')
                print(f"{i}. {kitap_adi} (Teslim Tarihi: {teslim} - {teslim_gunu})")
            secim = input("Teslim alınacak kitabın numarası: ").strip()
            if secim.isdigit() and 1 <= int(secim) <= len(odunclar):
                kitap = odunclar.pop(int(secim)-1)
                # Teslim tarihi kontrolü
                try:
                    teslim_gunu_dt = datetime.strptime(kitap.get("Teslim_Tarihi", ""), "%Y-%m-%d")
                    fark = (datetime.now().date() - teslim_gunu_dt.date()).days
                except Exception:
                    fark = 0
                if fark > 0:
                    print(f"Kitap {fark} gün geç teslim edildi. Ceza uygulanabilir.")
                print(f"'{kitap.get('Kitap_Adi', 'Bilinmiyor')}' kitabı teslim alındı.")
                # Güncellenmiş listeleri kaydet
                u["Odunc_Kitaplar"] = odunclar
                dosya_yaz(uyeler)
                return
            else:
                print("Geçersiz seçim.")
                return
    print("Bu ID ile kayıtlı bir üye bulunamadı.")

# Menü
def menu():
    while True:
        print("""
=======  ÜYE VE KİTAP YÖNETİM SİSTEMİ =======
1 - Üyeleri Listele
2 - Üye Ekle
3 - Üye Güncelle
4 - Üye Sil
5 - Kitap Ödünç Ver
6 - Kitap Teslim Al
7 - Çıkış
==============================================
""")
        secim = input("İşlem seçiniz (1-7): ").strip()
        if secim == "1":
            uyeleri_listele()
        elif secim == "2":
            uye_id = input("Üye ID: ").strip()
            ad_soyad = input("Ad Soyad: ").strip()
            adres = input("Adres: ").strip()
            telefon = input("Telefon: ").strip()
            uye_ekle(uye_id, ad_soyad, adres, telefon)
        elif secim == "3":
            uye_id = input("Güncellenecek üye ID: ").strip()
            uye_guncelle(uye_id)
        elif secim == "4":
            uye_id = input("Silinecek üye ID: ").strip()
            uye_sil(uye_id)
        elif secim == "5":
            uye_id = input("Kitap verilecek üye ID: ").strip()
            kitap_odunc_ver(uye_id)
        elif secim == "6":
            uye_id = input("Kitap teslim alınacak üye ID: ").strip()
            kitap_teslim_al(uye_id)
        elif secim == "7":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen 1-7 arasında bir değer giriniz.")

# Programı çalıştır
if __name__ == "__main__":
    menu()
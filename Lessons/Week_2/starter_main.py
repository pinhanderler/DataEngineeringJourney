# Projenin temelini oluşturan modülleri import edin.
# JSON verisi için 'json', 'reduce' fonksiyonu içinse 'functools' modülüne ihtiyacınız olacak.
import json
from functools import reduce


# Görev 1: Veri Okuma ve Hata Yönetimi
# 'urunler.json' dosyasını okuyacak bir fonksiyon tanımlayın.
# Fonksiyonunuz, dosya bulunamazsa veya JSON formatı bozuksa hata yönetimi yapmalıdır.
# İpucu: 'try-except' ve 'with open()' yapılarını kullanın.
def read_data(filename):
    #Belirtilen JSON dosyasını okur ve Python listesine dönüştürür. 
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f" Hata: '{filename}' dosyası bulunamadı.")
        return None
    except json.JSONDecodeError:
        print(f" Hata: '{filename}' dosyasında geçersiz JSON formatı.")
        return None


# Görev 2: Veri Analizi
# Bu fonksiyon, okunan ürün verilerini işleyecektir.
def analyze_data(products):
    """
    Ürünler listesi üzerinde filtreleme, map ve reduce işlemleri yapar.
    """
    # a) Stok miktarı 50'nin altında olan ürünleri filtreleyin.
    #    'filter()' ve 'lambda' kullanın.
    #    low_stock_products = list(...)
    low_stock_products = list(filter(lambda x: x['stok'] < 50, products))  
    low_stock_products_name = list(filter(lambda x: (x['ad'], x['stok']), low_stock_products))
    print(low_stock_products_name) 

    # b) Tüm ürünlerin fiyatlarına %20 KDV ekleyin.
    #    'map()' ve 'lambda' kullanın.
    prices_with_kdv = list(map(lambda x: round(x.get('fiyat', 0) * 1.20, 2), products))
    
    # c) Tüm ürünlerin toplam stok sayısını hesaplayın.
    #    'reduce()' kullanın.

    total_stock = reduce(lambda x, y: x + y, map(lambda p: p.get('stok', 0), products))
    #print(sum(x+y))
    

    # Bu üç sonucu geri döndürün.
    return low_stock_products, prices_with_kdv, total_stock


# Görev 3: Veri Kaydetme
def save_data(data, filename):
    """
    Veriyi belirtilen dosyaya JSON formatında kaydeder.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f" Veri '{filename}' dosyasına başarıyla kaydedildi.")
    except Exception as e:
        print(f" Dosya kaydedilirken hata oluştu: {e}")


# Uygulamanın Ana Akışı
if __name__ == "__main__":
    products_data = read_data('urunler.json')

    if products_data:
        # Analiz görevleri
        low_stock_products, prices_with_kdv, total_stock = analyze_data(products_data)

        # Sonuçları ekrana yazdırma
        print("\n Düşük Stoklu Ürünler:")
        print(json.dumps(low_stock_products, indent=2, ensure_ascii=False))

        print("\n KDV Eklenmiş Ürün Fiyatları:")
        print(prices_with_kdv)

        print(f"\n Toplam Stok Sayısı: {total_stock}")

        # Düşük stoklu ürünleri dosyaya kaydetme
        save_data(low_stock_products, 'd_stoklu_urunler.json')
# class Kitap():
#     language = "Turkish"         #sinif niteligi
#     def __init__ (self, name, author , total_page):     #ornek niteligi
#         self.name = name
#         self.author = author
#         self.total_page = total_page
 
    
#     def show_info(self):

#         print(f"{self.name}, {self.author}, {self.total_page}")   #bu seklilde de yapabiliriz

#         # print("Name:", self.name)
#         # print("Author:", self.author)
#         # print("Total_page:", self.total_page)

#     def increase_page(self, added_page):            #sayfa sayisi ekleyecegiz
#         self.total_page = self.total_page + added_page          #self.total_page += added_page
   
   
#     def decrease_page(self, remove_page):            #sayfa sayisi ekleyecegiz
#         if remove_page <= self.total_page:
#             self.total_page -= remove_page
#         else:
#             print("invalid")

  
      
# kitap_1 = Kitap("Sefiller", "Viktor Hugo", 500)
# kitap_2 = Kitap("1984", "George Orwel", 200)

# # print(kitap_1.language)
# # print(kitap_2.name)

# #print(kitap_1.show_info())
# #kitap_1.show_info()

# # kitap_1.increase_page(100)
# # kitap_1.show_info()

# kitap_1.decrease_page(550)
# kitap_1.show_info()


#-------------- Ayri bi sinif olusturuyoruz--------------


class Calisan():
    toplam_calisan = 18             #18 den baslayalim dedik. sifirdan da baslayabilirdik. 
    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas
        Calisan.toplam_calisan += 1         #toplam_calisan butun Calisan sinifinin genel bir ozelligi o yuzden self. degil de Calisan. yazdik

    def bilgileri_goster(self):
        print(f"{self.ad}, {self.soyad}, {self.maas}€/ay")


calisan_1 = Calisan("Ali", "Yilmaz", 2000)          #bunlar birer object
calisan_1.bilgileri_goster()


class Yonetici(Calisan):                    #bu sinifta Calisan dan farkli departman var(fazla parametre)
    def __init__(self, ad, soyad, maas, departman):
        super().__init__(ad, soyad, maas)
        self.departman = departman

    def bilgileri_goster(self):
        print(f"{self.ad}, {self.soyad}, {self.maas}€/ay, {self.departman}")         #bilgileri_goster i yukardan aliyor ama burda self.departman i eklemeliyiz
    

yonetici_1 = Yonetici("Ahmet", "Yilmaz", 4000, "IT")   
yonetici_1.bilgileri_goster()   

class Stajyer(Calisan):             #bu sinifta Calisandan farkli sabit maas var.(eksik parametre)
    toplam_stajyer = 0         #sadece toplam stajyer almak icin
    maas = 200              #butun stajyerlerin maasi 200€ demek
    def __init__(self,ad, soyad):
        super().__init__(ad, soyad, self.maas)      #self.maas yerine 200 de yazabiliriz.
        Stajyer.toplam_stajyer += 1



stajyer_1 = Stajyer("Ayse", "Yener")
stajyer_1.bilgileri_goster()
stajyer_2 = Stajyer("Ali", "veli")

print(Stajyer.toplam_stajyer)           #toplam stajyer sayisini verir

print(Calisan.toplam_calisan)           #tum toplam calisani verir.

import json #JSON modülü

try:
    with open(r"C:\Kodlama\Projeler\1.Proje\liste1.json", "r") as liste1jsondosyasi:
        veri = json.load(liste1jsondosyasi)

    liste1 = veri["liste1"]
    liste2 = veri["liste2"]

except FileNotFoundError:
    print("Dosya bulunamadi.")
except KeyError:
    print("Aranan anahtar JSON dosyasinin içince yok.")
except Exception as err:
    print("Hata!")
else:
    print("Dosya başariyla okundu.")
finally:
    print("Program tamamlandi.")

# Listeleri gezip değerlere bakabiliriz :
for i in liste1:
    print(i,end=" ")

print(" ")

for j in liste2:
    print(j,end=" ")

print("\n\n")

# Küme işlemleri için set'e çevirelim.()
    # Kümeler tekrarli değerleri içermezler. set() fonksiyonu tekrarli değerleri otomatik atar ama ben elle tekrar eden değerleri göstermek istediğim için for döngüsü kullandim çünkü neden olmasin. 
küme1 = set()
tekrar_edenler_kümesi1 = set()

for i in liste1:
    if i not in küme1:
        küme1.add(i)
    else:
        tekrar_edenler_kümesi1.add(i)

print(küme1)
print(tekrar_edenler_kümesi1)

küme2 = set()
tekrar_edenler_kümesi2 = set()

for i in liste2:
    if i not in küme2:
        küme2.add(i)
    else:
        tekrar_edenler_kümesi2.add(i)

print(küme2)
print(tekrar_edenler_kümesi2) # Tekrar eden eleman yok o yüzden boş döndürdü yani set() döndürdü.
print("\n\n\n")

# Süre ölçmek için time kütüphanesini import etmemiz lazim.
import time
# Küme işlemleri :
    # Birleşim -> .union() -- '|' operatörü de kullanilabilir. --
        # Orijinal kümeler değişmez.
        # Ayni eleman varsa birini alir.
basla = time.time()
print("Baslangic Zamani:\t{}".format(basla))

birlesim = küme1.union(küme2)

print("Birleşmiş kümeler : ",birlesim)

bitis = time.time()
print("Bitis Zamani:\t{}".format(bitis))
fark_union = bitis-basla
print("Fark_union :",fark_union)

print("\n\n\n")

    # Kesişim -> intersection() -- '&' operatörü de kullanilabilir. --
        # Sadece ortak elemanlari alir.
        # Orijinal kümeler değişmez.
basla = time.time()
print("Baslangic Zamani:\t{}".format(basla))

kesişim = küme1.intersection(küme2)
print("Kesişim kümeleri :",kesişim)

bitis = time.time()
print("Bitis Zamani:\t{}".format(bitis))
fark_intersection = bitis-basla
print("Fark_intersection :",fark_intersection)
print("\n\n\n")

    # Fark -> difference() -- '-' operatörü de kullanilabilir. --
basla = time.time()
print("Baslangic Zamani:\t{}".format(basla))

fark12 = küme1.difference(küme2)
fark21 = küme2.difference(küme1)
print("küme1 - küme2 :",fark12)
print("(-küme1) + küme2 :",fark21)

bitis = time.time()
print("Bitis Zamani:\t{}".format(bitis))
fark_difference = bitis-basla
print("Fark_difference :",fark_difference)

Süreler_listesi = [fark_union,fark_intersection,fark_difference]

with open(r"C:\Kodlama\Projeler\1.Proje\Sureler.json","w") as f:
    json.dump(Süreler_listesi,f,indent=3)




'''
    Yararlandiğim kaynaklar:
    1-)https://www.geeksforgeeks.org/python/time-functions-in-python-set-1-time-ctime-sleep/
    2-)https://www.geeksforgeeks.org/python/sets-in-python/
    3-)https://medium.com/@ibrahimpuskullu44/pythonda-algoritmalar%C4%B1n-%C3%A7al%C4%B1%C5%9Fma-s%C3%BCrelerini-%C3%B6l%C3%A7mek-timeit-mod%C3%BCl%C3%BC-ile-performans-analizi-f640ec73577a
    4-)ChatGPT
    5-)https://www.geeksforgeeks.org/python/python-json/
    '''

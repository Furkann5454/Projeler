Kullanici_dosyasi = input("Dosya yolunu giriniz :")
# C:\Kodlama\Projeler\2.Proje\sayi.txt

try:
    with open(Kullanici_dosyasi,"r") as file1:
        content = file1.read()
        sayilar = []
        for sayi in content.split():
            sayilar.append(int(sayi))

except FileNotFoundError:
    print("Belirtilen metin dosyasi bulunamadi.")
except ValueError:
    print("Sadece sayi giriniz!")
except Exception as err:
    print("Hata oluştu!")
else:
    print("Dosya başariyla alindi.")
    for i in sayilar:
        print(i,end=" ")
finally:
    print("\nİşlem sonlandi.")

# Sort işlemlerinden biri uygulandiğinda listeler kalici olarak değişir.
    # Bu yüzden kopyalayalim.
liste_bubblesort = sayilar.copy()
liste_selectionsort = sayilar.copy()

import time

def bubbleSort(liste):
    boyut = len(liste)
    print("Listenin boyutu :",boyut)
    süre_baslangic_bubblesort = time.time()
    adim_sayaci_bubblesort = 0
    for i in range(boyut):
        for j in range(boyut-i-1):
            adim_sayaci_bubblesort +=1
            if liste[j] > liste[j+1]:
                temp = liste[j]
                liste[j] = liste[j+1]
                liste[j+1] = temp
    print("Bubble Sort ile siralanmiş hali:", liste,end=" ")
    print("Bubble sort adim sayisi :",adim_sayaci_bubblesort)
    süre_bitis_bubblesort = time.time()
    calisma_süresi_bubblesort = süre_bitis_bubblesort - süre_baslangic_bubblesort
    print(calisma_süresi_bubblesort)
    return adim_sayaci_bubblesort,calisma_süresi_bubblesort


bubbleSort(liste_bubblesort)

# Liste siralanmamiş baktiğimizda :
for i in sayilar:
    print(i,end=" ")


def selectionSort(liste):
    boyut = len(liste)
    print("\nListenin boyutu :",boyut)
    süre_baslangic_selectionsort = time.time()
    adim_sayaci_selectionsort = 0
    for i in range(boyut):
        min_index = i
        for j in range(i+1,boyut):
            adim_sayaci_selectionsort +=1
            if liste[j] < liste[min_index]:
                min_index = j
        temp = liste[i]
        liste[i] = liste[min_index]
        liste[min_index] = temp
    süre_bitis_selectionsort = time.time()
    calisma_süresi_selectionsort = süre_bitis_selectionsort - süre_baslangic_selectionsort
    print("Selection sort ile siralanmiş hali :",liste,end=" ")
    print("Selection sort adim sayisi :",adim_sayaci_selectionsort)
    print(calisma_süresi_selectionsort)
    return adim_sayaci_selectionsort,calisma_süresi_selectionsort

selectionSort(liste_selectionsort)

adim_bubble, sure_bubble = bubbleSort(liste_bubblesort)
adim_selection, sure_selection = selectionSort(liste_selectionsort)

rapor_path = r"C:\Kodlama\Projeler\2.Proje\algoritma_karsilastirma_raporu.txt"

with open(rapor_path, "w") as rapor:
    # Bubble Sort
    for sayi in liste_bubblesort:
        rapor.write(f"{sayi}\n")
    rapor.write(f"Adim sayisi bubblesort :{adim_bubble}\n")
    rapor.write(f"Sure bubblesort{sure_bubble}\n")
    for sayi in liste_selectionsort:
        rapor.write(f"{sayi}\n")
    rapor.write(f"Adim sayisi selectionsort :{adim_selection}\n")
    rapor.write(f"Sure selectionsort :{sure_selection}\n")


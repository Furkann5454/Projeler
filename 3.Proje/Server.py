import zmq
import json
import os

context = zmq.Context()
socket = context.socket(zmq.REP)  
socket.bind("tcp://127.0.0.1:5555") 

print("Sunucu başlatildi, istek bekleniyor...")

dosya = "veriler.json"

def dosya_okuma():
    if os.path.exists(dosya) == False:
        with open(dosya,"w",encoding="utf-8") as dosya1:
            json.dump([],dosya1)
        return []
    else:
        with open (dosya,"r",encoding="utf-8") as dosya2:
            return json.load(dosya2)

def dosya_yazma(veri):
    with open(dosya,"w",encoding="utf-8") as dosya3:
        json.dump(veri,dosya3,indent=4)

kitaplar = dosya_okuma()

while True:
    try:

        mesaj = socket.recv_json()
        print("Gelen mesaj:", mesaj)
    
        istek = mesaj.get("istek")

        if istek == "Kitap_ekleme": # Kitap ekleme işlemi
            baslik = mesaj.get("baslik")
            yazar = mesaj.get("yazar")
            kitaplar.append({
                "baslik":baslik,
                "yazar":yazar,
                "Odunc_durum":False
            })
            dosya_yazma(kitaplar)
            yanit = {"Durum":"Hata yok.","mesaj":"Kitap eklendi."}

        elif istek == "Odunc_alma": # Ödünç alma işlemi.
            baslik = mesaj.get("baslik")
            found = None # Başta boş
            for kitap in kitaplar:
                if kitap["baslik"].lower() == baslik.lower(): # Küçük-Büyük harf kontrolü
                    found = kitap
                    break
            if found:
                if found["Odunc_durum"] == False:
                    found["Odunc_durum"] = True
                    dosya_yazma(kitaplar)
                    yanit = {"Durum": "Başarili", "mesaj": "Kitap ödünç verildi."}
                else:
                    yanit = {"Durum": "Hata", "mesaj": "Kitap zaten ödünçte."}
            else:
                yanit = {"Durum" : "Kitap yok."}

        elif istek == "Kitap_arama": # Kitap arama işlemi.
            baslik = mesaj.get("baslik")
            found = None
            for kitap in kitaplar:
                if kitap["baslik"].lower() == baslik.lower():
                    found = kitap
                    break
            if found:
                yanit = {"Durum": "Bulundu", "kitap": found}
            else:
                yanit = {"Durum": "Bulunamadi"}
    
        elif istek == "Odunc_iade":
            baslik = mesaj.get("baslik")
            found = None

            for kitap in kitaplar:
                if kitap["baslik"].lower() == baslik.lower():
                    found = kitap
                    break
            
            if found:
                if found["Odunc_durum"] == True:
                    found["Odunc_durum"] = False
                    dosya_yazma(kitaplar)
                    yanit = {"Durum": "Başarili", "mesaj": "Ödünç iade işlemi gerçekleştirildi."}
                else:
                        yanit = {"Durum": "Başarisiz", "mesaj": "Kitap zaten hiç ödünç alinmamiş ki."}
            else:
                        yanit = {"Durum": "Başarisiz", "mesaj": "Belirtilen kitap bulunamadi."}

        socket.send_json(yanit) # Yanıtı gönderdik.
    
    except Exception as err:
        print("Hata",err)
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)   
socket.connect("tcp://127.0.0.1:5555")  

def Kitap_ekleme():
    baslik = input("Kitabin başligini giriniz : ")
    yazar = input("Kitabin yazarinin adini giriniz: ")

    istek = {
        "istek": "Kitap_ekleme",
        "baslik": baslik,
        "yazar":yazar
    }

    socket.send_json(istek)
    yanit = socket.recv_json()
    print("Sunucu yaniti : ",yanit)

def Odunc_alma():
    baslik = input("Kitabin basligini giriniz :")

    istek = {
        "istek" : "Odunc_alma",
        "baslik" : baslik
    }
    socket.send_json(istek)
    yanit = socket.recv_json()
    print("Sunucu Ödünç alma işlemi yaniti :",yanit)

def Kitap_arama():
    baslik = input("Kitabin basligini giriniz :")

    istek = {
        "istek": "Kitap_arama",
        "baslik": baslik
    }

    socket.send_json(istek)
    yanit = socket.recv_json()
    print("Sunucu:", yanit)

def Odunc_iade():
    baslik = input("Kitabin basligini giriniz :")
    istek = {
        "istek":"Odunc_iade",
        "baslik":baslik
    }
    socket.send_json(istek)
    yanit = socket.recv_json()
    print("Sunucu:", yanit)


while True:
    for i in range(20):
        print("*",end="")
    print("\n--- Menü ---")
    print("1) Kitap ekle")
    print("2) Odunc al")
    print("3) Kitap ara")
    print("4) Kitap Odunc Iade")
    print("5) Çikis")
    secim = input("Seçim: ")


    match secim:
        case "1":
            Kitap_ekleme()
        case "2":
            Odunc_alma()
        case "3":
            Kitap_arama()
        case "4":
            Odunc_iade()
        case "5":

            break
        case _:
            print("Geçersiz işlem yaptiniz.")
    for i in range(20):
        print("*",end="")

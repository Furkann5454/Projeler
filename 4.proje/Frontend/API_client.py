# --------------PyQt5'ten gelen ID'yi alip Flask'a paketleyip gönderen kisim. -------------
import requests

API_URL = "http://127.0.0.1:5000"

def ucus_verisini_getir(ucus_id):
    try:
        url = f"{API_URL}/ucus/{ucus_id}"
        response = requests.get(url, timeout=5)
        
        if response.status_code == 200:
            return response.json(), None
        elif response.status_code == 404:
            return None, "Uçuş bulunamadi."
        else:
            return None, f"Sunucu hatasi: {response.status_code}"
            
    except requests.exceptions.ConnectionError:
        return None, "Flask sunucusu kapali veya bağlanti reddedildi."
    except Exception as e:
        return None, f"Bir hata oluştu: {str(e)}"
    
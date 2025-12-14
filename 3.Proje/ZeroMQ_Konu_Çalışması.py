import zmq # ZeroMQ'yu kullanmak için import ederiz.
import json # JSON import ettik.

# ZeroMQ socket bağlantı işlemini çok kolaylaştıran bir mesajlaşma kütüphanesidir.
    # Send - Recieve işlemleri çok hızlı olur.
    # Kolay ölçeklendirilebilir.
    # Server-client, publish-subscribe, worker pool gibi farklı mimariler sağlar.
    # Broker(Özel bir sunucu)'ya ihtiyaç olmaz. Böylece daha basit ve hızlı çalışır.
    # Sıfır gecikme ve Sıfır maliyet amaçlanmıştır.Açık kaynak yazılımlıdır.

# Context nedir ?
    # ZeroMQ kütüphanesinde bütün soketlerin yaşadığı ortamdır.
    # Soketlerin birbirine bağlanmasını sağlar.
    # Arka planda çekirdek yönetimi yapar ve üretim/dağıtım iletişim ağını sağlar.

context = zmq.Context # 1 Programda 1 context kullanılır.

# Socket nedir ?
    # Python Socket'i gibidir ama daha güçlüdür.
    # REQ , REP , PUB , SUB vs. her biri farklı iletişim şekli sağlar.
    
    # REQ , REP --> Bir istemci REQ ile bir istek gönderir ve sunucu REP ile işler ve yanıt döner.
    # İstemci bir yanıt gelene kadar bekler.

    # PUB , SUB --> Bir kaynağın birden çok alıcıya veri göndermesini amaçlar.(Birden çoğa durumu)
    # Bir yayıncı PUB ile mesajları gönderir ve birden fazla abone (SUB) bu yayıncıya bağlanır. Sadece ilgilendikleri topic'lere abone olurlar.

    # PUSH , PULL --> Görev dağıtımı ve iş yükü dengelenmesi için kullanılır.
    # Bir PUSH görevleri bir QUEUE'ye iter. Birden fazla PULL ise bu görevleri QUEUE'den alır ve işler. İş yükü işçiler arasında otomatik olarak dağıtılır.

# Synchronous :
    # istek - cevap sırası zorunlu olan modellerde kullanılır. 
    # Bir mesaj gönderilir ve mutlaka cevap beklenir.Cevap gelmeden yeni bir istek göderilemez.
    # En bilinen şablonu REQ - REP'tir.

#Asynchronous nedir ?
    # Tarafların iletişimde birbirlerini beklemek zorunda olmadıkları türdür.
    # Bir mesajdan sonra beklemek gerekmez,mesajlar art arda gönderilebilirler.
    # Çoklu üretici-tüketici modelinde kullanılır.
    # PUSH-PULL , PUB-SUB , DEALER-ROUTER ,PAIR örnek şablonlardır.

# PAIR nedir ?
    # ZeroMQ'daki en basit ve en serbest sockettir.
    # REP , REQ  gibi sıra zorunluluğu ; PUSH - PULL gibi tek yönlü değildir. 
    # İki uç arasında tamamen serbest,çift yönlü iletişim sağlar.
    # Sadece 2 socket bağlanabilir.
    # Her 2 taraf da send() ve recieve() ile istediği sırada iletileri alır.

# Taşıma ( Transport ) nedir ?
    # Soketlerinizin mesajları fiziksel olarak nasıl ileteceğini belirleyen protokoldür.
    # tcp : TCP/IP Protokolü.
        # Farklı bilgisayarlar, hatta farklı kıtalar arasında iletişim kurmak için kullanılır. ZeroMQ'daki en yaygın taşıma yöntemidir.
    # icp : Süreçler Arası İletişim (Inter-Process Communication).
        #Aynı işletim sistemindeki farklı uygulamalar (farklı süreçler) arasında iletişim kurmak için kullanılır. Daha hızlıdır.
    #inproc : İşlem İçi İletişim (In-Process Communication).
        #Aynı uygulamanın farklı iplikleri (threadler) arasında iletişim kurmak için kullanılır. En hızlı taşıma yöntemidir.

# Adresleme :
    # Bağlama ( BIND ) ve Bağlanma ( CONNECT ):
        # Bind nedir ?
        # Bir sunucu gibi soketi belirli bir porta ve yerel adrese kitlemektir.
        # Soket bu adresten gelen bağlantıları dinler.
        # Genelde server(sunucu) veya publisherlar  bind kullanırlar.
    
        # Connection nedir ?
        # Bir istemci gibi soketin sunucuya bağlandığı uzak adres ve porta aktif olarak bağlanmayı sağlar.
        # Genelde istemci ya da aboneler connect kullanırlar.

    # BIND --> Server ve publisher.
    # CONNECT --> client ve subscriber.

# Önemli kural ‼️
    # ZeroMQ mesajı sadece STRING , BYTES veya JSON STRING olarak alabilir.

# REQ --> İsteği başlatan taraftır.Sunucuya connect olur.
    # socket.send() ile istek gönderir.
    # socket.recv() ile yanıt beklenir.
# REP --> İsteği alan ve yanıt veren taraftır.Belirli adrese bind olur.
    # socket.recv() ile isteği alır. Bu adımda kod istek gelene kadar bloklanır.
    # socket.send() ile yanıtı gönderir.

# JSON hakkında :
    # json.loads --> JSON formatındaki string bir veriyi alır ve pythonun yerel veri yapılarından birisine dönüştürür.
    # json.dumps --> Bir python nesnesini alır ve bu nesneyi JSON String formatına çevirir.

# Connect kısmına localhost için --> tcp://127.0.0.1:PORT yazabiliriz.
    # Bilgisayarlar arası kullanım yapacaksan LAN IP yazılır.

# istemci = client
# sunucu = server

#Error Handling (Hataları ele almak)

#Örneğin girilen bir sayının karesini alıcaz ancak kullanıcı sayı değilde isim yazarsa program hata verip kapanıcak
#Bunun olmaması için try, except, finally kullanıcaz

while True: #while kullandım çünkü str girerse program kapanmasın kullanıcıya şans tanıyalım sonsuz döngü oluşturdum
    try: #ilk bir denicek hata varmı yokmu
        int(input("Enter a number:"))
    except: #eğer hata alırsa except çalışacak
        print("Enter a number!!!")
    else: # except için else dedik yani denedi sonra hata almazsa else çalışıcak
        print("True")
    finally: #hata olsa da olmasa da finally her zaman çalışır bunu burda kullanmak saçma ancak elbet lazım olabilir bir zaman ve çok kullanılmaz
        print("Finally")
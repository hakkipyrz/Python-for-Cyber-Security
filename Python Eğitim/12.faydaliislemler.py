#FAYDALI İŞLEMLER (BİLGİLER)

# 1-RANGE

#  List oluşturcaz diyelim sayılar 100'e kadar olacağını varsayalım tek tek elle eklemek yerine range kullanabiliriz.

print(list(range(101))) #101 dahil değil 1'den 100'e kadar listeye eleman ekledi.

for number in list(range(101)):
    print(number * 5)
    
print("-"*50)

for num in list(range(6,46,2)): #aralıklı da yazabiliriz slicing gibi 6'dan 45'e kadar 2şer artarak yazdırır
    print(num)
    
print("-"*50)

# 2-ENUMERATE

#verilerin indeksini görmemize yardımcı olur.

#Normalde şu şekilde yaparız:

index=0

for number in list(range(5,16)):
    print(f"Number:{number} Index: {index}")
    index += 1

print("-"*50)

#Enumerate ile:

for number in enumerate(list(range(5,16))): #ilk index yazdırır daha sonra sayıyı yazdırır.
    print(number)

print("-"*50)

# 3-RANDOM

#bunu kullanmak için kütüphaneyi çağırmamız gerekir -> from random import randint

from random import randint

print(randint(0,1000))# 0 ile 1000 arasında random bir tane sayı yazar.

print("-"*50)

my_list= list(range(0,10))

print(my_list) #normal bir liste oluşturduk ancak bunu rastgele sıralamak istiyorsak;

from random import shuffle #shuffle karıştırmak anlamına gelir

shuffle(my_list) #listeyi tamamen karıştırıyor ve her çalıştırdığımızda farklı sıralama geliyor.

print(my_list)
print("-"*50)

# 4-ZIP

#Elimizde bir çok liste var bunları birleştirmek istiyorsak zip kullanırız

sport_list = ["run","swim","basketball"]

calories_list= [100,200,300]

day_list=["monday","sunday","wednesday"]

new_list= list(zip(sport_list,calories_list,day_list)) #3 listeyi birleştiriyoruz.Ancak zip liste halinde gözükmez bu yüzden listeye çeviriyoruz.

print(new_list)

print("-"*50)

# 5-LIST ADVANCED (Listeler ileri seviye)

new_list= []

my_string="metallica"

for element in my_string:
   new_list.append(element) #Burdaki işlemi daha kısa satırda yazabiliriz
print(new_list)

new_list2= [element for element in my_string] # my_Stringdem tek tek elemanları alır yeni listeye koyar yukarıdaki ile aynı işlemdir.

print(new_list2)

print("-"*50)

new_list3= [number*5 for number in list(range(0,10))]

print(new_list3)
#Lists

my_list= [1,2,3]

print(my_list[0])

print("-"*50)

#Veri Güncelleme

my_list[0] = 5  #0. indeksi 1 yerine 5 yaptık
print("Güncelleme") 
print(my_list)
print("-"*50)
#Veri Ekleme
print("append()")
my_list.append(7) #listenin sonuna 7 ekledi

print(my_list)

print("-"*50)

print("pop()")
my_list.pop()# pop son elemanı siler.

print(my_list)

print("-"*50)

#Listeler sadece numaralardan oluşmaz karışık olabilir.

my_mixed_list = [12,"a",3, "Hakkı"]
print("Karışık Listeler")
print(my_mixed_list)

print("-"*50)

#Listelerde toplama

print("Listelerde Toplama")

my_list_1= ["a","b","c"]
my_list_2= ["e","f","g"]
my_list_toplam= my_list_1 + my_list_2 

print(my_list_toplam)
print("-"*50)

#Listeyi ters çevirme

my_list_1.reverse()

print(my_list_1) # a b c yi ,  b a yaptı
print("-"*50)

#Nested List (İç İçe Listeler)

new_list=["a",1,"Hakkı",[3,5,"Poyraz"]]

print(new_list)

print(new_list[3]) #3.indeksi diğer liste olur.

print(new_list[3][1]) #listenin içindeki listenin 1.indeksi 5'i verir.
print("-"*50)

#Slicing İşlemleri

print(new_list[2:]) #2.indeksten başlar, stringde yaptığımız tüm slicing işlemleri burdada geçerli

print("-"*50)
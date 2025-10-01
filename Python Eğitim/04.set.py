#Set de aynı elemandan birden fazla olmuyor.
#my_set2 = {1,2,3,1} şeklinde oluşturulur.


#CASTING (Değiştirme) int str çevirme gibi int(str())

print("Listeyi sete çevirme")

my_list= [1,2,3,1]

print(my_list)

my_set = set(my_list)

print(my_set)
print("-"*50)

#SET OLUŞTURMA
print("set oluşturma")

my_set2 = {1,2,3,1}

print(my_set2)
print("-"*50)

# int ve str karışık Set oluşturma

print("int ve str karışık Set oluşturma")

my_set3={"a", "a",1,1,3,"b"}
print(my_set3)
print("-"*50)
#Boş bir set oluşturma ve değer ekleme
print("Boş bir set oluşturma ve değer ekleme")
my_set4= {}
print(type(my_set4)) #set değil dict olarak görüyor bunun olmaması için

my_set5= set()
print(type(my_set5)) #şuan type set oldu

my_set5.add(2)
print(my_set5)

my_dict = dict() #Aynı şekilde dict de böyle yapabiliriz.
my_list2= list() #Listdede aynı şekil uygulanabilir.
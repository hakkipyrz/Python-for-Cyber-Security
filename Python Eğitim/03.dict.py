# Listelerde [] kullanılırken Dictionary'de {} kullanılır.

# Dict de my_dictionary= {"key":"value"} kullanılır. [key] ile de value çağırılır

my_fitness_dictionary={"run":100, "swim":300} #koşma 100 kalori yüzme 300 kalori şeklinde bilgileri girdik

print(my_fitness_dictionary["run"]) #run ın valuesini gösterir

print("-"*50)

#Value de int ile str aynı anda kullanma
print("Value de int ile str aynı anda kullanma")
my_dictionary1 = {"key1":1, "key2": 2, "key3": "Hakkı"} #aynı dict de hem int hem str kullanabiliriz.

print(my_dictionary1)
print("-"*50)

#Key de int ile str aynı anda kullanma
print("Key de int ile str aynı anda kullanma")
my_dictionary2 = {"key1": 20, 31:41}

print(my_dictionary2)
print("-"*50)

 #Dict de value olarak hem list hem dict yazma

print("Dict de value olarak hem list hem dict yazma")

my_dictionary3= {"key1":100,"key2":[10,30,58],"key3":{"key":5}}

print(my_dictionary3)

print("-"*50)

#Keyleri Çağırma

print("Keyleri Çağırma")
print(my_dictionary3.keys())
print("-"*50)

#Valueleri Çağırma

print("Valueleri çağırma")
print(my_dictionary3.values())
print("-"*50)

#dict3 de bulunan 5 valuesine ulaşma

print(my_dictionary3["key3"]["key"])
print("-"*50)
#Veri Güncelleme
print("veri güncelleme")

my_dictionary3["key1"] = 31 #100dü 31 oldu


print(my_dictionary3)
print("-"*50)
#Veri Ekleme

print("veri ekleme")

my_dictionary3["key4"] = "Hakkı" #key 4 yoktu key4 ve veri ekledim


print(my_dictionary3)
print("-"*50)
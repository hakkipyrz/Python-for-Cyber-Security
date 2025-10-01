 
my_list= list()
my_list.append

# my_list liste sınıfının instance'si (obje) oluyor. Yanındaki append ise attribute (özellik) deniyor.

# Snake = my_string
# Camel = myString bu ikisi yazım şekilleridir ve biz classlarda camel kullanırız

class Musician():

    job="Musician" #bu classda herkesin ortak özzelliği müzisyen olmak

    def __init__(self,name,age): #init de özellikleri tanımlıyoruz.
        self.name_attribute = name #self. kısmından sonraki yere istediğimizi yazabiliriz sadece = den sonraki kısım name olmak zorunda çünkü üstünde öyle tanımladık
        self.age = age

    #Method
    #Classların içine istediğimiz kadar method, fonks yazabiliriz

    def sing(self):
        print(f"We are the champions! -{self.name_attribute}") #istersem tekrar yukarıdaki name'i de yazdırabilirim

my_musician= Musician(name="James", age=35) #burda da instance oluşturduk yani bir müzisyen tanımladık ve özellikler verdik

print(my_musician.name_attribute, my_musician.age, my_musician.job) # bize ismini ve yaşını yazdırdı
my_musician.sing()
print("-"*50)
# GÜNCELLEME İşlemi

my_musician.name_attribute = "Lars"

print(my_musician.name_attribute)

print("-"*50)

# Class'da Pratik Kullanımlar

#Köpek yaşıyla insan yaşını bulma
class DogYears():
    year_factor= 7

    def __init__(self,age=5): #burda age=5 yazarsam age otomatik 5 alır
        self.age = age
        self.age_multiplied= age * 7 #aşağıda ki calculation'a gerek kalmadan bu şekilde de hızlıca 7 ile çarpabilirdim

    def calculation(self):
        return self.age * self.year_factor #self.year_factory yerine DogYears.year_factory de yazabilirim.
    
my_dog = DogYears(3) #burayı 3 yerine hiçbişey yazmasaydım 5 kabul edicekti

print(my_dog.calculation())

print(my_dog.age_multiplied)

print("-"*50)

# INHERITANCE (Miras Alma)

class Class1():
    
    def __init__(self):
        print("Class 1 created")
    
    def method_1(self):
        print("method 1 created")

    def method_2(self):
        print("method 2 created")

class Class2(Class1):  #class 2 de class1'in özelliklerini kullancaksa onu miras alması lazım o yüzden parantez içine class1 yazıcaz
    
    def __init__(self):
        Class1.__init__(self)
        print("Class 2 created")

    def method_3(self):
        print("method 3 created")

    #override (üstüne yazma)

    def method_1(self):
        print("method 1 override")

my_instance= Class1() #class 1 buna tanımlandı

my_instance2= Class2() #hem class1 created dedi hemde class2

my_instance2.method_2()

my_instance2.method_1()

my_instance.method_1()

print("-"*50)

# POLYMORPHISM: farklı sınıfın instance'ında onu o sınıfa ait method gibi çalıştırabiliyoruz

class Apple():
    def __init__(self,name):
        self.name= name
    
    def information(self):
        return self.name + " 100 calories"
    
class Banana():
    def __init__(self,name):
        self.name= name
    
    def information(self):
        return self.name + " 200 calories"
    
banana = Banana("banana") #instance tanımladık

apple = Apple("apple")

print(banana.information())
print("-"*50)
fruit_list= [banana, apple]

for fruit in fruit_list:
    print(fruit.information())
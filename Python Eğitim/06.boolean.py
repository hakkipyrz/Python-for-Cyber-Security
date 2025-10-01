# Boolean True False çalışır ancak baş harfi büyük olcak true ve false'nin

my_boolean= True

x=5
y=3

print(x<y) #false döndürdü


#SINAV

#Soru 1
my_string= "James Hetfield"

my_letter= my_string[4]

print(my_letter) #DOĞRU
print("*"*50)
#SORU 2
my_new_string= "QuentinTarantino" #tinT

print(my_new_string[4:8]) #doğru
print("*"*50) 

#soru 3
my_last_string= "Afyonkarahisarlılaştıramadıklarımızdanmısınız" #yapamadım 

#cevap:

print(my_last_string[::-1])
print("*"*50)

#SORU 4

#Aşağıdaki işlemin sonucu hangi veri tipinde olacaktır ?

print(type(3+10.2+50))  #float  , doğru

print("*"*50)

#SORU 5

#Aşağıdaki sorunun cevabı nedir?
print(5+8*12) #doğru
print("*"*50)
#Soru 6 Bu listeyi 3 farklı yoldan oluştur (set,list,dict) [1,2,"a"]

list = [1,2,"a"]

dict = {"key1": 1, "key2": 2, "key3": "a"}

set1= {1,2,"a"}

print(type(set1)) #Doğru
print("*"*50)

#SORU 7 Aşağıdaki "a"'yı tek satırda yazdır.

my_list= [1,4,[2,3,"a"]]

print(my_list[2][2]) #Doğru
print("*"*50)

#SORU 8 Aşağıdaki "b"'yı tek satırda yazdır.

my_dict= {"k1":2,"kk":[4,{"kkk":"b"}]}

print(my_dict["kk"][1]["kkk"]) #Doğru

print("*"*50)

#Soru 9  Aşağıdaki liste sete çevrilince hangi değerler içinde kalacaktır ?

my_list1 = [11,12,22,33,11,22,45,32,21,22,33,45]

my_set = set(my_list1)

print(my_set) #Doğru
print("*"*50)

#Soru 10 Aşağıdaki ifadenin sonucu nedir?

x = 40*5+3

y= 208-2*4

print(x>y)  #Doğru
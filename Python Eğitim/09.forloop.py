my_list= [1,2,3,4,5]

for i in my_list: #benim listemdeki elemanları al ve tek tek i'ye tanımla demek
    print("HelloWorld")

print("-"*50)

for i in my_list: 
    print(i)

print("-"*50)

for item in my_list: 
    new_number = item * 5 #her bir listedeki elemanı 5 ile çarparak yazdırdık
    print(new_number)

print("-"*50)

for i in my_list: 
    print(10%i) #listedeki sayıların 10 ile bölümünden kalanları yazdırır

print("-"*50)

for number in my_list:
    if number %2 == 0:
        print(number)

print("-"*50)

my_str = "James Hetfield"

for letter in my_str:
    print(letter)

print("-"*50)

my_tupple= (1,2,3)

for item in my_tupple:
    print(item * 5 -10)

print("-"*50)

my_new_list= [("a","b"),("c","d"),("e","f"), ("g","h")]

for element in my_new_list:
    print(element) #bunun farklı bir yolu var (x,y) şeklinde ve istersek orda sadece x'leri de yazdırabiliriz ancak bunu liste karışık değilse full tupple ise kullanmak mantıklı

print("-"*50)

for (x,y) in my_new_list:
    print((x,y))

print("-"*50)

for (x,y) in my_new_list:
    print(x) #sadece x leri yazdırabiliriz. Eğer tupple (1,2,3) olsaydı bu sefer (x,y,z) yazıcaktık.

print("-"*50)

my_dict= {"key1": 100,"key2":200, "key3": 300}

for x in my_dict.items():
    print(x)

print("-"*50)
 
for key,value in my_dict.items(): #bu şekilde sadece keyleri görebilirim
    print(key)
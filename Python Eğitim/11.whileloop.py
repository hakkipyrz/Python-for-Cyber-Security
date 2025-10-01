#Bir koşul sürece o işleme devam etmesini sağlar.

a=0

while a < 5:   #a 5'den küçük olduğu sürece kodu çalıştır.
    print("Hello")
    a = a +1 #eğer a'yı arttırmasaydım sonsuza dek Hello yazdırcaktı. a += 1 de aynı şey

print("-"*50)

my_list = [1,2,3,4,5]

while 3 in my_list: # listemde 3 olduğu sürece yap demek
    my_list.pop()   #önce 5 sonra 4 en son 3'ü siliyor sonra 3 olmadığı için çalışmıyor.
    print(my_list)


print("-"*50)

number = 0

while number < 10:

    if number == 5:
        break
    print(number)
    number += 1

print("-"*50)

p=0

while p < 20:
    #print("value p:" + str(p)) bunun yerine aşağıdakini de kullanabiliriz.
    print (f"value p: {p}") #f sayesinde herhangi bir değişkeni bir stringin içinde kullanabiliyoruz
    p +=1
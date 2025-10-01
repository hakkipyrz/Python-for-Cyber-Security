print(508+65)

print (30*5)

print (2*2*2)

print(2**3) #üslü ifade

print(11%2) #kalan bulma

print("*"*50)

# integer(int)= tam sayılar için kullanılır
# float= 1.25, 5.6 gibi ondalıklı sayılar için kullanılır.
# string= metinlerde kullanılır. "1.25" bu da stringdir.

x=3
y=5
print(x+y)

print("*"*50)

#r= float(input("r: ")) #kullanıcıdan değer alabiliriz.

#print(r)

#print("sonuç=",r*2*1.5)

#print(type(r)) #r nin string olduğunu bize söylüyor ve yukarıdaki işlemde hata aldım bu yüzden r yi floata çevirdim.

print("*"*50)

# STRING İFADELER

x= "Hello world"

print(x)

print(len(x)) #x in karakter uzunluğunu verir, boşlukları da sayar.

print("*"*50)

# ESCAPE CHARACTERS (KAÇIŞ KARAKTERLERİ) \n, \t

print("Hello \nWorld") # kaçış karakteridir ve newline'dan gelir world'ü aşağı yazdır

print("Hello \tWorld") # tab kadar boşluk bırakır.

print("*"*50)

# İNDEKS

y="Hakki Poyraz"

print(y[0]) #0. indeksi yazdırır.

print(y[-1]) # -1 son indeksi yazdırır.

print(y[2::]) # slicing işlemlerinde başlangıç:bitiş:artış miktarı şeklinde kullanılır, 2. indeksden başla demek 
print(y[1:8:2]) #1.indeksden başla 8.indekse kadar 2 şer yazdır ama 8.indeks dahil değil
print(y[::-1]) #tersten yazdırır
def hello_world():
    print("Hello World")

hello_world()

print("-"*50)
#INPUT AND RETURN

def hello_programing(name):
    print("Hello")
    print(name)

hello_programing("Python")

print("-"*50)

def hello_program(name="Python"): 
    print("hello")
    print(name)

hello_program() # eğer hello_program("java") yazarsam yine python yerine java yazdırır.

print("-"*50)

def summ(num1,num2):
    num3= num1 + num2
    print(num3)

summ(98,256)
print("-"*50)

#yaptığımız işlemi başka bir yere eşitlemek için return kullanıyoruz.

def summation(num1,num2,num3):
    return num1+num2+num3 #yani return başka bi kısımda bidaha kullanıcaksam çıktıyı tekrar girdi olarak kullanıcaksam return yazmam lazım

my_result= summation(10,20,30) #burda yukarıdaki çıktıyı tekrar girdi olarak kullandım

print(my_result)

print("-"*50)

#Eğer ilk harf "m" ise bunu büyük yapan fonks:
def control_string(s):
    if s[0] == "m":
        print(s.capitalize())
    

control_string("metallica")

print("-"*50)

# Arbitrary Arguments & Key Word Arguments

#Yukarıdaki summation fonksda 20,30 veya kullanıcının yazmak istediği kadar sayı toplatmak isteseydik nasıl yapıcaktık
# *args sayesinde yapılır.

def summation2(*args): 

    return sum(args)

print(summation2(10,20,30,40,50,60,70,80,90,100))

print("-"*50)

#**kwargs ise istenildiği kadar anahtar kelimeyle girdi vermesini sağlar. Dict gibi

def example_func(**kwargs):
    print(kwargs)

example_func(run=100, swim=200, basketball=300)

print("-"*50)

def keyword_func(**kwargs):
    if "Metallica" in kwargs:
        print("Heavy Metall!")
    else:
        print("Rock is dead")

keyword_func(Metallica=10,Madonna=5)

print("-"*50)

# FONKSİYONLARDA PRATİK YÖNTEMLER

def divide (number):
    return number/2

print(divide(10))
print("-"*50)
#peki aşağıdaki listeyi yukarıdaki fonksiyona nasıl uyarlarız?

my_list= [1,2,3,4,5,6,7,8]

for num in my_list:
    print(divide(num))

print("-"*50)

# MAP FONKSİYONU: daha büyük liste veya fonksiyonlarla uğraşıcağımızda map bize kolaylık sağlar.

print(list(map(divide, my_list)))

print("-"*50)

# stringlerde map kullanımı:

def control_string(string):
    return "Metallica" in string

print(control_string("Metallica")) #true döndürür şimdi liste oluşturalım

my_artist_list= ["Metallica", "Madonna", "Queen", "Megadeth", "Metallica2"]
print(list(map(control_string, my_artist_list))) #tüm hepsine uyguladı true, false döndürdü

print("-"*50)

# FİLTER FONKSİYONU: Sadece true ise listeme al işlemi yapar, kısaca filtreliyoruz belli koşula uyanları alıyoruz listeye ekliyoruz.

print(list(filter(control_string, my_artist_list))) #listeye sadece metallica ekledi binlerce listeden tek tek yapmaktansa bu şekilde hızlıca ekleyebiliriz

print("-"*50)

# LAMBDA FONKSİYONU: genellikle tek kullanımlık fonksiyonlarda kullanılır.

def multiply (number):
   return number *3 #bu işlemin benzerini lambda ile yapalım

print(multiply(5))

print("-"*50)

multiply2= lambda number:number * 3

print(multiply2(5)) #aynı sonucu alırız

print("-"*50)

my_list2 = [3,5,7,9]

print(list(map(lambda num:num*4, my_list2)))


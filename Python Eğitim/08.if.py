if 3>2 :
    print("3 2'den büyüktür")

print("-"*50)

x=4
y=4

if x>y: # 1. koşul her zaman if ile başlar
    print("x büyük")
elif x==y:
    print("x ve y eşit") # 2 ve daha fazla koşul varsa elif olur.
else:
    print("y büyük") #son koşul her zaman else ile biter

print("-"*50)

#Kullanıcıdan en sevdiği kahramanı yazdıralım

my_superhero= input("superhero:")

if my_superhero=="batman":
    print("Batman")
elif my_superhero== "superman": #bu şekilde birden fazla koşul elif ile yazabiliriz
    print("Superman")
elif my_superhero=="ironman":
    print("ironman")
elif my_superhero=="spiderman":
    print("Spiderman")
else:
    print(":(")

print("-"*50)

a=10
b=15
c=20

if a>b or b<c: #b<c true olduğu için if çalışır
    print("Hakki")
elif a<b and b>c:
    print("Poyraz")
else:
    print("HelloWorld")

print("-"*50)

isDead= False

if isDead == True:
    print("Character is dead")
else:
    print("Character is not dead")

if isDead: #böyle yazarsak da otomatik true algılar
    print("Character is dead")
else:
    print("Character is not dead")

if not isDead: #true değilse yazdır dedik isdead false olduğu için if çalıştı
    print("Character is not dead")

print("-"*50)

# PRATİK IF KULLANIMLARI

my_string= "Hello World"

if "Hello" in my_string: #my_stringimin içinde Hello varsa true yoksa false çalıştırır.
    print(True)
else:
    print(False)
print("-"*50)

my_list= [1,2,3,4,5]

if 2 in my_list:
    print(True)
else:
    print(False)
print("-"*50)

my_dict= {"k1": 100,"k2": 200}

if 100 in my_dict.keys(): #.values() desek yine çalışırdı
    print(True)
else:
    print(False)
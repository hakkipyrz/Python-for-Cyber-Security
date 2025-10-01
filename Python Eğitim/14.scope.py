
# Kapsam anlamına geliyor

a=10 
a=5
print(a) #eğer bunun da altına fonks içinde a=8 yazsak yine 5 okur bunu neye göre okuduğunu LEGB'ye göre karar verir.
print("-"*50)

 #LEGB -> L: Local, E: Enclosing, G: Global, B: Built-in

#Python fonksiyonda ilk local'i yazdırır, local yoksa enclosingi yazdırıyor o da yoksa global'i yazdırı

my_string= "Hakki"
#Burdaki ise Global

def my_func():
    #Burdaki kod Enclosing
    my_string= "James"

    def my_func2():

        # Burdaki kod Local
        my_string="Paul"
        print(my_string)
    
    my_func2()

my_func() #fonksda en son ki ismi yazdırırdı

print(my_string) #bunda ise fonksiyondakileri görmeden direkt ilk yazılanı yazdırdı

print("-"*50)

y=10

def func_new(y):
    print(y)
    y=5
    print(y)
    return y

func_new(10) #önce 10 yazdırdı ilk printe çünkü oraya kadar local yoktu sonra local tanımladık 5'i yazdırdı

#Eğer ki global değişkeni yani burda ki 10 değerini de değiştirmek istersek şunu yapıcaz

y= func_new(y)

print(y) #artık y 10 değil 5 oldu.

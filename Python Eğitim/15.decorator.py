#İki tane fonksiyonu iç içe kullanma:

def func (new_func):
    print("Func started")
    new_func()
    print("Func ended")

def hello_func():
    print("Hello world")

func(hello_func) #1.funcın değişkenini 2.func olarak yazıp ikisini de çalıştırdık.

print("-"*50)

# Direkt iç içe yazacaksam eğer 2 şekilde yazabilirim:

#1.YOL

def new_func():
    def new_func2():
        print("New Func 2")

    new_func2()

new_func()

print("-"*50)

#2.YOL

def new_func():
    def new_func2():
        print("New Func 2")

    return new_func2

string_new= new_func()

string_new()
print("-"*50)
#DECORATOR İŞLEMLERİ

def decorator_func(func):
    def wrapper_func():
        print("wrapper started")
        func()
        print("wrapper stopped")
    
    return wrapper_func

def func_new():
    print("hello world")

example_func= decorator_func(func_new)

example_func()
print("-"*50)

@decorator_func #yukarıda yaptığım tüm uzun işlemleri bu şekilde kısaca yapmış oldum decorator sayesinde
def func_new():
    print("hello world")

func_new()
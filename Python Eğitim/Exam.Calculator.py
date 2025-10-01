def calculator():
         
    if z=="+":
        print(x+y)
    elif z=="-":
        print(x-y)
    elif z=="*":
        print(x*y)
    elif z=="/":
        print(x/y)
    else:
        print("Please only type one of these characters: +,-,*,/")
    


while True:
    x= int(input("Please type the first number:"))
    y= int(input("Please type the second number:"))
    z= input("Choose between +,-,*,/")
    calculator()
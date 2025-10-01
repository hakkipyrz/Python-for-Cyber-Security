name= input("Name:")

print(f"Hello {name}, time to play hangman!")

secretword_list=["h","e","l","l","o","w","o","r","l","d"]
target_list= ["","","","","","","","","",""] #helloworld :)
health= 5

for i in target_list:
    print("-")



for target in target_list:
    word= input("Guess a word:")
        
    if word=="h":
        print("Correct")
        target_list[0]="h"
        print(target_list)

    elif word=="e":
        print("Correct")
        target_list[1]="e"
        print(target_list)
    
    elif word=="l":
        print("Correct")
        target_list[2]="l"
        target_list[3]="l"
        target_list[8]="l"
        print(target_list)

    elif word=="o":
        print("Correct")
        target_list[4]="o"
        target_list[6]="o"
        print(target_list)
        
    elif word=="w":
        print("Correct")
        target_list[5]="w"
        print(target_list)

    elif word=="r":
        print("Correct")
        target_list[7]="r"
        print(target_list)

    elif word=="d":
        print("Correct")
        target_list[9]="d"
        print(target_list)

    else:
        print("Wrong!")
        health -= 1
        print(f"You have {health} left")
        print(target_list)
    if health == 0:
        print("You died!")
        break 
    if target_list==secretword_list:
        print("Win!")
        break



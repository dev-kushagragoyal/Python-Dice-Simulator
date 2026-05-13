import random as r
import time as t 


while True:
    t.sleep(2)
    print()
    print("1.Roll the dice  2.To exit")
    print()
    user = int(input("Enter your choice : "))
    print()
    if user == 1:
        dice = r.randint(1,6)
        if dice == 6:
            print("Wow you got : ","6")
            print()
        elif dice == 5:
            print("Not a smaller number you got : ","5")
            print()
        elif dice == 4:
            print("Not to be sad you got : ","4")
            print()
        elif dice == 3:
            print("There are many more chances you got : ","3")
            print()
        elif dice == 2:
            print("Try again next time you got : ","2")
            print()
        elif dice == 1:
            print("Smaller steps can make bigger difference you got : ","1")
            print()
    elif user == 2:
        print("Thank you for playing")
        print()
        break

    else:
        print("Invalid input")
        print()

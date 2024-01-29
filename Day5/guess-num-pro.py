import random


mode = int(input("Enter mode: \n[0] You'll guess\n[1] AI will guess.\n"))

if mode == 0:
    aiPick = 0
    diff = int(input("Select difficulty mode:\n [0] Easy\n [1] Normal\n [2] Hard\n"))
    max = 0

    match diff:
        case 0:
          max = 10
        case 1:
          max = 50
        case 2:
          max = 100
        case _:
          print("Invalid ")
          exit()
                              
    aiPick = random.randint(0, max)
    print("Welcome to guess the number game".center(50))

    while True:
            a = random.randint(0, (aiPick - 1))
            b = random.randint(aiPick, max)
            print("Number is between " + str(a) + " : " + str(b))
            guess = int(input("Your guess : "))
            if guess == aiPick:
                print("Yeah!!!!!!!! Correct.")
                break
            else:
                print("Sorry, try again !")
           
    print("Game over!")     
elif mode == 1:
    print("AI will guess. Imagine number between 0-100")      
    a = 0
    b = 100
    f = True
    # I thought : 66
    while True:
        m = int((a+b)//2)
        d = 0
        d = input("Is your number between " + str(a) + " and " + str(m) + " : ")
    
        if d == "y":
            b = m
        elif d == "n":
            a = m # b = 100, a = 50, a = 25 
        else:
            print("Failed")
            break    

        if (b-a) < 5:
            r = input("Is your number " + str(random.randint(a, b)) + " : ")   
            if r == "y":
                print("I got you!!!!")
                break    

        if a == b:
            print("Can't guess !")     
    print("Game over!!!")        
        



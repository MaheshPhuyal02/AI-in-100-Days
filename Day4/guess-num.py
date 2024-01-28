import random
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

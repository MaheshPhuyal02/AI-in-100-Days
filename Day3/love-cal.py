import random


fname = input("Enter your name : ")
pname = input("Enter your partner name : ")

love = random.randint(50, 100)

print((fname.capitalize() + " + " + pname.capitalize() + "  = " + str(love) +   "%").center(50))
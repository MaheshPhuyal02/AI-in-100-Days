c = input("Enter char to fill : ")
l = int(input("Enter the lenght : "))
b = int(input("Enter the breadth : "))

for i in range(b):
    for j in range(l):
        print(c, end="")
    print("")
n = int(input("Enter n : "))

def add(num):
    global sum
    if num <= n:
        sum = sum + num
        num = num + 1
        add(num)
    else:
        print("Sum is : " + str(sum))
    
sum = 0
add(0)  
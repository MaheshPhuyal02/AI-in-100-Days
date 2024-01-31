num = int(input("Enter number : "))
power = int(input("Enter power : "))
result = 1


def powFun(count):
    global power, num, result
    if count <= power:
        result = result * num
        powFun(count=(count+1))
    else:
        print("Answer : " + str(result))    

powFun(1)

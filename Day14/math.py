import re as regex

exp = input("Enter expression: ")
pos = -1

exp_real = ""


def calculate(a, b, op):
    
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    elif op == "^":
        return a ** b
    else:
        return "Invalid Operator"
    
    
def postfix(a, b, op, word):
    global pos
    
    pos = pos + 1
    if word in "1234567890":
        if a is None:
         a = word
        else:
            b = word 
    
    else:
        if op is None:
            op = word
        else:
            a = calculate(a, b, op)
            op = word
            b = None
    if pos == len(exp_real):
        print(calculate(a, b, op))
        return
    
    
    postfix(a, b, op, exp_real[pos])
            
            
       
        
# 2+(3-5)

postfix(None, None, None, exp[0])
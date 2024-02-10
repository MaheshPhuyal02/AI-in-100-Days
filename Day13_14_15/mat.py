import numpy as np
import re as regex
import os
import math

def checkReg(reg, string):
    match = regex.search(reg, string)
    if match:
        return match.groups()
    else:
        return False

def findChar(s):
    for c in s:
        if c not in '1234567890-+*/^':
            return c
    return False    
    
def parse_equation(s):
    w = findChar(s)
    if w == False:
        return False
    nums = [0,0,0]
    accum = ''
    expo = False
    sign = 1
    for c in s:
        if expo and c == '2':
            expo = False
            nums[0] = nums[1]
            nums[1] = 0
            accum = ''
        elif c in '1234567890.':
            accum += c
        elif c == w:
            if accum == '':
                accum = '1'
            nums[1] = float(accum) * sign
            accum = ''
        elif c == '+':
            sign = 1
        elif c == '-':
            sign = -1
        elif c == '^':
            expo = True
    nums[2] = float(accum) * sign
    return nums    
    
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "Complex Roots"
    
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return root1, root2

def doNp(arr1, arr2, op):
    if op == "+":
        return np.add(arr1, arr2)
    elif op == "-":
        return np.subtract(arr1, arr2)
    elif op == "*":
        return np.multiply(arr1, arr2)
    elif op == "/":
        return np.divide(arr1, arr2)
    elif op == "%":
        return np.mod(arr1, arr2)    

def doMath(val1, val2, oper):
  try:  
    if oper == "+":
        return val1 + val2
    elif oper == "-":
        return val1 - val2
    elif oper == "*":
        return val1 * val2
    elif oper == "/":
        return val1 / val2
    elif oper == "%":
        return val1 % val2    
  except Exception as e:
        return "Error: " + str(e)

appName = "MathPy"
os.system('cls')

variables = {}
patterns = [{
    "val" : r'(\w+)\s*=\s*(\d+)',   
    "d_mat":r'(\w+)\s*=\s*\[([\d\s;,]+)\]',
    "p_op" : r'(\w+)\s*([+\-*/])\s*(\w+)',
    "oper" : r'(\w+)\s*=\s*(\w+)\s*([\+\-\*\/])\s*(\w+)',
    "var" : r'(\w+)\s*=\s*(\w+)',
    "print" : r'print\((\w+)\)',
    "fun" : r'(\w+)\(([\w,]+)\)',
    "fun_i" : r'(\w+)\s*=\s*fun\("([^"]+)"\)',
    "fun" : r'(\w+)\(([\w,]+)\)',
    "clc" : r'clc',
}]

coef_pattern = r'([-+]?)(\d*)[a-zA-Z]*\^?(\d*)'

while True:  
    commands = input( appName + " >> ")
    commands = commands.strip()
    if commands == "exit":
        print("Exiting...")
        break
    commands = commands.strip()
    
    for pattern in patterns:
        
        if checkReg(pattern['val'], commands):
            var, val = checkReg(pattern['val'], commands)
            variables[var] = int(val)
        
        if checkReg(pattern['fun_i'], commands):
            var, fun = checkReg(pattern['fun_i'], commands)
            variables[var] = fun
            print(var + " => " + fun)
            
            
        elif checkReg(pattern['p_op'], commands) and commands.__contains__("=") == False:
            v1, oper, v2 = checkReg(pattern['p_op'], commands)
            out = 0
            v11 = any
            v22 = any
            
            if variables.keys().__contains__(v1):
                if type(variables[v1]) == np.ndarray:
                    v11 = np.array(variables[v1])
                    v22 = np.array(variables[v2])
                    print(doNp(v11, v22, oper))
                else:
                    v11 = int(variables[v1])
                    v22 = int(variables[v2])
                    print(doMath(v11, v22, oper))
            else:
                v11 = int(v1)
                v22 = int(v2)
                print(doMath(v11, v22, oper))
                
        elif checkReg(pattern['oper'], commands):
            var, val1, oper, val2 = checkReg(pattern['oper'], commands)
            v11 = any
            v22 = any
            out = any
            if variables.keys().__contains__(val1):
                if type(variables[val1]) == np.ndarray:
                    v11 = np.array(variables[val1])
                else:
                    v11 = int(variables[val1])
            else :
                v11 = int(val1)
                
            if variables.keys().__contains__(val2):
                 if type(variables[val2]) == np.ndarray:
                    v22 = np.array(variables[val2])
                 else:
                    v22 = int(variables[val2])
            else :
                v22 = int(val2)
            if type(v11) == int and type(v22) == int:
                out = doMath(v11, v22, oper)
            else:
                out = doNp(v11, v22, oper)
        #    add to variables
            variables.update({var : out})    
            print("" + var + " => " + str(out))
            
        elif checkReg(pattern['var'], commands):
            var, val = checkReg(pattern['var'], commands)  
            variables.update({var : val})
            # print(variables)
        elif checkReg(pattern['print'], commands):
            values = checkReg(pattern['print'], commands)
            print(variables[var])
        elif variables.keys().__contains__(commands):
            print(variables[commands])
        elif commands == "cls":
            os.system('cls')
            
            
        elif checkReg(pattern['fun'], commands) :
            fun, val = checkReg(pattern['fun'], commands)
            match fun:
             case "inv":
                if(variables.keys().__contains__(val)):
                    if type(variables[val]) == np.ndarray:
                        print(np.linalg.inv(variables[val]))
                    else:
                        print(1 / variables[val])    
             case "solve":
                # print(variables[val].replace(" ", ""))
                w = findChar(variables[val].replace(" ", ""))
                if w == False:
                    print("Invalid equation")
                    
                nums = parse_equation(variables[val].replace(" ", ""))
                
                
                print( w + " => " + str(solve_quadratic( nums[0], nums[1], nums[2])))     
           
                
            
        elif checkReg(pattern['d_mat'], commands):
            v, val = checkReg(pattern['d_mat'], commands)  
            ls = []
            if val.__contains__(";"):
                ss = val.split(";")
              
                for s in ss:
                    ls.append(list(map(int, s.split(","))))
                    
            else :    
               ls = list(map(int, val.split(",")))
            variables[v] = np.array(ls)
            print(variables[v])
            
        elif commands == "clc":
          variables.clear()
            
        elif commands == "vars":
            for key in variables:
                print(key + " => " + str(variables[key]))
        else:
            print("Invalid command")
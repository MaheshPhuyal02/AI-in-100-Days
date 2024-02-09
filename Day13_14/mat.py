import numpy as np
import re as regex
import os

def checkReg(reg, string):
    match = regex.search(reg, string)
    if match:
        return match.groups()
    else:
        return False
    
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
    "d_mat":r'(\w+)\s*=\s*\[([\d\s,]+)\]',
    "p_op" : r'(\w+)\s*([+\-*/])\s*(\w+)',
    "oper" : r'(\w+)\s*=\s*(\w+)\s*([\+\-\*\/])\s*(\w+)',
    "var" : r'(\w+)\s*=\s*(\w+)',
    "print" : r'print\((\w+)\)',
    
}]

while True:  
    commands = input( appName + " >> ")
    commands = commands.strip()
    if commands == "exit":
        print("Exiting...")
        break
    
    for pattern in patterns:
        if checkReg(pattern['val'], commands):
            var, val = checkReg(pattern['val'], commands)
            variables[var] = int(val)
            # print(variables)
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
                    v11 = variables[val1]
            else :
                v11 = int(val1)
                
            if variables.keys().__contains__(val2):
                 if type(variables[val2]) == np.ndarray:
                    v22 = np.array(variables[val2])
                 else:
                    v22 = variables[val2]
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
            variables[var] = variables[val]
            # print(variables)
        elif checkReg(pattern['print'], commands):
            values = checkReg(pattern['print'], commands)
            print(variables[var])
        elif variables.keys().__contains__(commands):
            print(variables[commands])
        elif commands == "cls":
            os.system('cls')
            
        elif checkReg(pattern['d_mat'], commands):
            v, val = checkReg(pattern['d_mat'], commands)  
            ls = list(map(int, val.split(",")))
            variables[v] = np.array(ls)
            print(variables[v])
            
        else:
            print("Invalid command")
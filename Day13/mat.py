import numpy as np
import re as regex
import os

def checkReg(reg, string):
    match = regex.search(reg, string)
    if match:
        return match.groups()
    else:
        return False

appName = "MathPy"
os.system('cls')

variables = {}
patterns = [{
    "val" : r'(\w+)\s*=\s*(\d+)',   
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
            v11 = 0
            v22 = 0
            if variables.keys().__contains__(v1):
                v11 = variables[v1]
            else :
                v11 = int(v1)
            
            if variables.keys().__contains__(v2):
                v22 = variables[v2]
            else :
                v22 = int(v2)
                
            if oper == "+":
                out = v11 + v22
            elif oper == "-":
                out = v11 - v22
            elif oper == "*":
                out = v11 * v22
            elif oper == "/":
                out = v11 / v22
            elif oper == "%":
                out = v11 % v22
            print(out)
        elif checkReg(pattern['oper'], commands):
            var, val1, oper, val2 = checkReg(pattern['oper'], commands)
            
            v11 = 0
            v22 = 0
            out = 0
            if variables.keys().__contains__(val1):
                v11 = variables[val1]
            else :
                v11 = int(val1)
                
            if variables.keys().__contains__(val2):
                v22 = variables[val2]
            else :
                v22 = int(val2)
                
            if oper == "+":
                out = v11 + v22
            elif oper == "-":
                out = v11 - v22
            elif oper == "*":
                out = v11 * v22
            elif oper == "/":
                out = v11 / v22
            elif oper == "%":
                out = v11 % v22
           
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
        else:
            print("Invalid command")
    
    
    
        
        
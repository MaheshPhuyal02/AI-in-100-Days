while True:
   fnum = int(input("Enter first number : "))
   snum = int(input("Enter second number : "))
   sign = input("Enter sign ( + - / x ) : ")

   if sign == "+" :
      print(str(fnum) + " + " + str(snum) + " = " + str(fnum + snum))
   elif sign == "-":
      print(str(fnum) + " - " + str(snum) + " = " + str(fnum - snum))
   elif sign == "/":
      print(str(fnum) + " / " + str(snum) + " = " + str(fnum / snum))
   elif sign == "x":
      print(str(fnum) + " x " + str(snum) + " = " + str(fnum * snum))
   else:
      print("Invalid sign ")      
      break  

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

ch = input("Enter word : ")
list = list(ch)
h = 0
while h <= fact(len(list) - 1):
   
   i = 0
   while i<len(list) - 1:
      s = list[i]
      list[i] = list[i+1]
      list[i+1] = s
      print(''.join(str(e) for e in list)) 
      i += 1
      

   h += 1   


      
    
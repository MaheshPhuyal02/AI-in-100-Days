import os

def addStudent():
    global l
    name = input("Enter name of student : ")
    roll = int(input("Enter roll no. : "))
    major = input("Enter major of the student : ")
    id = len(l)
    l.append({'name':name,  'roll':roll,'major':major, 'id':id})

def removeStudent():
    global l
    roll = int(input("Enter roll no. : "))
    for i in l:
        if i['roll'] == roll:
            l.remove(i)
           

def printAll():
    global l
    if len(l) > 0:
     for i in l:
        print("Name = " + i.get('name'))
        print("Roll no. = " + str(i.get('roll')))
        print("Major = " + i.get('major'))
    else:
        print("No students :/")    

def printOf():
       global l
       roll = int(input("Enter roll no. : "))
       for i in l:
        if i['roll'] == roll:
         print("Name = " + str(i['name']))
         print("Roll no. = " + str(i["roll"]))
         print("Major = " + i["major"])

def updateStudent():
    global l
    roll = int(input("Enter roll no. : "))
    for i in l:
        if i['roll'] == roll:
           name = input("Update name : ")
           roll = int(input("Update roll no. : "))
           major = input("Update major of the student : ")
           id = i['id']
           l.insert(id, {'name':name,  'roll':roll,'major':major})
           l.remove(i)
           break


inn = "\n"
l = []
os.system("cls")

print("Welcome to Moonlight School, Class 10 ".center(50))
print("")
print("")

command = int(input(
    "[0] = Get all students\n" + 
    "[1] = Data of one student\n" + 
                    "[2] = Sort Asc.\n[3] = Sort Dsc.\n[4] = Add Student\n"
                    +"[5] = Update Student\n" + 
                    "[6] = Remove Student\n" + 
                    "[7] = Clear list \n"))

while True:
 match(command):
    case 0:
        printAll()
    case 1:
        printOf()
    case 2:
        l.sort(key=lambda k:k['roll'])
    case 3:
        l.sort(key=lambda k:k['roll'], reverse=True)
    case 4:
        addStudent()
    case 5:
        updateStudent()
    case 6:
        removeStudent()
    case 7:
        l.clear()   
    case _:
          print("Unknown command")
          exit()         
 print("-------------------------------------------------------")   
 command = int(input("Enter command : "))
     


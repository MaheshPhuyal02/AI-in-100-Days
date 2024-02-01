lString = input("Enter list seperate members by , : ")
l = lString.rsplit(",")
if len(l) <= 0:
    print("List is empty :( ")
    exit(-1)

command = int(input("[1] = Sort Asc.\n[2] = Sort Dsc.\n[3] = Add Item,\n[4] = Remove Item\n[5] = Clear list \n"))

match(command):
    case 1:
        l.sort()
    case 2:
        l.sort(reverse=True)
    case 3:
        i = int(input("Enter item : "))
        l.append(i)
    case 4:
        index = int(input("Enter index : "))
        l.pop(index)
    case 5:
        l.clear()
    case _:
        print("Command not found.. Exiting...")
        exit()
print("List : " + str(l))        
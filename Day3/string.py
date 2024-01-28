inn = input("Enter the sentance : ")

print("Upper all : " + inn.upper())
print("Lower all : " + inn.lower())
print("Capitalize : " + inn.capitalize())
print("To title : " + inn.title())

f = input("Enter word to search : ")

if inn.lower().find(f.lower()) > 0 :
    r = input("Enter a word to replace with : ")
    inn = inn.replace(f, r)
    print("New sentence  : " + inn)
else :
    print("Not found. ")    

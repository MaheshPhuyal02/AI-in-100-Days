word = input("Enter word : ")
revWord = ""
pos = 0

for i in range( -1 * len(word), 0):
    revWord = revWord +  word[ ((-1 * i) - 1)]
    pos = pos+1

print("Reverse : " + revWord)
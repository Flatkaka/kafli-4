s = input("Input a string: ")

for x in range(0,(len(s))):
    if (s[x].isdigit()) == True:
        print(s[x], end='')
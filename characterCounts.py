setning = input("Enter a sentence: ")
tala = 0
stor = 0
litill = 0
rest = 0
space = 0
for x in range(0,len(setning)):
    if setning[x].isdigit() == True:
        tala += 1
    elif setning[x].isupper() == True:
        stor += 1
    elif setning[x].islower() == True:
        litill += 1
    elif setning[x].isspace() == True:
        space += 1
    else:
        rest += 1
print('{:>15s}  {:>5d}'.format('Upper case', stor))
print('{:>15s}  {:>5d}'.format('Lower case', litill))
print('{:>15s}  {:>5d}'.format('Digits', tala))
print('{:>15s}  {:>5d}'.format('Punctuation', rest))
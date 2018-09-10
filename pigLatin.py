word = input("Enter a word: ")
count = 0
while word !='.':
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        print(word + "yay")
    else:
        for x in range(0,len(word)):
            if word[x] == 'a' or word[x] == 'e' or word[x] == 'i' or word[x] == 'o' or word[x] == 'u':
                break
            count += 1
        print( word[count:]+word[:count]+'ay')
    word = input("Enter a word: ")
    count = 0
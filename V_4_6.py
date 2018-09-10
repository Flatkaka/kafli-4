name = input("Input a name: ")
fyrir, seinna = name.split(", ")
print(seinna[0].upper() + ". "+ fyrir[0].upper() + fyrir[1:])
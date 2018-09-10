my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code
my_int2 = my_int
fulltala = ""
while my_int > 0:
    binn = my_int % 2
    binn_str = str(binn)
    fulltala = fulltala + binn_str
    my_int = my_int // 2
if my_int2 == 0:
    fulltala = "0"
print("The binary of", my_int2, "is", fulltala[::-1])
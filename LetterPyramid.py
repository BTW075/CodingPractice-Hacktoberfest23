# alphabet pyramid pattern
size = 5
alpha = 65

for i in range(size):
    # print spaces
    for j in range(size - i):
        print(" ", end="")
    # print alphabets
    for k in range(2 * i + 1):
        print(chr(alpha + k), end="")
    print()

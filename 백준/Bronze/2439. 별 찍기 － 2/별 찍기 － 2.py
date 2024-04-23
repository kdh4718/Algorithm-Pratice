star  = int(input())
for i in range(0, star):
    for n in range(0, star-(i+1)):
        print(" ", end="")
    for n in range(0, i+1):
        print("*", end="")
    print("")
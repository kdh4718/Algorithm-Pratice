num = int(input())

def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return int(i)
    return True

while True:
    if num == 1:
        break
    elif prime(num) == True:
        print(num)
        break
    else:
        print(prime(num))
        num /= prime(num)
        num = int(num)
        continue
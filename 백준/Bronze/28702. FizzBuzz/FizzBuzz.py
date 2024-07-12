fb = [str(input()) for _ in range(3)]

for i in range(3):
    try:
        a = int(fb[i])
        num = a+(3-i)
    except:
        continue

if num % 3 == 0:
    if num % 5 == 0:
        print("FizzBuzz")
    else:
        print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)
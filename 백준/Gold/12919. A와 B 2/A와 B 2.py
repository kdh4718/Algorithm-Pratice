a = input()
b = input()
flag = False

def makeWord(a):
    global flag

    if len(a) == len(b):
        if a == b:
            flag = True
            return
    else:
        c = a+"A"
        if c in b or c[::-1] in b:
            makeWord(c)
        d = a+"B"
        if d in b or d[::-1] in b:
            makeWord(d[::-1])

    return

makeWord(a)
print(1 if flag else 0)
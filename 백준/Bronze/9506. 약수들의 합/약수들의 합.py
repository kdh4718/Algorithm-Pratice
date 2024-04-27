while True:
    a = int(input())
    if a == -1:
        break
    div = []

    for i in range(1, a):
        if a % i == 0:
            div.append(i)
    
    if sum(div) == a:
        print(a, "= ", end="")
        for i in div:
            if i == div[-1]:
                print(i)
            else:
                print(i, "+ ", end="")
    else:
        print(a,"is NOT perfect.")
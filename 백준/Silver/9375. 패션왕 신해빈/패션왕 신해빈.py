t = int(input())
for _ in range(t):
    n = int(input())
    clo = dict()
    for i in range(n):
        name, typ = map(str, input().split())
        if typ in clo:
            clo[typ].append(name)  
        else:
            clo[typ] = [name]  
    
    cnt = 1 

    for k in clo:
        cnt *= (len(clo[k])+1)
    print(cnt-1)
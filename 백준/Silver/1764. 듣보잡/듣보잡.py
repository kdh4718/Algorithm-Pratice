n, m = map(int, input().split())
listen = list(input() for i in range(n))
look = list(input() for i in range(m))

listen_look = list(set(listen).intersection(look))
print(len(listen_look))
for i in sorted(listen_look):
    print(i)
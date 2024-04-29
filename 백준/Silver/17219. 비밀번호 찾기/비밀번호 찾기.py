n, m = map(int, input().split())
password = {}

for i in range(n):
    site, pswd = map(str, input().split())
    
    password[site] = pswd
    
for i in range(m):
    site = input()
    print(password[site])
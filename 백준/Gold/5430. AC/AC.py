from collections import deque

t = int(input())
for _ in range(t):
    error_flag = False
    reverse_flag = False
    p = list(input())
    n = int(input())
    n_list = input().strip()[1:-1].split(",")
    n_list = deque(n_list)
    
    if n == 0:
        n_list = []
    
    for i in p:
        if i == "R":
            reverse_flag = not reverse_flag
        else:
            if not n_list:
                print('error')
                error_flag = True
                break
                
            if reverse_flag:
                n_list.pop()
            else:
                n_list.popleft()
        
    if not error_flag:
        if reverse_flag:
            n_list.reverse()
            
        print("[" + ",".join(n_list) + "]")
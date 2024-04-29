n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))
mini = 1e9
start = []
link = []
def dfs(a, start_remain, link_remain):
    global mini, start, link
    len_start = len(start)
    len_link = len(link)
    if a == n:
        sum_start = 0
        for i in start:
            for j in range(len_start):
                sum_start += n_list[i][start[j]]
                
        sum_link = 0
        for i in link:
            for j in range(len_link):
                sum_link += n_list[i][link[j]]
        
        mini = min(mini, abs(sum_start-sum_link))
        
        return
    
    if start_remain:
        start.append(a)
        dfs(a+1, start_remain-1, link_remain)
        start.pop()
    if link_remain:
        link.append(a)
        dfs(a+1, start_remain, link_remain-1)
        link.pop()
        
    
dfs(0, n//2, n//2)
print(mini)
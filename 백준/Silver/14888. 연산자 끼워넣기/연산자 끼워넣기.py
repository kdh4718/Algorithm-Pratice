n = int(input())
n_list = list(map(int, input().split()))
op = list(map(int, input().split()))
mini = 1e9
maxi = -1e9
def dfs(depth, total, p, m, e, d):
    global mini, maxi
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if p:
        dfs(depth+1, total + n_list[depth], p-1, m, e, d)
    if m:
        dfs(depth+1, total - n_list[depth], p, m-1, e, d)
    if e:
        dfs(depth+1, total * n_list[depth], p, m, e-1, d)
    if d:
        dfs(depth+1, int(total / n_list[depth]), p, m, e, d-1)
dfs(1, n_list[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)
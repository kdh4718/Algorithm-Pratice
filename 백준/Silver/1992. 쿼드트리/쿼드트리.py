n = int(input())
tree = [list(map(int, input())) for _ in range(n)]
answer = ""

def Quad_Tree(x, y, N):
    global answer
    point = tree[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if tree[i][j] != point:
                answer += "("
                Quad_Tree(x, y, N//2)
                Quad_Tree(x, y + N//2, N//2)
                Quad_Tree(x + N//2, y, N//2)
                Quad_Tree(x + N//2, y + N//2, N//2)
                answer += ")"
                return
    
    if point == 0:
        answer += "0"
    else:
        answer += "1"
    
    return
    
Quad_Tree(0, 0, n)
print(answer)
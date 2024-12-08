def find(line):
    return not sum(line)

def solution(wallpaper):
    answer = []
    graph = [[0 if i == '.' else 1 for i in list(wall)] for wall in wallpaper]
    length = len(graph)
    dir = [0, 0, length, len(graph[0])]
    
    for i in range(4):
        num = 0
        
        while True:
            if i == 0:
                line = graph[num]
                print(1, line)
            elif i == 1:
                line = [graph[i][num] for i in range(length)]
                print(2, line)
            elif i == 2:
                line = graph[length - num - 1]
                print(3, line)
            else:
                line = [graph[i][len(graph[0]) - num - 1] for i in range(length)]
                print(4, line)
                
            if not find(line): break
            num += 1
        
        num = abs(dir[i] - num)
        
        answer.append(num)
    
    return answer
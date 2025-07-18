def make_server(server, hour, k, count):
    for i in range(hour, min(len(server), hour + k)):
        server[i] += count
    
    return server

def solution(players, m, k):
    server = [0] * 24
    answer = 0
    
    for hour, num in enumerate(players):
        need = (num // m) - server[hour]
        
        if need > 0:
            server = make_server(server, hour, k, need)
            answer += need
    
    return answer
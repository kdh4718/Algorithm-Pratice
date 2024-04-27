from itertools import permutations

def solution(user_id, banned_id):
    user_per = list(permutations(user_id, len(banned_id)))
    answer = []
    
    def check(user, ban):
        for i in range(len(user)):
            if len(user[i]) != len(ban[i]):
                return False
            
            for j in range(len(user[i])):
                if ban[i][j] == "*":
                    continue
                    
                if user[i][j] != ban[i][j]:
                    return False
        
        return True
    
    for user in user_per:
        if not check(user, banned_id):
            continue
        else:
            user = set(user)
            if user not in answer:
                answer.append(user)
    
    return len(answer)
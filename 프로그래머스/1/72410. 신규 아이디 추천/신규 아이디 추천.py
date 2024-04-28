import re

def solution(new_id):
    answer = re.sub(r'[^\w\-_.]', '', new_id.lower())
    answer = re.sub(r'\.+', '.', answer)
    answer = re.sub(r'^\.|\.$', '', answer)
    answer = re.sub(r'\.$', '', answer[:15])
    
    if not answer:
        answer = 'a'
        
    while len(answer) < 3:
        answer += answer[-1]

    return answer
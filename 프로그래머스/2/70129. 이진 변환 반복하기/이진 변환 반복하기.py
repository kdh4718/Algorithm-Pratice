def solution(s):
    change, count = 0, 0
    
    while s != '1':
        change += 1
        count += s.count('0') 
        s = str(bin(s.count('1')))[2:]
    
    return [change, count]
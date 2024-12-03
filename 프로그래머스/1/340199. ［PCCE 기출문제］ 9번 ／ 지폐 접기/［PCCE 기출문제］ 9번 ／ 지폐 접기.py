def check(bill, wallet):
    if bill[0] > wallet[0] or bill[1] > wallet[1]:
        return False
    
    return True

def solution(wallet, bill):
    answer = 0
    wallet.sort()
    
    while True:
        bill.sort()
        flag = check(bill, wallet)
        
        if flag: break
        
        bill[1] //= 2
        answer += 1
    
    return answer
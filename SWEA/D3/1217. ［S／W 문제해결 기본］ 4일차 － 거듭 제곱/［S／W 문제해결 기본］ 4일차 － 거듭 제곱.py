for test_case in range(1, 11):
    num = int(input())
    n, m = map(int, input().split())
    
    def multi(a, b):
        if b == 1:
            return a
        
        return a*multi(a, b-1)
        
    
    print(f"#{num}", multi(n, m))
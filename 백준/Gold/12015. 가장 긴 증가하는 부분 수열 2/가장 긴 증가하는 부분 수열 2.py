n = int(input())
sequence = list(map(int, input().split()))
cnt = [0]

for seq in sequence:
    if cnt[-1] < seq:
        cnt.append(seq)
        
    else:
        start = 0
        end = len(cnt)
        
        while start < end:
            mid = (start + end) // 2
    
            if cnt[mid] < seq:
                start = mid + 1
            else:
                end = mid
                
        cnt[end] = seq
                
print(len(cnt)-1)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    
    for i in range(dump):      
        min_box = min(box)
        max_box = max(box)
        
        if max_box - min_box <= 1:
            break
        
        box[box.index(min_box)] += 1
        box[box.index(max_box)] -= 1
        
    print(f'#{test_case}', max(box) - min(box))
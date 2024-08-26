n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
nums.sort()
stack = []
minimum = float('inf')

for i in range(n):
    stack.append(nums[i])
    
    while len(stack) >= 2 and abs(stack[0] - stack[-1]) >= m:
        minimum = min(minimum, abs(stack[0] - stack[-1]))
        stack.pop(0)

print(minimum)
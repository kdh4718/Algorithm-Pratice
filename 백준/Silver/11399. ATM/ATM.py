n = int(input())
person = list(map(int, input().split()))
person.sort()
for i in range(1, n):
    person[i] += person[i-1]
print(sum(person))
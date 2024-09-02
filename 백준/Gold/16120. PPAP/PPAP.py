ppap = list(input())
stack = []

for p in ppap:
    stack.append(p)

    while stack[-4:] == ['P', 'P', 'A', 'P']:
        del stack[-4:]
        stack.append('P')

print('PPAP' if stack == ['P'] else 'NP')

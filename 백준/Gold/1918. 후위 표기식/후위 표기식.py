inOrder = list(input())
stack = []
postOrder = []
priority = {'*':3,'/':3,'+':2,'-':2,'(':1}

for order in inOrder:
    if order.isalpha():
        postOrder.append(order)
    elif order == '(':
        stack.append(order)
    elif order == ')':
        while stack[-1] != '(':
            postOrder.append(stack.pop())
        stack.pop()
    else:
        while stack and priority[stack[-1]] >= priority[order]:
            postOrder.append(stack.pop())
        stack.append(order)

while stack:
    postOrder.append(stack.pop())

for order in postOrder:
    print(order, end="")

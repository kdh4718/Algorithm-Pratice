for test_case in range(1, 11):
    n = int(input())
    tree = [""] * (n + 1)
    result = 0

    def postOrder(root):
        if root > n:
            return
        elif len(tree[root]) == 1:
            return int(tree[root][0])

        numLeft = postOrder(int(tree[root][1]))
        numRight = postOrder(int(tree[root][2]))

        if tree[root][0] == '*':
            return numLeft * numRight
        elif tree[root][0] == '/':
            return numLeft // numRight
        elif tree[root][0] == '+':
            return numLeft + numRight
        elif tree[root][0] == '-':
            return numLeft - numRight

    for _ in range(n):
        node = input().split()
        tree[int(node[0])] = node[1:]

    print(f"#{test_case}", postOrder(1))

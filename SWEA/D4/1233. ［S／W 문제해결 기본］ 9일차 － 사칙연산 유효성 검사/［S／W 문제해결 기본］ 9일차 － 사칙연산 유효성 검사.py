for test_case in range(1, 11):
    n = int(input())
    tree = [""] * (n + 1)
    result = 0
    operator = ['*', '/', '+', '-']

    def postOrder(root):
        if root > n:
            return
        elif len(tree[root]) <= 1:
            if tree[root][0].isdigit():
                return 1
            else:
                return 0

        numLeft = postOrder(root*2)
        numRight = postOrder((root*2)+1)

        if numLeft == 0 or numRight == 0:
            return 0

        if tree[root][0] in operator:
            return 1
        else:
            return 0

    for _ in range(n):
        node = input().split()
        tree[int(node[0])] = node[1:]

    print(f"#{test_case}", postOrder(1))

for test_case in range(1, 11):
    n = int(input())
    tree = [[] for _ in range(n+1)]
    result = ""

    def inOrder(root):
        global result
        if root > n:
            return

        inOrder(root*2)
        result += tree[root][0][0]
        inOrder((root*2) + 1)

    for _ in range(n):
        node = list(map(str, input().split()))
        tree[int(node[0])].append(node[1:])

    inOrder(1)

    print(f"#{test_case}", result)
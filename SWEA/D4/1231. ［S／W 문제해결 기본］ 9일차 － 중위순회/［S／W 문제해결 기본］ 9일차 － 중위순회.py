for test_case in range(1, 11):
    n = int(input())
    tree = [""] * (n + 1)
    result = ""

    def inOrder(root):
        global result
        if root > n:
            return

        inOrder(root * 2)
        result += tree[root]
        inOrder((root * 2) + 1)

    for _ in range(n):
        node = input().split()
        tree[int(node[0])] = node[1]

    inOrder(1)

    print(f"#{test_case} {result}")

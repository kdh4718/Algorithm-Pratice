import sys

sys.setrecursionlimit(10 ** 6)


def postOrder(start, end):
    if start > end:
        return
    root = preOrder[start]
    splitPoint = start + 1

    while splitPoint <= end and preOrder[splitPoint] < root:
        splitPoint += 1

    postOrder(start + 1, splitPoint - 1)
    postOrder(splitPoint, end)
    print(root)


preOrder = []
while True:
    try:
        preOrder.append(int(input()))
    except:
        break

postOrder(0, len(preOrder) - 1)

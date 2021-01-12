class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def construct(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = construct(arr, root.left, 2 * i + 1, n)
        root.right = construct(arr, root.right, 2 * i + 2, n)
    return root


def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)


def BranchSum(root):
    sum = []
    calculateBranchSum(root, 0, sum)
    return sum


def calculateBranchSum(root, runningSum, sum):
    if root is None:
        return
    newRunningSum = runningSum+root.data
    if root.left is None and root.right is None:
        sum.append(newRunningSum)
        return
    calculateBranchSum(root.left, newRunningSum, sum)
    calculateBranchSum(root.right, newRunningSum, sum)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
    root = None
    n = len(arr)
    root = construct(arr, root, 0, n)
    # inOrder(root)
    print( BranchSum(root))

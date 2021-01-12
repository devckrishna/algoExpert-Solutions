class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)


def printTree(root):
    if root:
        print(root.val)
        printTree(root.left)
        printTree(root.right)


def findClosestBST(tree, target, closest):
    if tree is None:
        return closest

    if abs(target-closest) > abs(target-tree.val):
        closest = tree.val
    if target < tree.val:
        findClosestBST(tree.left, target, closest)
    elif target > tree.val:
        findClosestBST(tree.right, target, closest)
    else:
        return closest

def findClosestBSTI(tree,target,closest):
    currNode=tree
    while currNode is not None:
        if abs(target-closest) > abs(target-currNode.val):
            closest=currNode.val
        if target < currNode.val:
            currNode=currNode.left
        elif target > currNode.val:
            currNode=currNode.right
        else:
            break
    return closest

if __name__=='__main__':
    r = Node(10)
    insert(r, Node(5))
    insert(r, Node(15))
    insert(r, Node(2))
    insert(r, Node(6))
    insert(r, Node(13))
    insert(r, Node(22))
    insert(r, Node(1))
    insert(r, Node(14))
    print(findClosestBSTI(r, 12, float("infinity")))

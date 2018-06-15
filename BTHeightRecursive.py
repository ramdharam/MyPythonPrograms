class Node:
    def __init__(self,v):
        self.data = v
        self.left = None
        self.right = None

def BTHeight(root):
    if root is None:
        return 0
    l = BTHeight(root.left) + 1
    r = BTHeight(root.right) + 1

    return max(l,r)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(BTHeight(root))
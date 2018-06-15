from collections import deque

class Node:
    def __init__(self,v):
        self.data = v
        self.left = None
        self.right = None

def treeHeight(root):
        if root is None:
            return 0
        q = [root]
        q = deque(q)
        height = 0

        while (True):
            nodes  = len(q)

            if nodes ==0:
                return height
            height += 1

            while (nodes > 0):
                curr = q.popleft()
                if curr.left is not None:
                    q.append(curr.left)
                if curr.right is not None:
                    q.append(curr.right)
                nodes -=1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(treeHeight(root))
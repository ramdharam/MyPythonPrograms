class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    k = 0

    def helper(self, node, k):
        if node:
            self.helper(node.left, k)
            self.k += 1
            if self.k == k:
                return node.val
            self.helper(node.right, k)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root is None:
            return
        if k == 0:
            return 0
        return self.helper(root, k)


b = TreeNode(1)
c = TreeNode(2)
b.right = c
a = Solution()
print(a.kthSmallest(b,2))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res - 1
        
    def dfs(self, root):
        if root == None:
            return 0
        
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.res = max(self.res, l + r + 1)
        return max(l, r) + 1
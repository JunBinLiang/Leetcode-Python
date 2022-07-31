# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1000000000
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if root == None:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.res = max(self.res, l + r + root.val);
        self.res = max(self.res, root.val)
        return max(l + root.val, r + root.val, 0)
        
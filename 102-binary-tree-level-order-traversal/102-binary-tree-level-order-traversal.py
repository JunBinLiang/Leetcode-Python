# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.l1 = []
        self.dfs(root, 1)
        return self.l1
        
    def dfs(self, root, dep):
        if root == None:
            return
        if len(self.l1) < dep:
            self.l1.append([])
        self.l1[dep - 1].append(root.val)
        self.dfs(root.left, dep + 1)
        self.dfs(root.right, dep + 1)
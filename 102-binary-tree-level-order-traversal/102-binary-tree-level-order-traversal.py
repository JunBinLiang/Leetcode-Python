# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        q = deque([root])
        res = []
        
        while len(q) > 0:
            size = len(q)
            level = []
            for i in range(size):
                top = q.popleft()
                level.append(top.val)
                if top.left != None:
                    q.append(top.left)
                if top.right != None:
                    q.append(top.right)
            res.append(level)
        
        return res
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         self.l1 = []
#         self.dfs(root, 1)
#         return self.l1
#         
#     def dfs(self, root, dep):
#         if root == None:
#             return
#         if len(self.l1) < dep:
#             self.l1.append([])
#         self.l1[dep - 1].append(root.val)
#         self.dfs(root.left, dep + 1)
#         self.dfs(root.right, dep + 1)
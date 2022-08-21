# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        g = {}
        g[root.val] = []
        def dfs(root):
            if root == None:
                return
            if root.left != None:
                g[root.left.val] = []
                g[root.left.val].append(root.val)
                g[root.val].append(root.left.val)
            if root.right != None:
                g[root.right.val] = []
                g[root.right.val].append(root.val)
                g[root.val].append(root.right.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        
        q = [start]
        se = set()
        se.add(start)
        res = 0
        while len(q) > 0:
            sz = len(q)
            res += 1
            for i in range(sz):
                top = q[0]
                q.pop(0)
                for nxt in g[top]:
                    if nxt not in se:
                        se.add(nxt)
                        q.append(nxt)
        return res - 1
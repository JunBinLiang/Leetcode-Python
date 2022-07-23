# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        q = [root]
        layer = 0
        while len(q) > 0:
            size = len(q)
            li = []
            for i in range(size):
                top = q[0]
                q.pop(0)
                if top.left != None:
                    q.append(top.left)
                if top.right != None:
                    q.append(top.right)
                li.append(top.val)
                
            if layer % 2 == 1:
                li = li[:: -1]
            
            res.append(li)
            layer += 1
                
        return res
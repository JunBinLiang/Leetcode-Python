"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        q = [root]
        while len(q) > 0:
            le = len(q)
            for i in range(le):
                top = q[0]
                q.pop(0)
                if len(q) > 0 and i != le - 1:
                    top.next = q[0]
                if top.left != None:
                    q.append(top.left)
                if top.right != None:
                    q.append(top.right)
        return root
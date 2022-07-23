# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.dfs(nums, 0, len(nums) - 1)
    
    def dfs(self, a, l, r):
        if l > r:
            return None
        mid = l + (r - l) // 2
        root = TreeNode(a[mid])
        root.left = self.dfs(a, l, mid - 1)
        root.right = self.dfs(a, mid + 1, r)
        return root
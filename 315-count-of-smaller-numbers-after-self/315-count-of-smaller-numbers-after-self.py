class SegmentTree:
    def __init__(self, nums, l , r):    
        self.l = l
        self.r = r
        if l == r:
            self.val = nums[l]
        else:
            mid = l + (r - l) // 2
            self.left = SegmentTree(nums, l, mid)
            self.right = SegmentTree(nums, mid + 1, r)
            self.val = self.left.val + self.right.val
    
    
    def update(self, idx, val):
        if self.l == self.r:
            self.val += val
            return
        
        mid = self.l + (self.r - self.l) // 2
        if idx <= mid:
            self.left.update(idx, val)
        else:
            self.right.update(idx, val)
        self.val = self.left.val + self.right.val
        
           
    def query(self, start, end):
        if self.l == start and self.r == end:
            return self.val
        mid = self.l + (self.r - self.l) // 2
        if end <= mid:
            return self.left.query(start, end)
        if start > mid:
            return self.right.query(start,end)
        return self.left.query(start, mid) + self.right.query(mid + 1, end)

class Solution:
    def countSmaller(self, a: List[int]) -> List[int]:
        n = len(a)
        res = [0] * n
        
        se = set()
        for i in range(n):
            se.add(a[i])
        b = [x for x in se]
        b.sort()
        rank = 1
        f = {}
        for i in range(len(b)):
            f[b[i]] = rank
            rank += 1
            
        
        nums = [0] * (rank + 1)
        seg = SegmentTree(nums, 0, rank)
        
                
        for i in range(n - 1, -1, -1):
            ra = f[a[i]]
            res[i] = seg.query(0, ra - 1)
            seg.update(ra, 1)
        return res
    

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
            self.val = val
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
        
        
        
        
        

class NumArray:
    def __init__(self, nums: List[int]):
        self.seg = SegmentTree(nums, 0, len(nums) - 1)

    def update(self, index: int, val: int) -> None:
        self.seg.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.seg.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
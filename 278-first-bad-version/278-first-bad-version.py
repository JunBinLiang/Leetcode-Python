# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        #g g g     b     b   b b b
        #                x    
        
        
        l = 1
        r = n
        res = -1
        
        while l <= r:
            mid = l + (r - l) // 2
            isb = isBadVersion(mid)
            if isb == False:
                l = mid  +1
            else:
                res = mid #possible candidate
                r = mid - 1
        
        return res
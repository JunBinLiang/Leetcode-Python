class Solution:
    def minEatingSpeed(self, a: List[int], h: int) -> int:
        
        l = 1
        r = max(a)
        res = -1
        
        while l <= r:
            mid = l + (r - l) // 2
            cnt = 0
            for i in a:
                cnt += (i // mid)
                if i % mid != 0:
                    cnt += 1
            if cnt <= h:
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
        return res
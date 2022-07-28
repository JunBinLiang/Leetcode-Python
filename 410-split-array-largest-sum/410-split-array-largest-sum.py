class Solution:
    def splitArray(self, a: List[int], m: int) -> int:
        
        l = max(a)
        r = 1000000000
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            print(l, r, mid)
            #can we divide m array such that sum <= mid
            if self.check(a, mid, m):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
    
    def check(self, a, mid, m):
        total = 0
        cnt = 0
        for i in a:
            if total + i > mid:
                cnt += 1
                total = i
            else:
                total += i
        return cnt + 1 <= m
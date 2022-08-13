class Solution:
    def subarraysWithKDistinct(self, a: List[int], k: int) -> int:
       
        # sliding window => how many subarray with atmost k distinct integers
        def most(a, k):
            if k == 0:
                return 0
            res = 0
            n = len(a)
            f = {}
            l = 0
            for i in range(n):
                if a[i] not in f:
                    f[a[i]] = 0
                f[a[i]] += 1
                while len(f) > k:
                    f[a[l]] -= 1
                    if f[a[l]] == 0:
                        del f[a[l]]
                    l += 1
                res += (i - l + 1)
            return res
                    
                    
         
        # how many subarrays have at most k  distinct integers
        # how many subarrays have at most k - 1 distinct integers
        # subarray with exactly k integers
        return  most(a, k) - most(a, k - 1)
        
        
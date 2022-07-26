class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        f = {0 : 1}
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            if s - k in f.keys():
                res += f[s - k]
                
            if s not in f.keys():
                f[s] = 0
            f[s] += 1
            
        return res
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        odd, even = 0, 0
        sum1 = 0
        
        for i in arr:
            sum1 += i
            if sum1 % 2 == 1:
                res += 1
                res += even
                odd += 1
            else:
                res += odd
                even += 1
        
        
        return res % 1000000007
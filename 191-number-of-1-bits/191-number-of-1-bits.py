class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (n & (1 << i)) != 0:# check if bit is on
                res += 1
            
        return res
    
#0000000000000000000000000000 1 011
#                             1 000
#0000000000000000000000000000 1 000 
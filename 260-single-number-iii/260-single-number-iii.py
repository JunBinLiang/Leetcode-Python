#5 : 30 - 5 : 45

class Solution:
    def singleNumber(self, a: List[int]) -> List[int]:
        res = [0, 0]
        xor = 0
        for i in a:
            xor ^= i
            
        index = -1
        for j in range(32):
            if (xor & (1 << j)) > 0:
                index = j
                
        for i in a:
            if (i & (1 << index)) > 0:
                res[0] ^= i
            
        res[1] = res[0]
        for i in a:
            res[1] ^= i
        
        return res
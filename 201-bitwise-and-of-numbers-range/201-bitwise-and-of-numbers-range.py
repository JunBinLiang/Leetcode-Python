class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        res = 0
        for i in range(31):
            if (left & (1 << i)) == 0:
                continue
            x = 0
            for j in range(0, i):
                if (left & (1 << j)) > 0:
                    x += (1 << j)
            need = (1 << i) - x
            if left + need > right:
                res += (1 << i)
                
        return res
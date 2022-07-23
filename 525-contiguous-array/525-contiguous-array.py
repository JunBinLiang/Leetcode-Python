class Solution:
    def findMaxLength(self, a: List[int]) -> int:
        f = {0 : -1}
        t = 0
        res = 0
        for i in range(len(a)):
            if a[i] == 0:
                t += -1
            else:
                t += 1
            
            if t in f.keys():
                res = max(res, i - f[t])
            else:
                f[t] = i
        
        return res
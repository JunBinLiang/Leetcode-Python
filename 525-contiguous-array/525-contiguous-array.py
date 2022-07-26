class Solution:
    def findMaxLength(self, a: List[int]) -> int:
        for i in range(len(a)):
            if a[i] == 0:
                a[i] = -1
        
        f = {0 : -1}
        t, res = 0, 0
        for i in range(len(a)):
            t += a[i]   
            
            if t in f.keys():
                res = max(res, i - f[t])
            
            if t not in f.keys():
                f[t] = i
        
        return res
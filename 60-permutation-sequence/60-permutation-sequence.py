class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        f = [1] * 15
        seen = [False] * 10    
        for i in range(2, len(f)):
            f[i] = f[i - 1] * i
            
        
        res = ""
        
        for i in range(n):
            t = 0
            x = -1
            for j in range(1, n + 1):
                if seen[j]:
                    continue
                if k <= t + f[n - (i + 1)]:
                    k -= t
                    x = j
                    break
                else:
                    t += f[n - (i + 1)]
            seen[x] = True
            res += str(x)
        return res
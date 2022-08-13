class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = 1000000000
        j = 0
        f = {}
        g = {}
        for i in range(len(t)):
            if t[i] not in g:
                g[t[i]] = 0
            g[t[i]] += 1
        
        l, r = -1, -1
        
        def check():
            for k in g:
                if k not in f or f[k] < g[k]:
                    return False
            return True
        
        for i in range(len(s)):
            if s[i] not in f:
                f[s[i]] = 0
            f[s[i]] += 1
            
            while check():
                le = i - j + 1
                if le < res:
                    res = le
                    l = j
                    r = i
                    
                f[s[j]] -= 1
                j += 1   
                
        if l == -1:
            return ""
        return s[l : r + 1]
                
                
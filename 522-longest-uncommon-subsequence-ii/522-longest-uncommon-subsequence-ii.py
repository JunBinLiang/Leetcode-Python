class Solution:
    def findLUSlength(self, a: List[str]) -> int:
        a = sorted(a, key = len)
        res = -1
        ma = {}

        for s in a:
            if s in ma.keys():
                ma[s] += 1
            else:
                ma[s] = 1
                 
        for i in range(len(a)):
            if ma[a[i]] > 1:
                continue
            good = True
            for j in range(i + 1, len(a)):
                if self.sub(a[i], a[j]):
                    good = False
            if good:
                res = max(res, len(a[i]))
            
        return res
    
    def sub(self, s, t):
        j = 0
        for c in t:
            if c == s[j]:
                j += 1
            if j >= len(s):
                break  
        return j >= len(s)
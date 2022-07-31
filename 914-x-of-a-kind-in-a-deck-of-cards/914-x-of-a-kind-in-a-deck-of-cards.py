class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        f = {}
        for i in deck:
            if i not in f.keys():
                f[i] = 0
            f[i] += 1
        
        a = [x for x in f.values()]
        a.sort()
        g = a[0]
        for i in a:
            g = gcd(g, i)
        
        return g > 1 and True
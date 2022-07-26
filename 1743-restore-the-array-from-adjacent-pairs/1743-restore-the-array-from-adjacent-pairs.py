class Solution:
    def restoreArray(self, a: List[List[int]]) -> List[int]:
        f = {}
        g = {}
        use = set()
        res = []
        for p in a:
            x, y = p[0], p[1]
            if x not in f.keys():
                f[x] = 0
                g[x] = []
            if y not in f.keys():
                f[y] = 0
                g[y] = []
            f[x] += 1
            f[y] += 1
            g[x].append(y)
            g[y].append(x)
        
        for i in f.keys():
            if f[i] == 1:
                res.append(i)
                use.add(i)
                break
        
        
        while len(res) != len(a) + 1:
            last = res[len(res) - 1]
            for nxt in g[last]:
                if nxt not in use:
                    use.add(nxt)
                    res.append(nxt)
        return res
        
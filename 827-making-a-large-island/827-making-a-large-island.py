di = [[0, 1],[0, -1],[1, 0],[-1, 0]]
class Solution:
    def largestIsland(self, a: List[List[int]]) -> int:
        n = len(a)
        m = len(a[0])
        ID = 1
        self.cnt = 0
        res = 0
        
        mark = []
        for i in range(n):
            mark.append([0] * m)
        
        
        def dfs(r, c):
            if r < 0 or r >= n or c < 0 or c >= m:
                return
            if a[r][c] == 0 or mark[r][c] != 0:
                return
            mark[r][c] = ID
            self.cnt += 1
            for d in di:
                nxtr = r + d[0]
                nxtc = c + d[1]
                dfs(nxtr, nxtc)
                
          
        f = {}
        for i in range(n):
            for j in range(m):
                if a[i][j] == 1 and mark[i][j] == 0:
                    self.cnt = 0
                    dfs(i, j)
                    f[ID] = self.cnt
                    ID += 1
                    res = max(res, self.cnt)
                    
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    tot = 1
                    se = set()
                    for d in di:
                        nxtr = i + d[0]
                        nxtc = j + d[1]
                        if nxtr >= 0 and nxtr < n and nxtc >= 0 and nxtc < m and a[nxtr][nxtc] == 1:
                            se.add(mark[nxtr][nxtc])
                    for com in se:
                        tot += f[com]
                    res = max(res, tot)
        return res
                
#1 0
#0 1
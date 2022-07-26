di = [[-1, 0], [1, 0], [0, 1], [0, -1]]

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.res = False
        n = len(grid)
        m = len(grid[0])
        self.visit = []
        for i in range(n):
            self.visit.append([False] * m)
        for i in range(n):
            for j in range(m):
                if self.visit[i][j] == False:
                    self.dfs(grid, -1, -1, i, j)
        return self.res
        
        
    def dfs(self, grid, lastr, lastc, i, j):
        if self.visit[i][j] == True:
            self.res = True
            return
        self.visit[i][j] = True
        
        n = len(grid)
        m = len(grid[0])
        for p in di:
            r = i + p[0]
            c = j + p[1]
            if c < 0 or c >= m or r < 0 or r >= n:
                continue
            if r == lastr and c == lastc:
                continue
            if grid[r][c] == grid[i][j]:
                self.dfs(grid, i, j, r, c)
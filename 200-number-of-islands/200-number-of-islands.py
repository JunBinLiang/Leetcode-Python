class Solution:
    def numIslands(self, a: List[List[str]]) -> int:
        n = len(a)
        m = len(a[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == '1':
                    cnt += 1
                    self.dfs(a, i, j)
        return cnt
    
    def dfs(self, a, r, c):
        n = len(a)
        m = len(a[0])
        if r < 0 or r >= n or c < 0 or c >= m:
            return
        if a[r][c] == '0':
            return
        
        a[r][c] = '0'
        self.dfs(a, r + 1, c)
        self.dfs(a, r - 1, c)
        self.dfs(a, r, c + 1)
        self.dfs(a, r, c - 1)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = []
        for i in range(m):
            a = []
            for j in range(n):
                a.append(-1)
            self.dp.append(a)
        
        return self.recursion(m - 1, n - 1)
        
    def recursion(self, m,n): #O(mn)
        if m == 0 or n == 0:
            return 1
        if self.dp[m][n] != -1:
            return self.dp[m][n]
        self.dp[m][n] = self.recursion(m-1,n)+self.recursion(m, n-1)
        return self.dp[m][n]

        
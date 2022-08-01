#1 : 50 - 2 : 05
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        mod = 1000000007
        
        dp = []
        for i in range(n + 10):
            dp.append([])
            for j in range(n + 10):
                dp[i].append(0)
            
        
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(0, i + 1):
                if s[i - 1] == 'I':
                    for k in range(0, j):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
                else:
                    for k in range(j, i + 1):
                        dp[i][j] += dp[i - 1][k]
                        dp[i][j] %= mod
                
                
                
        res = 0
        for i in range(n + 1):
            res += dp[n][i]
            res %= mod
        return res
                
class Solution:
    def maxSumMinProduct(self, a: List[int]) -> int:
        mod = 1000000000 + 7
        res = 0
        n = len(a)
        
        l = [-1] * n
        r = [-1] * n
        sta = []
        pre = [0] * (n + 1)
        pre[1] = a[0]
        for i in range(1, n):
            pre[i + 1] = a[i] + pre[i]
        
        for i in range(n):
            while len(sta) > 0 and a[i] <= a[sta[-1]]:
                sta.pop(len(sta) - 1)
            
            if len(sta) > 0:
                l[i] = sta[-1]
            sta.append(i)
        
        sta = []
        for i in range(n - 1, -1, -1):
            while len(sta) > 0 and a[i] <= a[sta[-1]]:
                sta.pop(len(sta) - 1)
            if len(sta) > 0:
                r[i] = sta[-1]
            sta.append(i)
            
                    
        for i in range(n):
            ll = l[i] + 1
            rr = r[i]
            if r[i] == -1:
                rr = n
            res = max(res, a[i] * (pre[rr] - pre[ll]))
            
        return int(res % mod)
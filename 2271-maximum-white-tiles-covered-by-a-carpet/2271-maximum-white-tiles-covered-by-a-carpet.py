class Solution:
    def maximumWhiteTiles(self, a: List[List[int]], carpetLen: int) -> int:
        n, res = len(a), 0
        a.sort()
        
        pre = [0] * n
        pre[0] = a[0][1] - a[0][0] + 1
        for i in range(1, n):
            le = a[i][1] - a[i][0] + 1
            pre[i] = pre[i - 1] + le
            
            
        def getPre(l, r):
            if l == 0:
                return pre[r]
            return pre[r] - pre[l - 1]
        
        
        for i in range(n):
            #a[i][0] - to
            to = a[i][0] + carpetLen - 1
            pos = -1
            l, r = i, n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if to >= a[mid][0]:
                    pos = mid
                    l = mid + 1
                else:
                    r = mid - 1
                    
            #cover [i : pos]
            tot = 0
            if i <= pos - 1:
                tot += getPre(i, pos - 1)
                
            if to > a[pos][1]:
                tot += (a[pos][1] - a[pos][0] + 1)
            else:
                tot += (to - a[pos][0] + 1)
            res = max(res, tot)
            
        return res
    
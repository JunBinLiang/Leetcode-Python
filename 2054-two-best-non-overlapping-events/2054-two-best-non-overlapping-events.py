import heapq
class Solution:
    def maxTwoEvents(self, a: List[List[int]]) -> int:
        a.sort()
        res = 0
        
        h = []
        mx = 0
        for i in range(len(a)):
            s, e, val = a[i][0], a[i][1], a[i][2]
            while len(h) > 0 and h[0][0] < s:
                mx = max(mx,heappop(h)[1])    
            res = max(res, mx + val)
            heappush(h, (e, val))
        return res
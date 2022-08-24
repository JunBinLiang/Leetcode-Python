di = [[0, 1],[0, -1],[1, 0],[-1, 0]]
class Solution:
    def largestIsland(self, a: List[List[int]]) -> int:
        def allone(ma):
            for row in ma:
                if sum(row) != len(ma[0]):
                    return False
            return True
        
        n, m = len(a), len(a[0])
        if allone(a):
            return n * m
        res = 0
        def find(nums, x):
            if nums[x] == x:
                return x
            root = find(nums, nums[x])
            nums[x] = root
            return root
        
        nums = [0] * (n * m)
        sizes = [1] * (n * m)
        for i in range(n * m):
            nums[i] = i
            
           
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    continue
                r1 = find(nums, i * m + j)
                for d in di:
                    nxtr = i + d[0]
                    nxtc = j + d[1]
                    if nxtr >= 0 and nxtr < n and nxtc >= 0 and nxtc < m and a[nxtr][nxtc] == 1:
                        r2 = find(nums, nxtr * m + nxtc)
                        if r1 != r2:
                            nums[r2] = r1
                            sizes[r1] += sizes[r2]
                            res = max(res, sizes[r1])
                            
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    se = set()
                    tot = 1
                    for d in di:
                        nxtr = i + d[0]
                        nxtc = j + d[1]
                        if nxtr >= 0 and nxtr < n and nxtc >= 0 and nxtc < m and a[nxtr][nxtc] == 1:
                            r1 = find(nums, nxtr * m + nxtc)
                            se.add(r1)
                    for com in se:
                        tot += sizes[com]
                    res = max(res, tot)
        return res
        
        
        
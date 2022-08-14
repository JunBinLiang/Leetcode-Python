class Solution:
    def largestLocal(self, a: List[List[int]]) -> List[List[int]]:
        n = len(a)
        res = []
        for i in range(n - 2):
            res.append([])
            for j in range(n - 2):
                val = max(max(a[i][j : j + 3]), max(a[i + 1][j:j+3]), max(a[i+2][j:j+3]))
                res[i].append(val)
        return res
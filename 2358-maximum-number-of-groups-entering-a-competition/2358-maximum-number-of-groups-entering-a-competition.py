class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        res = 0
        for i in range(n + 1):
            if i * (i + 1) / 2 <= n:
                res = i
        return res
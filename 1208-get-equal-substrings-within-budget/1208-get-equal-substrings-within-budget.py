class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        res = 0
        n = len(s)
        j = 0
        total = 0
        for i in range(n):
            total += abs(ord(s[i]) - ord(t[i]))
            while total > maxCost:
                total -= abs(ord(s[j]) - ord(t[j]))
                j += 1
            res = max(res, i - j + 1)
        return res
class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        if n < 1000:
            return s
        res = ""
        s = s[::-1]
        for i in range(len(s)):
            res += (s[i])
            if (i + 1) % 3 == 0 and i != len(s) - 1:
                res += '.'
        res = res[::-1]
        return res
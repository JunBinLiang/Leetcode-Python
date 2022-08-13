class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        res = 0
        j, tot = 0, 0
        
        for i in range(len(s)):
            if s[i] == 'F':
                tot += 1
            while tot > k:
                if s[j] == 'F':
                    tot -= 1
                j += 1
            res = max(res, i - j + 1)
            
        j = 0
        tot = 0
        for i in range(len(s)):
            if s[i] == 'T':
                tot += 1
            while tot > k:
                if s[j] == 'T':
                    tot -= 1
                j += 1
            res = max(res, i - j + 1)
            
        return res
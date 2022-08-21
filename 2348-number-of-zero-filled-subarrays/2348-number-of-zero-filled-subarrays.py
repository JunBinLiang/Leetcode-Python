class Solution:
    def zeroFilledSubarray(self, a: List[int]) -> int:
        res = 0
        n = len(a)
        i = 0
        while i < n:
            if a[i] != 0:
                i += 1
                continue
            j = i
            while j < n and a[j] == 0:
                j += 1
            
            cnt = j - i
            res += ((cnt * (cnt + 1)) // 2)
            i = j
        return res
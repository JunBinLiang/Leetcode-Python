class Solution:
    def minOperations(self, a: List[int]) -> int:
        res = 0
        a.sort()
        n = len(a)
        while a[n - 1] != 0:
            cnt = 0
            for i in range(n):
                if a[i] % 2 == 1:
                    a[i] -= 1
                    cnt += 1
            if cnt == 0:
                res += 1
                for i in range(n):
                    a[i] //= 2
            else:
                res += cnt
            a.sort()
        return res
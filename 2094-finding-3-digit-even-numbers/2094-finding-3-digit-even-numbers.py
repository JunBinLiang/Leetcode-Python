class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        f = [0] * 10
        for d in digits:
            f[d] += 1
        
        
        for i in range(100, 1000, 2):
            val = i
            cnt = [0] * 10
            while val > 0:
                d = val % 10
                val //= 10
                cnt[d] += 1
            
            flag = True
            for j in range(10):
                if cnt[j] > f[j]:
                    flag = False
            if flag:
                res.append(i)
        return res
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], k: int) -> int:
        n = len(customers)
        sum1, res = 0, 0
        tot1, tot2 = 0, 0
        for i in range(n):
            if grumpy[i] == 0:
                sum1 += customers[i]
        
        
        for i in range(n):
            tot1 += customers[i]
            if grumpy[i] == 0:
                tot2 += customers[i]
            if i >= k - 1:
                res = max(res, sum1 - tot2 + tot1)
                tot1 -= customers[i - k + 1]
                if grumpy[i - k + 1] == 0:
                    tot2 -= customers[i - k + 1]  
        return res
        
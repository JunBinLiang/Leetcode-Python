class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        mn = prices[0]
        for i in range(1, len(prices)):
            res = max(res, prices[i] - mn)
            mn = min(mn, prices[i])
        return res
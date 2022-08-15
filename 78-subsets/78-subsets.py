class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        res = []
        n = len(a)
        
        for state in range(0, 1 << n):
            subset = []
            for j in range(n):
                if (state & (1 << j)) > 0:
                    subset.append(a[j])
            res.append(subset)
        return res
    
#0 1 2 3 4 5 6 7
#        111
class Solution:
    def waysToMakeFair(self, a: List[int]) -> int:
        n = len(a)
        rodd =[0] * n
        reven =[0] * n
        
        odd, even = 0, 0
        res = 0
        for i in range(n - 1, -1, -1):
            if i % 2 == 0:
                even += a[i]
            else:
                odd += a[i]
            rodd[i] = odd
            reven[i] = even
            

        odd = 0
        even = 0
        
        for i in range(n):
            if i == n - 1:
                if even == odd:
                    res += 1
                continue
            
            if odd + reven[i + 1] == even + rodd[i + 1]:
                res += 1
        
            if i % 2 == 0:
                even += a[i]
            else:
                odd += a[i]
        
        return res
        
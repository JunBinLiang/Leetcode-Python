class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        n = len(a)
        l = [0] * n
        r = [0] * n
        
        l[0] = a[0]
        for i in range(1, n):
            l[i] = l[i - 1] * a[i]
            
        r[n - 1] = a[n - 1]
        for i in range(n - 2, -1, -1):
            r[i] = a[i] * r[i + 1]
            
        for i in range(n):
            if i == 0:
                a[i] = r[i + 1]
            elif i == n - 1:
                a[i] = l[i - 1]
            else:
                a[i] = l[i - 1] * r[i + 1]
                
        return a
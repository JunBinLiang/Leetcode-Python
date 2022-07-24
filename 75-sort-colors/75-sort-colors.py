class Solution:
    def sortColors(self, a: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        idx = 0
        for i in range(len(a)):
            if a[i] == 0:
                t = a[idx]
                a[idx] = 0
                a[i] = t
                idx += 1
                
        for i in range(len(a)):
            if a[i] == 1:
                t = a[idx]
                a[idx] = 1
                a[i] = t
                idx += 1
                
        return a
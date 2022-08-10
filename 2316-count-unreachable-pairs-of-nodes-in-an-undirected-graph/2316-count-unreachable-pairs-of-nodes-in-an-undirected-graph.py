class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        nums = [0] * n
        for i in range(n):
            nums[i] = i
        
        for edge in edges:
            u, v = edge[0], edge[1]
            r1 = self.find(nums, u)
            r2 = self.find(nums, v)
            if r1 != r2:
                nums[r1] = r2
        
        f = {}
        for i in range(n):
            r = self.find(nums, i)
            if r not in f:
                f[r] = 1
            else:
                f[r] += 1
        
        for i in range(n):
            r = self.find(nums, i)
            res += (n - f[r])
        return res // 2
            
    
    def find(self, nums, x):
        if nums[x] == x:
            return x
        root = self.find(nums, nums[x])
        nums[x] = root
        return root
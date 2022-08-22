class Solution:
    def maximumSegmentSum(self, a: List[int], q: List[int]) -> List[int]:
        n = len(a)
        res = [0] * n
        
        def find(nums, x):
            if nums[x] == x:
                return x
            root = find(nums, nums[x])
            nums[x] = root
            return root
        
        
        nums = [0] * n
        vals = [0] * n
        for i in range(n):
            nums[i] = i
        
        
        
        
        mx = 0
        for i in range(n - 1, -1, -1):
            res[i] = mx
            idx = q[i]
            vals[idx] = a[idx]
            mx = max(mx, a[idx])
            a[idx] = 0
            
            if idx - 1 >= 0 and a[idx - 1] == 0:
                r1 = find(nums, idx - 1)
                r2 = find(nums, idx)
                if r1 != r2:
                    nums[r1] = r2
                    vals[r2] += vals[r1]
                    mx = max(mx, vals[r2])
                    
            if idx + 1 < n and a[idx + 1] == 0:
                r1 = find(nums, idx + 1)
                r2 = find(nums, idx)
                if r1 != r2:
                    nums[r1] = r2
                    vals[r2] += vals[r1]
                    mx = max(mx, vals[r2])
            
        return res
            
        
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        def good(c):
            if c in ['a', 'e', 'i', 'o', 'u']:
                return True
            return False
        
        res, cnt = 0, 0
        l = 0
        for i in range(len(s)):
            if good(s[i]):
                cnt += 1
            while i - l + 1 >= k:
                res = max(res, cnt)
                if good(s[l]):
                    cnt -= 1
                l += 1
                
        return res
    
    
#class Solution:
#    def maxVowels(self, s: str, k: int) -> int:
#        
#        def good(c):
#            if c in ['a', 'e', 'i', 'o', 'u']:
#                return True
#            return False
#        
#        res, cnt = 0, 0
#        for i in range(len(s)):
#            if good(s[i]):
#                cnt += 1
#            if i < k - 1:
#                continue  
#            res = max(res, cnt)    
#            if good(s[i - k + 1]):
#                cnt -= 1
#        return res
            
                
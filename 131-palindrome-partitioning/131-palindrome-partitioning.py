class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, 0, [])
        return self.res
        
    def dfs(self, s, idx, li):
        if idx == len(s):
            self.res.append([x for x in li])
            return
        
        for j in range(idx, len(s)):
            #s[idx : j]
            newstr = s[idx : j + 1]
            if newstr == newstr[::-1]:
                li.append(newstr)
                self.dfs(s, j + 1, li)
                li.pop()
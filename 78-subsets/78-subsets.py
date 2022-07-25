class Solution:
    def subsets(self, a: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(a, 0, [])
        return self.res
    
    def dfs(self, a, i, cur):
        if i >= len(a):
            self.res.append([x for x in cur])
            return
        
        #take
        cur.append(a[i])
        self.dfs(a, i + 1, cur)
        cur.pop()
        
        
        #untake
        #add nothing
        self.dfs(a, i + 1, cur)
        #remove nothing
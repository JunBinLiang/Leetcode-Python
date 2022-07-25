class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res=[]
        self.list1=list(s)
        self.dfs(0,"",[],s)
        return self.res
    
    def dfs(self,i,tmpString,tmpList,s):
        if i==len(s):
            for p in tmpList:
                if p!=p[::-1]:
                    return
            le = 0
            for j in tmpList:
                le += len(j)
            if le == len(s):
                self.res.append(tmpList.copy())
            return
        
       
    
    
        tmpString=tmpString+s[i]
        self.dfs(i+1,tmpString,tmpList,s)
        
        tmpList.append(tmpString)
        self.dfs(i+1,"",tmpList,s)
        tmpList.pop()

class Solution:
    def closestMeetingNode(self, a: List[int], node1: int, node2: int) -> int:
        visit = [False] * len(a)
        def dfs(a, u, dep, dic):
            if u == -1 or visit[u]:
                return
            visit[u] = True
            dic[u] = dep
            dfs(a, a[u], dep + 1, dic)
            
        dic1 = {}
        dic2 = {}
        
        dfs(a, node1, 0, dic1)
        visit = [False] * len(a)
        dfs(a, node2, 0, dic2)
        
        mn = 1000000000
        res = 1000000000
        for k in dic1:
            if k in dic2:
                mn = min(mn, max(dic1[k], dic2[k]))
                
        if mn == 1000000000:
            return -1
        
        for k in dic1:
            if k in dic2:
                if mn == max(dic1[k], dic2[k]):
                    res = min(res, k)
    
        return res
                
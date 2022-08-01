class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = {}
        for i in range(numCourses):
            g[i] = []
        
        ind = [0] * numCourses
        for edge in prerequisites:
            g[edge[1]].append(edge[0])
            ind[edge[0]] += 1
            
            
        q = []
        visit = set()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)
                visit.add(i)
                
        while len(q) > 0:
            top = q[0]
            q.pop(0)
            for nxt in g[top]:
                if nxt in visit:
                    return False
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    q.append(nxt)
                    visit.add(nxt)
        
        return len(visit) == numCourses
            
                
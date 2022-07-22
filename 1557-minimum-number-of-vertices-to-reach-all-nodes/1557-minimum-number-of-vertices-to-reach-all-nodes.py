class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ind = [0] * n
        res = []
        for e in edges:
            ind[e[1]] += 1
        
        for i in range(n):
            if ind[i] == 0:
                res.append(i)
        return res
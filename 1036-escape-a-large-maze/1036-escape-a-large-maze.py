di = [[0, 1], [0, -1], [1, 0], [-1, 0]]

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        
        return self.bfs(source, target, blocked) and self.bfs(target, source, blocked)
        
        
    def bfs(self, a, b, block):
        s = set()
        visit = set()
        
        step = 0
        q = []
        q.append(a)
        visit.add(tuple(a))
        
        for blo in block:
            s.add(tuple(blo))
        
        while len(q) > 0:
            top = q[0]
            if top == b:
                return True
            
            q.pop(0)
            step += 1
            if step >= len(block) * len(block):
                break
            for p in di:
                r, c = top[0] + p[0], top[1] + p[1]
                if r < 0 or r >= 1000000 or c < 0 or c >= 1000000 or tuple([r, c]) in s or tuple([r, c]) in visit:
                    continue
                q.append([r, c])
                visit.add(tuple([r, c]))
        return step >= len(block) * len(block)
        
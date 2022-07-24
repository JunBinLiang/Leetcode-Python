import collections
di = [[1, 0],[-1, 0],[0, 1],[0, -1]]

class Solution:
    def numIslands(self, a: List[List[str]]) -> int:
        n = len(a)
        m = len(a[0])
        cnt = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == '0':
                    continue
                
                # do BFS
                cnt += 1
                q = deque([[i, j]])
                a[i][j] = '0'
                while len(q) > 0:
                    sz = len(q)
                    for x in range(sz):
                        pos = q.popleft()
                        r, c = pos[0], pos[1]
                        for p in di:
                            nxtr = r + p[0]
                            nxtc = c + p[1]
                            if nxtr < 0 or nxtr >= n or nxtc < 0 or nxtc >= m or a[nxtr][nxtc] == '0':
                                continue
                            q.append([nxtr, nxtc])
                            a[nxtr][nxtc] = '0'
        return cnt
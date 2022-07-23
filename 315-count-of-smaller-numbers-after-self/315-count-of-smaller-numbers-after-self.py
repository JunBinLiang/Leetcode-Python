# https://grantjenks.com/docs/sortedcontainers/sortedlist.html#sortedcontainers.SortedList.bisect_left
# SortedList
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, a: List[int]) -> List[int]:
        res = [0] * len(a)
        sl = SortedList()
        
        for i in range(len(a) - 1, -1, -1):
            idx = sl.bisect_left(a[i])
            res[i] = idx
            sl.add(a[i])
            
        return res
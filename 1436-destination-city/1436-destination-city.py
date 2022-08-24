class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        se = set()
        for e in paths:
            se.add(e[0])  
        for e in paths:
            if e[1] not in se:
                return e[1]
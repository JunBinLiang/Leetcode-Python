class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if ty > tx:
                ty %= tx
            else:
                tx %= ty
        
        if tx == sx:
            if ty >= sy:
                return (ty - sy) % tx == 0
        if ty == sy:
            if tx >= sx:
                return (tx - sx) % ty == 0
        return False
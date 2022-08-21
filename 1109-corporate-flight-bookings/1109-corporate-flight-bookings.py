class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    
        line = [0] * (n + 1)
        
        
        for interval in bookings:
            l = interval[0] - 1
            r = interval[1] - 1
            w = interval[2]
            line[l] += w
            line[r + 1] -= w
           
        res = []
        tot = 0
        for i in range(len(line) - 1):
            tot += line[i]
            res.append(tot)    
        return res
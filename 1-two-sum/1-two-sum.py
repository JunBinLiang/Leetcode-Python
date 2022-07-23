class Solution:
    def twoSum(self, a: List[int], t: int) -> List[int]:
        f = {}
        for i in range(len(a)):
            if t - a[i] in f.keys():
                return [i, f[t - a[i]]]
            f[a[i]] = i
        return []
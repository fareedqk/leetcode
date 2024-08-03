class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # return Counter(target) == Counter(arr)
        res = [0] * 1001
        count = 0

        for t, c in zip(target, arr):
            if res[t] == 0:
                count += 1
            res[t] += 1
            if res[c] == 1:
                count -= 1
            res[c] -= 1

        return count == 0
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # i = 0
        # for num in arr:
        #     if num % 2 != 0:
        #         i += 1
        #         if i > 2:
        #             return True
        #     else: 
        #         i = 0
        # return False
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                return True
        return False
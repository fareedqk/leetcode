class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    # mul *= 10
        mul = 1
        sum = 0
        for i in digits[::-1]:
            ans = i * mul
            # print(i)
            mul *= 10
            # print(mul)
            # sum += i
            sum = sum + ans
            # print(sum)
        plus_one = sum+1
        # res = [int(res) for res in str(plus_one)]
        res = [int(res) for res in str(plus_one)]
        return res

        
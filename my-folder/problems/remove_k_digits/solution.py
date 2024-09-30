class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while stack and k > 0 and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        while k:
            k = k - 1
            stack.pop()

        if ''.join(stack).lstrip('0'):
            return ''.join(stack).lstrip('0') # remove leading zeros 
        return '0' # handle edge cases
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        length = len(s[-1])
        return length
        
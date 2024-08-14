class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        for i in range(len(s)):
            return len(s[-1])
        
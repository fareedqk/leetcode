class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for i in range(len(s)):
            dict[s[i]] = 1 + dict.get(s[i], 0)
        
        for idx, val in enumerate(s):
            if dict[val] == 1:
                return idx
        return -1

        
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        j = 0
        n = len(spaces)
        for i in range(len(s)):
            if j < n and i == spaces[j]:
                result.append(' ')
                j += 1
            result.append(s[i])
        return "".join(result)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}

        for i in magazine:
            dic[i] = dic.get(i, 0) + 1

        for j in ransomNote:
            if j not in dic or dic[j] <= 0:
                return False
            dic[j] -= 1

        return True
            
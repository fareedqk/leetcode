class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i, word in enumerate(words):
            if word[0] != s[i][0]:
                return False
        return True
        
        
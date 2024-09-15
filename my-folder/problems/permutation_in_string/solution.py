class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lenS1, lenS2 = len(s1), len(s2)
        if lenS1 > lenS2: return False

        charS1 = [0] * 26
        charS2 = [0] * 26

        for x in range(lenS1):
            charS1[ord(s1[x]) - ord('a')] += 1
            charS2[ord(s2[x]) - ord('a')] += 1
        
        for x in range(lenS1, lenS2):
            if charS1 == charS2: return True

            charS2[ord(s2[x]) - ord('a')] += 1
            charS2[ord(s2[x - lenS1]) - ord('a')] -= 1
        
        return charS1 == charS2
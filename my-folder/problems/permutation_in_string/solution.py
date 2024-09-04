class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        charS1 = [0] * 26
        charS2 = [0] * 26

        for i in range(len(s1)):
            charS1[ord(s1[i]) - ord('a')] += 1
            charS2[ord(s2[i]) - ord('a')] += 1

        for i in range(len(s1), len(s2)):
            if charS1 == charS2: return True

            charS2[ord(s2[i]) - ord('a')] += 1
            charS2[ord(s2[i - len(s1)]) - ord('a')] -= 1

        return charS1 == charS2
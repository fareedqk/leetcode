class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_s, dict_t = {}, {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if (c1 in dict_s and dict_s[c1] != c2) or (c2 in dict_t and dict_t[c2] != c1):
                return False

            dict_s[c1] = c2
            dict_t[c2] = c1
        return True
        
        
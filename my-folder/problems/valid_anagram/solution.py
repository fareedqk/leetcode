class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
    
        count_s, count_t = {}, {}

        # creating hash maps
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        # checking if the keys and values are same
        # for c in count_s:
        return count_s == count_t
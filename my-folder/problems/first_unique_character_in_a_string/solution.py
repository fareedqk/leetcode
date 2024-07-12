class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = {}
        for i in range(len(s)):
            if s[i] in hash_map:
                hash_map[s[i]] += 1
            else:
                hash_map[s[i]] = 1
        

        for key, val in hash_map.items():
            if val == 1:
                return s.index(key)
        return -1
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        dict_pattern = {}
        dict_words = {}
        
        for p, w in zip(pattern, words):
            if p in dict_pattern and dict_pattern[p] != w:
                return False
            if w in dict_words and dict_words[w] != p:
                return False
            dict_pattern[p] = w
            dict_words[w] = p
        return True

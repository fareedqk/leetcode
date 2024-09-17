class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1, s2 = s1.split(), s2.split()
        hash_map = {}
        result = []
        for word in s1 + s2:
            hash_map[word] = hash_map.get(word, 0) + 1
            print(hash_map)
        
        for i in hash_map:
            if hash_map[i] == 1:
                result.append(i)
        return result
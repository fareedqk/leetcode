class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)

        # for word in strs:
        #     sorted_word = "".join(sorted(word))
        #     res[sorted_word].append(word)

        # return res.values()
        res = {}
        for s in strs:
            f = str(sorted(s))
            if f not in res:
                res[f] = []
            res[f].append(s)
        
        return list(res.values())
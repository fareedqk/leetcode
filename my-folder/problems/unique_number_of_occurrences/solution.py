class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}
        for i in arr:
            dic[i] = dic.get(i, 0) + 1
            # if i in dic:
            #     dic[i] += 1
            # else:
            #     dic[i] = 1
        
        return len(set(dic.values())) == len(dic.values())
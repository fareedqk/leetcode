class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurences = []
        for i, num in enumerate(nums):
            if num == x:
                occurences.append(i)
        result = []
        for query in queries:
            if query <= len(occurences):
                result.append(occurences[query - 1])
            else:
                result.append(-1)
        return result
        
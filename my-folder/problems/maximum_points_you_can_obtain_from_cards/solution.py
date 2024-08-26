class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum, right_sum = sum(cardPoints[:k]), 0
        max_score = left_sum

        last = len(cardPoints)-1
        for i in range(k):
            left_sum -= cardPoints[k-1-i]
            right_sum += cardPoints[last-i]
            max_score = max(max_score, left_sum + right_sum)
        return max_score
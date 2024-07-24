class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)

        q = deque(range(len(deck)))
        for c in deck:
            i = q.popleft()
            res[i] = c

            if q:
                q.append(q.popleft()) # pop and shift it to the end of queue
        return res
        
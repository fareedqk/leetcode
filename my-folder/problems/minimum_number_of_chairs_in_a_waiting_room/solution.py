class Solution:
    def minimumChairs(self, s: str) -> int:
        chairs = 0
        people = 0

        for i in s:
            if i == 'E':
                people += 1
                if chairs < people:
                    chairs += 1

            elif i == 'L':
                people -= 1
            else: 
                None
        return chairs
        
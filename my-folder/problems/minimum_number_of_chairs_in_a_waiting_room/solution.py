class Solution:
    def minimumChairs(self, s: str) -> int:
        # waiting room
        person = 0
        chairs = 0
        for i in s:
            if i == "E":
                person += 1
                if chairs < person:
                    chairs += 1
            elif i == "L":
                person -= 1

        return chairs
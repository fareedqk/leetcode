class Solution:
    def minimumChairs(self, s: str) -> int:
        person, chairs = 0, 0
        
        for i in s:
            if i == 'E':
                person += 1
                # condition --> when we will need chairs?
                if chairs < person:
                    chairs += 1
            elif i == 'L':
                person -= 1
        return chairs

        
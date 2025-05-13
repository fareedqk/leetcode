class Solution:
    def diStringMatch(self, string: str) -> List[int]:
        s, l = 0, len(string)
        result = []
        for c in string:
            if c == "I":
                result.append(s)
                s += 1
            else:
                result.append(l)
                l -= 1
        result.append(s)
        return result

        
        
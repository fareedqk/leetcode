class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_str = s * 2
        new_str = new_str[1:-1]
        if s in new_str:
            return True 
        else: 
            return False
        
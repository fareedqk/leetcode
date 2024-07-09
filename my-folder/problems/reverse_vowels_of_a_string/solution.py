class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s) # convert s string into a list to make it mutable

        left, right = 0, len(s)-1 # first, end
        
        while left < right:
            if s[left] in vowels: # checking left pointer
                while s[right] not in vowels: # checking right pointer
                    right -= 1 
                s[left], s[right] = s[right], s[left]
                right -= 1
            left += 1
        return "".join(s) # converting from list to string 

        
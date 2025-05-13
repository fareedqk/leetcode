class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        result = set()
        for word in words:
            transformation = ""
            for char in word:
                transformation += morse[ord(char) - ord('a')] # ord('a') = 97
            result.add(transformation)
        return len(result)
        
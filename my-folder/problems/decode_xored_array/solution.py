class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for i in range(len(encoded)):
            next_element = encoded[i] ^ arr[i]
            arr.append(next_element)
    
        return arr
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element_count = Counter(nums)
        
        majority_elements = []
        size = len(nums) // 3
    
        for element, count in element_count.items():
            if count > size:
                majority_elements.append(element)
        
        return majority_elements
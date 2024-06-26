class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        new_string = s.upper().replace('-', '')[::-1]
        group = []
        for i in range(0, len(new_string), k):
            group.append(new_string[i:i+k])
        
        return '-'.join(group)[::-1]
            
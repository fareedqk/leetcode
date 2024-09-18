class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        nums=[0]*len(s)
        left=-1
        right=-1

        for i in range(len(s)):
            if s[i]==c:
                left=i
                right=i
                break
        
        for i in range(len(s)):
            if s[i]==c and left!=i:
                right=i
                break

        for i in range(len(s)):
            if i==right:
                left=right
                for j in range(right+1,len(s)):
                    if s[j]==c:
                        right=j
                        break
            
            nums[i]=min(abs(i-left),abs(i-right))
        return nums
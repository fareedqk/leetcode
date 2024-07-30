class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack =[]
        count=0
        # stck.append(s[0])
        for i in s:
            if stack and (stack[-1]=='b' and i == 'a'):
                stack.pop()
                count += 1
            else:
                stack.append(i)
        return count


        
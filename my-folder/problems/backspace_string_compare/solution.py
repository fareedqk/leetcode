class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for i in s:
            if len(s_stack) != 0:
                if i == '#':
                    s_stack.pop()
                    continue
            elif i == '#':
                continue
            s_stack.append(i)
        for j in t:
            if len(t_stack) != 0:
                if j == '#':
                    t_stack.pop()
                    continue                
            elif j == '#':
                continue
            t_stack.append(j)

        return s_stack == t_stack

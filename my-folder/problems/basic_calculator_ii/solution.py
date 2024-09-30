class Solution:
    def calculate(self, s: str) -> int:
        num, prev_op, stack=0, '+', []
        for c in s+'+':
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if prev_op=='+':
                    stack.append(num)
                elif prev_op == '-':
                    stack.append(-num)
                elif prev_op == '*':
                    stack.append(stack.pop()*num)
                elif prev_op == '/':
                    stack.append(math.trunc(stack.pop()/num))
                prev_op=c
                num=0             
        return sum(stack)
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                decoded_str = ""
                while stack and stack[-1] != '[':
                    decoded_str = stack.pop() + decoded_str
                stack.pop() # discard "["
            
                no = ""
                while stack and stack[-1].isdigit():
                    no = stack.pop() + no
                stack.append(decoded_str * int(no))

        return "".join(stack)
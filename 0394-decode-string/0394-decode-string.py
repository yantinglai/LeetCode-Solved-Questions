class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        temp = ""
 
        for c in s:
            if c == "]":
                inner_str = ""
                multiplier = ""
                while stack[-1] != "[":
                    inner_str = stack.pop() + inner_str
                stack.pop()
                while stack and stack[-1].isdigit():
                    multiplier = stack.pop() + multiplier 
                stack.append(int(multiplier) * inner_str)
                continue
      
            else:
                stack.append(c)
        return "".join(stack)
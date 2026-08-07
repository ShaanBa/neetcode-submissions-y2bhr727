class Solution:
    def isValid(self, s: str) -> bool:
        brace_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []

        for char in s:
            if char in brace_map.values():
                stack.append(char)
            elif stack: 
                if stack[-1] == brace_map[char]:
                    stack.pop(-1)
                else:
                    return False
            else:
                return False
        return len(stack) == 0
                
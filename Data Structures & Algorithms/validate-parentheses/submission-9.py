class Solution:
    def isValid(self, s: str) -> bool:
        brace_map = {
            '(': ")",
            '{': '}',
            '[': ']'
        }

        stack = []

        if len(s) == 1:
            return False
        for i in range(len(s)):
            if s[i] in brace_map.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if s[i] == brace_map.get(stack[-1]):
                    stack.pop(-1)
                else:
                    return False
        return len(stack) == 0


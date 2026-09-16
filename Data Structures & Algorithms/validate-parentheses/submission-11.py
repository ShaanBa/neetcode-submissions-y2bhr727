class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brace_map = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        for i in range(len(s)):
            if s[i] in brace_map.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                if brace_map[stack[-1]] == s[i]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
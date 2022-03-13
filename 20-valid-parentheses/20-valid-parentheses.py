class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(':')', '{':'}', '[':']'}
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif stack and d[stack[-1]] == ch:
                stack.pop()
            else:
                return False
        return stack == []
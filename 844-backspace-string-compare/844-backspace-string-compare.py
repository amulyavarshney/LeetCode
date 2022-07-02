class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1, stack2 = [], []
        for x in s:
            if x != '#':
                stack1.append(x)
            elif stack1:
                stack1.pop()
        for x in t:
            if x != '#':
                stack2.append(x)
            elif stack2:
                stack2.pop()
        return stack1 == stack2
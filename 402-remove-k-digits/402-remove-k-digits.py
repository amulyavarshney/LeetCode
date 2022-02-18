class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        stack = []
        for i in range(n):
            while stack and int(stack[-1])>int(num[i]) and k>0:
                stack.pop()
                k -= 1
            stack.append(num[i])
        if k>0:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
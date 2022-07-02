class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        c = ''
        for x in s:
            if x.isdigit():
                c += x
            elif x == '[':
                stack.append(c)
                stack.append(x)
                c = ''
            elif x == ']':
                z = ''
                while stack[-1] != '[':
                    z = stack.pop() + z
                stack.pop()
                y = int(stack.pop())
                stack.append(z*y)
            else:
                stack.append(x)
        return ''.join(stack)
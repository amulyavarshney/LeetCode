class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_s, cur_n = '', 0
        for x in s:
            if x == '[':
                stack.append(cur_s)
                stack.append(cur_n)
                cur_s = ''
                cur_n = 0
            elif x == ']':
                prev_n = stack.pop()
                prev_s = stack.pop()
                cur_s = prev_s + cur_s*prev_n
            elif x.isdigit():
                cur_n = cur_n*10 + int(x)
            else:
                cur_s = cur_s + x
        return cur_s
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-/*':
                prev1 = stack.pop()
                prev2 = stack.pop()
                stack.append(str(int(eval(prev2+token+prev1))))
            else:
                stack.append(token)
        return stack[0]
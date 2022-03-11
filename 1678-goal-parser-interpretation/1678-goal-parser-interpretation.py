class Solution:
    def interpret(self, command: str) -> str:
        s, ans = '', []
        for x in command+'':
            s += x
            if s == 'G':
                ans.append('G')
                s = ''
            elif s == '()':
                ans.append('o')
                s = ''
            elif s == '(al)':
                ans.append('al')
                s = ''
        return ''.join(ans)
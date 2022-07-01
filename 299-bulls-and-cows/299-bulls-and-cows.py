class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d = {}
        bull, cow = 0, 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bull += 1
            else:
                d[secret[i]] = d.get(secret[i], 0) + 1
        for i in range(len(secret)):
            if guess[i] != secret[i] and d.get(guess[i], 0) > 0:
                cow += 1
                d[guess[i]] -= 1
        return f"{bull}A{cow}B"
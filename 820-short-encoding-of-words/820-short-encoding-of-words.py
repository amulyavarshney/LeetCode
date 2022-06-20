class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        c, s = 0, set()
        words.sort(key=len, reverse=True)
        for word in words:
            for x in s:
                if word == x[-len(word):]:
                    break
            else:
                s.add(word)
                c += len(word)+1
        return c
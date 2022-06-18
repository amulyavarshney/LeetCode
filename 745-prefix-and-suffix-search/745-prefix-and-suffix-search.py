class WordFilter:

    def __init__(self, words: List[str]):
        self.d = {}
        for i in range(len(words)):
            word = words[i]
            for j in range(len(word)):
                for k in range(len(word)):
                    self.d[word[:j+1]+'.'+word[k:]] = i
                
    def f(self, prefix: str, suffix: str) -> int:
        return self.d.get(prefix+'.'+suffix, -1)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
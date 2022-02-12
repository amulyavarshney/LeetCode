class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = collections.defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                mask = word[:i]+'*'+word[i+1:]
                d[mask].add(word)
        q = collections.deque([(beginWord, 1)])
        vis = set()
        while q:
            word, level = q.popleft()
            vis.add(word)
            if word == endWord:
                return level
            for i in range(len(word)):
                mask = word[:i]+'*'+word[i+1:]
                for w in d[mask]:
                    if w not in vis:
                        q.append((w, level+1))
        return 0
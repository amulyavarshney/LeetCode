class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        s = set()
        for word in words:
            morse = []
            for ch in word:
                morse.append(d[ord(ch)-97])
            s.add(''.join(morse))
        return len(s)
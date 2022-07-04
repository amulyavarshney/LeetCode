class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        d = collections.defaultdict(list)
        for p in products:
            for i in range(1, len(p)+1):
                d[p[:i]].append(p)
        ans = []
        for i in range(1, len(searchWord)+1):
            d[searchWord[:i]].sort()
            ans.append(d[searchWord[:i]][:3])
        return ans
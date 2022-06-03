class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = collections.defaultdict(set)
        for u,v in connections:
            adj[u].add(v)
            adj[v].add(u)
        vis = [False]*n
        intime = [0]*n
        low = [0]*n
        time = 0
        ans = []
        def dfs(u, p):
            nonlocal time, ans
            time += 1
            intime[u] = low[u] = time
            vis[u] = True
            for v in adj[u]:
                if v == p: # parent
                    continue
                elif vis[v] == True: # backedge
                    low[u] = min(low[u], intime[v])
                else: # forward edge
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] > intime[u]:
                        ans.append([u, v])
        dfs(0, -1)
        return ans
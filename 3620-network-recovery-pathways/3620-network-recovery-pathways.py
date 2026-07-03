class Solution:
    def check(self, mid, adj, topo, online, k, n):

        dist = [inf] * n
        dist[0] = 0

        for u in topo:

            if dist[u] == inf:
                continue

            if u != 0 and u != n - 1 and not online[u]:
                continue

            for v, w in adj[u]:

                if w < mid:
                    continue

                if v != n - 1 and not online[v]:
                    continue

                dist[v] = min(dist[v], dist[u] + w)

        return dist[n - 1] <= k

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        max_edge = 0

        for u, v, w in edges:
            adj[u].append((v, w))
            indegree[v] += 1
            max_edge = max(max_edge, w)

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo = []

        while q:
            u = q.popleft()
            topo.append(u)

            for v, _ in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        low, high = 0, max_edge
        ans = -1

        while low <= high:

            mid = (low + high) // 2

            if self.check(mid, adj, topo, online, k, n):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans  
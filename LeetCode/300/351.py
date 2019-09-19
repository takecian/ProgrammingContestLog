class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = {}

        skip[(1, 7)] = 4
        skip[(1, 3)] = 2
        skip[(1, 9)] = 5
        skip[(2, 8)] = 5
        skip[(3, 7)] = 5
        skip[(3, 9)] = 6
        skip[(4, 6)] = 5
        skip[(7, 9)] = 8
        ans = 0

        def bfs(used, last):
            nonlocal ans
            if len(used) >= m:
                ans += 1
            if len(used) == n:
                return
            for j in range(1, 10):
                if j not in used:  # if j is not used
                    # Sort the vertices of the edge to search in skip
                    edge = (min(last, j), max(last, j))
                    if edge not in skip or skip[edge] in used:
                        bfs(used + [j], j)

        for i in range(1, 10):
            bfs([i], i)
        return ans

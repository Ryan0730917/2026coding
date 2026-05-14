#week12-4.py leetcode 1466
from collections import defaultdict
from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        path = defaultdict(list)

        for a, b in connections:
            path[a].append((b, +1))   # 原本方向 a -> b
            path[b].append((a, -1))   # 反向邊

        def helper(now):
            ans = 0
            visited.add(now)

            for k, d in path[now]:
                if k not in visited:
                    if d == +1:
                        ans += 1
                    ans += helper(k)

            return ans

        return helper(0)

# Time Complexity: O(N*M)
# Space Complexity: O(N)

class Solution:
    def countGoodSubsequences(self, s: str) -> int:
        dict1 = collections.Counter(s)

        m, total = max(dict1.values()), 0

        @lru_cache(1000)
        def dfs(n, k):
            return 1 if not k else dfs(n, k - 1) * (n - k + 1) // k

        for k in range(1, m + 1):
            product = 1

            for i in dict1.values():
                product *= (1 + dfs(i, k))

            total += product - 1

        return total % (10**9 + 7)
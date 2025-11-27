class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # counts how many times each node appears
        counter = defaultdict(int)
        n = len(edges)

        ''' the middle node will have the highest outgoing value '''

        # Loop through edges and increment the count for both endpoints.
        for a, b in edges:
            counter[a] += 1
            counter[b] += 1

        # find the node whose count is the number of edges.
        for node, freq in counter.items():
            if freq == n:
                return node
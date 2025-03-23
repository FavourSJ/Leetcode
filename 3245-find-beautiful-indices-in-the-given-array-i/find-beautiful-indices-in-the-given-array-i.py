class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # find all occurences of a in s
        a_indices = [i for i in range(len(s) - len(a) + 1) if s[i:i + len(a)] == a]

        # find all occurences of b in s
        b_indices = [j for j in range(len(s) - len(b) + 1) if s[j:j + len(b)] == b]

        result = []
        # pointer for b_indices
        j = 0 

        # Iterate over each index `i` where `a` appears
        for i in a_indices:
            # Move `j` to the first `b` index that is within `k` distance
            while j < len(b_indices) and b_indices[j] < i - k:
                j += 1

            # Check if `b_indices[j]` is within range of `k`
            if j < len(b_indices) and abs(b_indices[j] - i) <= k:
                # Append `i` to result if it meets the condition
                result.append(i)
        return result
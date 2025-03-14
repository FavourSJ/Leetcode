class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_count = Counter(stones)
        jewel_count = 0

        for stone in stone_count:
            if stone in jewels:
                jewel_count += stone_count[stone]
        return jewel_count
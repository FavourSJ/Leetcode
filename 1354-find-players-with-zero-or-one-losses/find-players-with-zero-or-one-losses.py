# Time complexity: O(n + mlogm)

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = defaultdict(int) # Dictionary to track losses per player
        players = set() # Set to track all players (both winners & losers)

        for winner, loser in matches:
            players.add(winner) # Add winner to set
            players.add(loser) # Add loser to set
            loss_count[loser] += 1 # Increment loss count for the loser

        # Players who have not lost any matches
        no_losses = sorted([player for player in players if loss_count[player] == 0])

        # Players who have lost exactly one match
        one_loss = sorted([player for player in players if loss_count[player] == 1])

        return [no_losses, one_loss]
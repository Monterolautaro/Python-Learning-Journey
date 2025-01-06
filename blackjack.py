# 7. 🌶️ (Optional)
"""
In this problem we'll be working with a simplified version of blackjack (aka twenty-one). 
In this version there is one player (who you'll control) and a dealer. Play proceeds as follows:

1) The player is dealt two face-up cards. The dealer is dealt one face-up card.

2) The player may ask to be dealt another card ('hit') as many times as they wish.
 If the sum of their cards exceeds 21, they lose the round immediately.

3) The dealer then deals additional cards to himself until either:
a - the sum of the dealer's cards exceeds 21, in which case the player wins the round

b - the sum of the dealer's cards is greater than or equal to 17. If the player's total is greater than the dealer's,
    the player wins. Otherwise, the dealer wins (even in case of a tie).

When calculating the sum of cards, Jack, Queen, and King count for 10.
Aces can count as 1 or 11 (when referring to a player's "total" above,
we mean the largest total that can be made without exceeding 21. So e.g. A+8 = 19, A+8+8 = 17)   


For this problem, you'll write a function representing the player's decision-making strategy in this game.
 We've provided a very unintelligent implementation below:
"""


def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay.
    When calculating a hand's total value, we count aces as "high" (with value 11) if doing so
    doesn't bring the total above 21, otherwise we count them as low (with value 1). 
    For example, if the player's hand is {A, A, A, 7}, we will count it as 11 + 1 + 1 + 7,
    and therefore set player_total=20, player_low_aces=2, player_high_aces=1.
    """
    low = player_low_aces
    high = player_high_aces

    if player_total < 14:
        return True

    if(player_total + high):
        return False

# This very conservative agent always sticks with the hand of two cards that they're dealt.

# We'll be simulating games between your player agent and our own dealer agent by calling your function.

# Try running the function below to see an example of a simulated game:

# q7.simulate_one_game()
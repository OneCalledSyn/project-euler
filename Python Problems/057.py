from collections import Counter

# Define card values, mapping each rank to its numerical value
values = {r: i for i, r in enumerate('23456789TJQKA', start=2)}

# Define all possible straights, including the Ace-low straight as (5,4,3,2,1)
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(5, 4, 3, 2, 1)]

# Define ranks based on frequency of card values
# The index represents the hand type's strength
# 0: High card, 1: One Pair, 2: Two Pairs, 3: Three of a Kind,
# 4: Straight, 5: Flush, 6: Full House, 7: Four of a Kind
ranks = [
    (1, 1, 1, 1, 1),    # High card
    (2, 1, 1, 1),       # One Pair
    (2, 2, 1),          # Two Pairs
    (3, 1, 1),          # Three of a Kind
    (),                  # Straight (handled separately)
    (),                  # Flush (handled separately)
    (3, 2),             # Full House
    (4, 1)              # Four of a Kind
]

def hand_rank(hand):
    # Count the frequency of each card value
    counts = Counter(card[0] for card in hand)
    
    # Sort the counts first by frequency descending, then by card value descending
    sorted_counts = sorted(((v, values[k]) for k, v in counts.items()), reverse=True)
    
    # Zip the sorted counts to separate frequencies and values
    score = list(zip(*sorted_counts))
    
    # Determine the rank based on the frequency pattern
    try:
        score[0] = ranks.index(score[0])
    except ValueError:
        score[0] = 0  # Default to High card if not found
    
    # Check for Flush (all cards have the same suit)
    if len(set(card[1] for card in hand)) == 1:
        score[0] = 5  # Flush rank
    
    # Current straight sequence
    current_straight = tuple(score[1])
    
    # Handle Ace-low straight by adjusting card values
    if current_straight == (14, 5, 4, 3, 2):
        score[1] = (5, 4, 3, 2, 1)
        current_straight = (5, 4, 3, 2, 1)
    
    # Check for Straight or Straight Flush
    if current_straight in straights:
        score[0] = 8 if score[0] == 5 else 4  # 8: Straight Flush, 4: Straight
    
    return score

for _ in range(int(input())):
    hand = input().split()
    player1, player2 = hand[:5], hand[5:]
    print("Player 1" if hand_rank(player1) > hand_rank(player2) else "Player 2")
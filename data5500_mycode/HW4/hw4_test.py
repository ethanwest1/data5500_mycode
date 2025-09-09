# Ethan Westenskow

from DeckOfCards import *

# ---- Step 2: Scoring helpers ----
def score_hand(hand_cards):
    # Counters to track hand total and number of aces
    total = 0
    ace_count = 0
    for card in hand_cards:
        total += card.val
        if card.face == 'Ace':  
            ace_count += 1

    # Ace Handling
    while total > 21 and ace_count > 0: 
        total -= 10
        ace_count -= 1

    return total 


def is_bust(total):
    bust = False
    if total > 21:
        bust = True
    return bust


# ---- Temporary test harness ----
# Build some test hands manually using Card(suit, face, value)
test_hands = {
    "Ace + 9": [Card("Spades", "Ace", 11), Card("Diamonds", "9", 9)],  # expect 20
    "Ace + 9 + Ace": [Card("Spades", "Ace", 11), Card("Diamonds", "9", 9), Card("Hearts", "Ace", 11)],  # expect 21
    "Ace + 9 + 5": [Card("Spades", "Ace", 11), Card("Diamonds", "9", 9), Card("Clubs", "5", 5)],  # expect 15
    "Q + K": [Card("Hearts", "Queen", 10), Card("Clubs", "King", 10)],  # expect 20
    "8 + 8 + 5": [Card("Diamonds", "8", 8), Card("Spades", "8", 8), Card("Hearts", "5", 5)],  # expect 21
    "Ace + Ace + 9": [Card("Diamonds", "Ace", 11), Card("Clubs", "Ace", 11), Card("Hearts", "9", 9)],  # expect 21
    "9 + 9 + 9": [Card("Spades", "9", 9), Card("Diamonds", "9", 9), Card("Hearts", "9", 9)],  # expect 27, bust
}

print("\n---- Running Score Tests ----")
for name, hand in test_hands.items():
    total = score_hand(hand)
    print(f"{name}: {total} (Bust? {is_bust(total)})")


# ---- Main game (unchanged for now) ----
def main():
    # Welcome Message
    print("\nWelcome to Blackjack! I hope you're feeling lucky!\n")

    # Creating the deck of cards
    deck = DeckOfCards()

    # Print Deck (Unshuffled & Shuffled)
    print("Deck before shuffled:")
    deck.print_deck()
    deck.shuffle_deck()
    print("\nDeck After Shuffled:")
    deck.print_deck()

    # Deal 2 cards to the user + print the cards. 
    card1 = deck.get_card()
    card2 = deck.get_card()
    
    print(f"\nCard 1 is: {card1}")
    print(f"Card 2 is: {card2}")

    # Calculate + print the score of the user's hand
    score = 0
    score += card1.val
    score += card2.val

    print(f"Your score is: {score}")

    # User Gameplay (hit or not)
    hit = input("\nWould you like to hit? (y/n) ")


main()
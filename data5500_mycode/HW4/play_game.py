# Ethan Westenskow

from DeckOfCards import *

#Score hand helper
def score_hand(hand_cards):
    #Counters to track hand total and num of aces
    total = 0
    ace_count = 0
    for card in hand_cards:
        total += card.val
        if card.face == 'Ace': ###### I'M NOT SURE IF CARD.FACE is the correct reference. 
            ace_count += 1


def is_bust():
    return



#Main function to play the game. Contains: welcome, dealing to the user, gameplay
def main():
    #Welcome Message
    print("\nWelcome to Blackjack! I hope you're feeling lucky!\n")

    #Creating the deck of cards
    deck = DeckOfCards()

    #Print Deck (Unshuffled & Shuffled)
    print("Deck before shuffled:")
    deck.print_deck()
    deck.shuffle_deck()
    print("\nDeck After Shuffled:")
    deck.print_deck()

    #Deal 2 cards to the user + print the cards. 
    card1 = deck.get_card()
    card2 = deck.get_card()
    
    print(f"\nCard 1 is: {card1}")
    print(f"Card 2 is: {card2}")

    #Calculate + print the score of the user's hand
    score = 0
    score += card1.val
    score += card2.val

    print(f"Your score is: {score}")

    #User Gameplay (hit or not)
    hit = input("\nWould you like to hit? (y/n) ")

main()



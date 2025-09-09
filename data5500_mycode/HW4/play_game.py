# Ethan Westenskow

from DeckOfCards import *

#Score hand helper
def score_hand(hand_cards):
    #Counters to track hand total and num of aces
    total = 0
    ace_count = 0
    for card in hand_cards:
        total += card.val
        if card.face == 'Ace':  
            ace_count += 1
    #Ace Handling
    while total > 21 and ace_count > 0: 
        total -= 10
        ace_count -= 1
    return total 

#Did the player bust? 
def is_bust(total):
    bust = False
    if total > 21:
        bust = True
    return bust

#We can call on this function to more easily print/format the cards. (CHATGPT)
def card_string(card):
    """Return 'Face of Suit' for display (without value)."""
    return f"{card.face} of {card.suit}"

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

    #Establishing player & dealer hand for gameplay
    player_hand = []
    dealer_hand = []

    #Deal 2 cards to the dealer + append to dealer_hand.
    dealer_hand.append(deck.get_card())
    dealer_hand.append(deck.get_card())

    #Deal 2 cards to the user + append the cards to player_hand + print the user's hand
    player_hand.append(deck.get_card())
    player_hand.append(deck.get_card())

    #Scores the player's hand.
    player_total = score_hand(player_hand)

    #Prints the player's starting deck.
    print(f"\nCard number 1 is: {card_string(player_hand[0])}")
    print(f"Card number 2 is: {card_string(player_hand[1])}")
    print(f"Your total score is: {player_total}")


    #User Gameplay (hit or not)
    #See if player busted
    busted = is_bust(player_total)
    while not busted:
            hit = input("\nWould you like to hit? (y/n) ").lower()
            if hit == 'y':
                player_hand.append(deck.get_card())
                player_total = score_hand(player_hand)
                print(f"Card number {len(player_hand)} is: {card_string(player_hand[-1])}")
                print(f"Your total score is: {player_total}")
                busted = is_bust(player_total) #Updates and sees if you bust after each hit
                if busted == True:
                    print("You busted, you lose!")
                    break
            elif hit == 'n':
                break
            else:
                print("Please enter a valid input: (y/n) ")


main()

##### YOU JUST FINISHED THE HIT LOOP LOGIC. NOW YOU NEED TO DO THE DEALER REVEAL AND DEALER TURN. ####


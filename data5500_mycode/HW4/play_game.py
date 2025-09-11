# Ethan Westenskow
# ChatGPT Conversation: https://chatgpt.com/share/68c2f44d-5578-800b-b007-6c9701159666

from DeckOfCards import *

#Score hand helper
def score_hand(hand_cards):
    #Counters to track hand total and num of aces for the ace handling below. 
    total = 0
    ace_count = 0
    for card in hand_cards:
        total += card.val
        if card.face == 'Ace':  
            ace_count += 1
    #Ace Handling- if the total is less than 21 it treats the ace as a 10, but if the score is over 21 then it treats it as a 1. 
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

#We can call on this function to more easily print/format the cards.
def card_string(card):
    """Return 'Face of Suit' for display (without value)."""
    return f"{card.face} of {card.suit}"

#Main function to play the game. Contains: welcome, dealing to the user, gameplay
def main():
    #Creating the deck of cards
    deck = DeckOfCards()
    #Establishing the loop that will let us play again, if desired. 
    play_again = 'y'
    while play_again == 'y': 
        #Welcome Message
        print("\nWelcome to Black Jack! I hope you're feeling lucky!\n")

        #Print Deck (Unshuffled & Shuffled)
        print("Deck before shuffled:")
        deck.print_deck()
        deck.shuffle_deck()
        print("\nDeck After Shuffled:")
        deck.print_deck()

        #Establishing player & dealer hand for gameplay. This is used to calculate the total of the hand using score_hand()
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
        player_busted = is_bust(player_total) 
        while not player_busted:  
                hit = input("\nWould you like to hit? (y/n) ").lower()
                if hit == 'y':
                    player_hand.append(deck.get_card())
                    player_total = score_hand(player_hand)
                    print(f"Card number {len(player_hand)} is: {card_string(player_hand[-1])}")
                    print(f"Your total score is: {player_total}")
                    player_busted = is_bust(player_total) #Updates and sees if you bust after each hit
                    if player_busted == True:
                        print("You busted, you lose!")
                        break
                elif hit == 'n':
                    break
                else:
                    print("Please enter a valid input:(y/n) ")
        
        #Dealers gameplay
        if not player_busted: #The dealer only does this if the player doesn't bust, if the player busts, this portion isn't important.
            print(f"\nDealer card number 1 is: {card_string(dealer_hand[0])}")
            print(f"Dealer card number 2 is: {card_string(dealer_hand[1])}")

            dealer_total = score_hand(dealer_hand)
            print(f"Dealer's score is: {dealer_total}")

            # The dealer will hit if their hand total is less than 17. This loop will deal a card, append it to their hand, and compute the score.
            while dealer_total < 17:
                dealer_hand.append(deck.get_card())
                print(f"Dealer hits, card number {len(dealer_hand)} is: {card_string(dealer_hand[-1])}")
                dealer_total = score_hand(dealer_hand)
                print(f"Dealer score is: {dealer_total}\n")
        
            #Decide Winner
            dealer_busted = is_bust(dealer_total)
            if dealer_busted:
                print("Dealer busted, you win!!")
            elif player_total > dealer_total and player_total <= 21:
                print("Your score is higher, you win!")
            elif dealer_total >= player_total and player_total <= 21:
                if dealer_total == player_total:
                    print("Dealer score is equal, you lose!")
                elif dealer_total > player_total:
                    print("Dealer score is higher, you lose!")

        #This determines if we play again or not.            
        play_again = input("\n:Would you like to play again?(y/n): ").lower()
        while play_again not in ('y', 'n'): #Chatgpt taught me this simpler method for data validation. As long as the user input isnt' 'y' or 'n' it will re-prompt the user for a valid input. 
            play_again = input("Please enter y or n: ").lower()

        if play_again == 'n':
            print("\nThanks for playing!")


main()



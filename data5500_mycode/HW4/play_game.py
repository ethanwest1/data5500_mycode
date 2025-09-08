# Ethan Westenskow

from DeckOfCards import *

def welcome():
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

welcome()

def 
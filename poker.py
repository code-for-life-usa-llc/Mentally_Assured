import random
# cards
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
def create_deck():
    deck = []
    for r in ranks:
        for s in suits:
            card = r + " of " + s
            deck.append(card)
    return deck
def shuffle_deck(deck):
    random.shuffle(deck)
def deal_cards(deck, num):
    hand = []
    for i in range(num):
        card = deck.pop()
        hand.append(card)
    return hand
def get_hand_value(hand):
    values = []
    for card in hand:
        # split "10 of Hearts" -> "10"
        rank = card.split(" ")[0]
        values.append(ranks.index(rank))
    values.sort(reverse=True)
    return values
def play_poker():
    print("Welcome to Poker!")
    deck = create_deck()
    shuffle_deck(deck)
    player_hand = deal_cards(deck, 5)
    computer_hand = deal_cards(deck, 5)
    print("\nYour hand is:")
    for c in player_hand:
        print(c)
    input("\nPress Enter to see the computer's hand...")
    print("Computer's hand is:")
    for c in computer_hand:
        print(c)
    player_value = get_hand_value(player_hand)
    computer_value = get_hand_value(computer_hand)
    if player_value > computer_value:
        print("\nYou win!")
    elif player_value < computer_value:
        print("\nComputer wins!")
    else:
        print("\nIt is a tie!")
play_poker()
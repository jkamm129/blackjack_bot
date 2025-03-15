import random
import time

# Define the deck with multiple decks for realistic blackjack
NUM_DECKS = 6
DECK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4 * NUM_DECKS

def shuffle_deck():
    global deck2, running_count
    deck2 = DECK.copy()
    random.shuffle(deck2)
    # Start 1/3 of the way through the deck to generate an effective running count
    removed_cards = deck2[:len(deck2) // 3]
    deck2 = deck2[len(deck2) // 3:]
    running_count = sum(1 if card in ['2', '3', '4', '5', '6'] else -1 if card in ['10', 'J', 'Q', 'K', 'A'] else 0 for card in removed_cards)

shuffle_deck()

def calculate_value(cards):
    value = 0
    aces = 0
    for card in cards:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A':
            aces += 1
            value += 11  # Initially count Ace as 11
        else:
            value += int(card)
    
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value

def update_count(card, count):
    if card in ['2', '3', '4', '5', '6']:
        return count + 1
    elif card in ['10', 'J', 'Q', 'K', 'A']:
        return count - 1
    return count

def get_bet_size(running_count, base_bet):
    if running_count >= 5:
        return base_bet * 5
    elif running_count >= 3:
        return base_bet * 3
    elif running_count >= 1:
        return base_bet * 2
    return base_bet

def get_recommended_play(player_value, dealer_upcard):
    if player_value >= 17:
        return "Stand"
    elif player_value <= 11:
        return "Hit"
    elif player_value == 12 and dealer_upcard in ['4', '5', '6']:
        return "Stand"
    elif player_value >= 13 and dealer_upcard in ['2', '3', '4', '5', '6']:
        return "Stand"
    elif player_value == 10 and dealer_upcard not in ['10', 'A']:
        return "Double Down"
    elif player_value == 11:
        return "Double Down"
    return "Hit"

player_money = 1000  # Starting money
blackjack_multiplier = 2.5  # Payout multiplier for blackjack
base_bet = 10  # Base bet amount

while len(deck2) >= 4 and player_money > 0:
    time.sleep(4)
    print("\nStarting a new round...\n")
    print(f"You have ${player_money}")
    print(f"Current running count: {running_count}")
    recommended_bet = get_bet_size(running_count, base_bet)
    print(f"Recommended bet size: ${recommended_bet}")
    
    while True:
        try:
            bet = int(input("Enter your bet amount: "))
            if bet > player_money or bet <= 0:
                print("Invalid bet. You cannot bet more than you have or less than 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")
    
    d1, p1, d2, p2 = deck2.pop(0), deck2.pop(0), deck2.pop(0), deck2.pop(0)
    dealer_hand, player_hand = [d1, d2], [p1, p2]
    
    running_count = update_count(d1, running_count)
    running_count = update_count(d2, running_count)
    running_count = update_count(p1, running_count)
    running_count = update_count(p2, running_count)
    
    dealer_value = calculate_value(dealer_hand)
    player_value = calculate_value(player_hand)
    
    print("Dealer's cards: [Hidden]", d2)
    print("Dealer's visible hand value:", calculate_value([d2]))
    print("Player's cards:", p1, p2)
    print("Player's hand value:", player_value)
    
    if player_value == 21:
        print("Blackjack! You win with a multiplier!")
        player_money += int(bet * blackjack_multiplier)
        continue
    
    doubled_down = False
    if player_money >= bet and len(player_hand) == 2:
        double_down = input("Do you want to double down? (y/n): ")
        if double_down.lower() == "y":
            bet *= 2
            hit = deck2.pop(0)
            player_hand.append(hit)
            player_value = calculate_value(player_hand)
            running_count = update_count(hit, running_count)
            print("Player doubled down and drew:", hit)
            print("Player's hand value:", player_value)
            doubled_down = True
    
    if not doubled_down:
        while player_value < 21:
            recommended_play = get_recommended_play(player_value, d2)
            print(f"Recommended play: {recommended_play}")
            choice = input("Hit (h) or stand (s): ")
            if choice == "h":
                hit = deck2.pop(0)
                player_hand.append(hit)
                player_value = calculate_value(player_hand)
                running_count = update_count(hit, running_count)
                print("Player drew:", hit)
                print("Player's hand value:", player_value)
            elif choice == "s":
                break
    
    while dealer_value < 17:
        hit = deck2.pop(0)
        dealer_hand.append(hit)
        dealer_value = calculate_value(dealer_hand)
        running_count = update_count(hit, running_count)
        print("Dealer drew:", hit)
        print("Dealer's hand value:", dealer_value)
    
    print("Final Dealer's hand value:", dealer_value)
    print("Final Player's hand value:", player_value)
    
    if player_value > 21:
        print("Player busts! Dealer wins.")
        player_money -= bet
    elif dealer_value > 21:
        print("Dealer busts! Player wins!")
        player_money += bet
    elif dealer_value > player_value:
        print("Dealer wins!")
        player_money -= bet
    elif dealer_value < player_value:
        print("Player wins!")
        player_money += bet
    else:
        print("It's a tie! Bet refunded.")
    
    if len(deck2) < 4:
        print("Not enough cards left in the deck. Game over!")
        break
    
    if player_money <= 0:
        print("You have run out of money! Game over.")
        break
















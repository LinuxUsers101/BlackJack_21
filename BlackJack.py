import random

cards = ["⭐️", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "♛", "♚"]
suits =  ["♠", "♥", "♦", "♣"]
values = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13
}

blackjack = "3:2"
regularW = "1:1"       
insurance = "2:1"   
#for a blackjack win (3:2 payout), your total payout would be £75 (1.5 × £50).
#For a regular win (1:1 payout), your total payout would be £50 (1 × £50).
#For insurance (2:1 payout), if you placed the usual insurance bet of half your original bet (£25), your insurance payout would be £50 (2 × £25). 
#your insurance payout would be £50 (2 × £25).
#£50 (1 × £50). regular 
#$75 (1.5 × £50). blackjacks

bj = 21 
BET = 0
bank_account = 10000
stand = False
The_Deck = [(card, suit) for suit in suits for card in cards]
Yhand = random.choice(The_Deck)
Yhand2 = random.choice(The_Deck)
dealerH = random.choice(The_Deck)
dealerH2 = random.choice(The_Deck)
hand = [Yhand, Yhand2]
Dhand = [dealerH, dealerH2]
Bust = False
def rules():
    print("The Main Rules and Regulations")
    print("1) Objective")
    print("2) Card Values")
    print("3) Initial Deal")
    print("4) Players Choices")
    print("5) Dealer Rules")
    print("6) Winning & Payouts")
    option = input("What would you like to know: ").strip().lower()
    if option == "1":
        print("The goal is to have a card total closer to 21 than the dealer without going over 21.")
    elif option == "2":
        print(values)
    elif option == "3":
        print("Each player receives two face-up cards; the dealer gets two cards, one face down (hole card).")
    elif option == "4":
        print("Hit - Request A Card")
        print("Stand - Stick with your current Hand (End Turn)")
        print("Double Down - Doubles The bet, Takes one last card")
        print("Split - pairs into two hands by placing an equal additional bet")
    elif option == "5":
        print("The Dealer will hit until reaching at least 17")
    elif option == "6":
        print("A BlackJack is an ace and a 10-Value card in the first hand the Payout is 3:2")
        print("Players win if there hand is closer to 21 than the dealers hand")
        print("If Dealer goes bust, Player wins")
        print("Ties will Result in a push and bets are returned")
    else:
        print("Enter a Valid Case")


def hand_total(hand):
    total = 0
    aces = 0
    for card, suit in hand:
        if card in ["J", "♚", "♛"]:
            total += 10
        elif card == "⭐️" or card == "Ace":
            aces += 1
            total += 11
        else:
            total += int(card)
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

def is_blackjack(hand):
    if len(hand) == 2:
        card_values = [card for card, suit in hand]
        if ("⭐️" in card_values or "Ace" in card_values) and any(c in card_values for c in ["10", "J", "♛", "♚"]):
            return True
    return False

def winning():
    global hand, Dhand, BET, bank_account
    player_total = hand_total(hand)
    dealer_total = hand_total(Dhand)
    
    if is_blackjack(hand):
        if is_blackjack(Dhand):
            # Both player and dealer have blackjack - push
            print(f"Both player and dealer have blackjack. Push. Bet returned: {BET}$")
            bank_account += BET
        else:
            # Player blackjack wins with 3:2 payout
            payout = int(BET * 1.5)
            print(f"Blackjack! You win {payout}$")
            bank_account += BET + payout
            print(f"Your new bank account: {bank_account}")
    else:
        if player_total > 21:
            print(f"You bust! Dealer wins. You've lost {BET}$")
        elif dealer_total > 21:
            print(f"Dealer busts! You win. You've won {BET}$")
            bank_account += BET * 2
            print(f"Your new bank account: {bank_account}")
        elif player_total > dealer_total:
            print(f"You won! You've gained {BET}$")
            bank_account += BET * 2
            print(f"Your new bank account: {bank_account}")
        elif dealer_total > player_total:
            print(f"Dealer won! You've lost {BET}$")
        else:
            print(f"Push, you get your bet back: {BET}$")
            bank_account += BET
            print(f"Your new bank account: {bank_account}")


def blackJackG():
    global BET
    global bank_account
    
    print("Welcome to BlackJack")
    print(" 1 | 5 | 10 | 50 | 100 | 1000 | Custom ")
    if bank_account <= 0:
        print("Please ensure you have money")
        return
    bet = input("Please Select a Bet: ").strip()
    while bet not in ["1", "5", "10", "50", "100", "1000", "custom"]:
        print("Please enter a valid Bet")
        bet = input("Please Select a Bet: ").strip()
    if bet == "custom":
        customBet = input("Enter a Custom Bet: ").strip()
        while not customBet.isdigit() or int(customBet) <= 0:
            print("Please Enter Number Greater than 0")
            customBet = input("Enter a Custom Bet: ").strip()
        BET = int(customBet)
    else:
        BET = int(bet)
    
    if BET > bank_account:
        print("You don't have enough money for that bet.")
        return
    
    bank_account -= BET
    print("------------------------------------")
    player()
def points():
    for card, value in values.items():
        if card == "Ace" or card == "1":
            print(f"{card} can be worth 1 or 11")
        else:
            print(f"{card} is worth {value}")

def NextMov():
    print("------------------------------------")
    print("Available moves:")
    print("\n 1. Hit")
    print(" 2. Stand")
    print(" 3. Double")
    move = input("\nWhat is your next move?: ").strip().lower()
    global Yhand, hand, BET, stand
    if move == "hit":
        new_card = random.choice(The_Deck)
        hand.append(new_card)
        print("Your current cards:")
        for card in hand:
            print(f" - {card[0]} of {card[1]}")
        print(f"You've Chosen to Hit. Your latest card is: {new_card[0]} of {new_card[1]}.")
        player_total = hand_total(hand)
        if player_total > 21:
            Bust == True 
            print(f"Bust! Your total is {player_total}. You lose.")
            return
        NextMov()
    elif move == "stand":
        print("will luck Be on your side")
        stand = True
        print("Your current cards:")
        for card in hand:
            print(f" - {card[0]} of {card[1]}")
        playersT = hand_total(hand)
        print(f"Players's total: {playersT}")
        print("------------------------------------")
        print("Dealer's cards:")
        for card in Dhand:
            print(f" - {card[0]} of {card[1]}")
        dealer_total = hand_total(Dhand)
        print(f"Dealer's total: {dealer_total}")
        winning()
    elif move == "double":
        BET += BET
        new_card = random.choice(The_Deck)
        hand.append(new_card)
        print(f"Your Final Card is: {new_card[0]} of {new_card[1]}.")
        player_total = hand_total(hand)
        if player_total > 21:
            print(f"Bust! Your total is {player_total}. You lose.")
        winning()
    else: 
        print("Sorry, that choice isn't valid. Please choose again")
        NextMov()
        

def blur(card):
    return "?? of ??"
    
def dealer():
    global BET
    print(f"The dealer flips over the {dealerH[0]} of {dealerH[1]}")
    if stand == False:
        print(f"The dealer takes out there second card, the {blur(dealerH2)}")
    elif stand == True:
        print(f"The dealer reveals their second card, the {dealerH2[0]} of {dealerH2[1]}")
    Dhand = [dealerH, dealerH2]
    dealer_total = hand_total(Dhand)
    if dealer_total > 21:
        BET += BET
        print(f"Dealer busts with {dealer_total}! You win!, {BET}")
        return
    NextMov()
def player():
    print(f"The dealer slides you the {Yhand[0]} of {Yhand[1]}.")
    print(f"The dealer slides your second card, {Yhand2[0]} of {Yhand2[1]}.")
    print("------------------------------------")
    player_total = hand_total(hand)
    if player_total > 21:
        BET -= BET
        print(f"Bust! Your total is {player_total}. You lose, {BET}")
        return
    if player_total < 21:
        print("BLACKJACK")
    dealer()
    
print("------------------------------------")
blackJack = input("Welcome to Blackjack. Play or pass?: ").strip().lower()
print("------------------------------------")
    
while blackJack not in ["play", "pass"]:
    print("Please enter a valid option")
    blackJack = input("Welcome to Blackjack. Play or pass?: ").strip().lower()
        
if blackJack == "play":
    Guide = input("Do You Want look at the Guide y/n ")
    while Guide not in ["y", "n"]:
        print("Please Enter a Valid Choice")
        Guide = input("Do You Want look at the Guide y/n ")
    if Guide == "y":
        rules() 
    else: 
        blackJackG()
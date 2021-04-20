import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


playing = True
game_on = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    
    def __init__(self):
        self.deck = []

        for suit in suits:
            for rank in ranks:
                new_card = Card(suit, rank) # instantiate each card in the for loop with the class Card, then append it to the list self.deck
                self.deck.append(new_card)

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp


    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self,name):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.name = name

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        pass

    def __str__(self):
        return self.name

      


class Chips:

    def __init__(self, total=100):
        self.total = total 

    def win_bet(self, value_bet):
        self.total += value_bet

    def lose_bet(self, value_bet):
        self.total -= value_bet


def take_bet(user_chip):

    while True:

        try:
            bet = int(input('Type the value for the bet\n'))
            if bet < user_chip.total:
                return bet
            

        except:

            print("An error occured! \n")
            continue

        else:
            print('You dont have money enough')


def hit(deck, hand):

    pop_card = deck.deal()
    
    if pop_card.rank == 'Ace':

        if hand.value + pop_card.value > 21:
            pop_card.value = 1
            hand.value += pop_card.value
            print(f'{hand.name} card is: {pop_card} and the value is 1')
            hand.add_card(pop_card)

        else:
            hand.value += pop_card.value
            print(f'{hand.name} card is: {pop_card}  and the value is {pop_card.value}')
            hand.add_card(pop_card)

    else:
        
        hand.value += pop_card.value
        hand.add_card(pop_card)



def hit_or_stand(deck, hand):
    global playing

    user_choice = input('\nType Hit or Stand\n').lower()

    if user_choice == 'hit':
        hit(deck, hand)

    else:
        #print('player has choose to stand')
        playing = False
    

def show_some(player, dealer):
    print('\n'+ '*' * 10 + 'SHOW SOME OF THE CARDS' + '*' * 10)
    print('\nDealer cards are:')
    for card in dealer.cards[:]:
        print(card, card.value)
    print('Dealer value', dealer.value)
    

    print('\nPlayer cards are:')
    for card in player.cards:
        print(card, card.value)

    print('player value', player.value)
  

def show_all(player,dealer):
    print('\n'+ '*' * 10 + 'SHOW ALL' + '*' * 10)
    print('\nDealer cards are:')
    for card in dealer.cards:
        print(card, card.value)
    print(f'Dealer hands value is {dealer.value}')

    print('\nPlayer cards are:')
    for card in player.cards:
        print(card, card.value)
    print(f'Player hands value is {player.value}')


def player_busts(player_hand):

    print(f'Player_BUST!!!!  hand is {player_hand.value}, END OF THIS ROUND!!')
    player_chips.lose_bet(bet_value)

        

def player_wins(player_hand):
    print(f'\nPlayer WINS! current player hand is {player_hand.value}')
    player_chips.win_bet(bet_value)

        

def dealer_busts(dealer_hand):
    print(f'\nDealer BUST! Dealers hand is {dealer_hand.value}') 
    player_chips.win_bet(bet_value * 2)

    
   
def dealer_wins(dealer_hand):
    print(f'\nDealer WINS! Dealers hand is {dealer_hand.value}')

    
def push():
    pass


while game_on:

    # Print an opening statement
    print('\n'*20 + '-'*10 + "Starting BlackJack" + '-'*10)

    
    # Create & shuffle the deck, deal two cards to each player
    red_deck = Deck()
    red_deck.shuffle()
    player = Hand('player')
    dealer = Hand('dealer')

    #print(red_deck.__str__())

    for i in range(2):
        hit(red_deck,player)

    
    for i in range(2):
        hit(red_deck,dealer)
    
        
    # Set up the Player's chips
    player_chips = Chips()
    
    # Prompt the Player for their bet
    bet_value = take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)    
    show_some(player, dealer)


    print('-'* 20 + 'INITIATING GAME' + '-'*20)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(red_deck, player)
           
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
 
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player)
            break  


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer.value < 17 or (dealer.value <= player.value and dealer.value < 21):
        hit(red_deck, dealer)       
        
        # Show all cards
        show_all(player, dealer)
        
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(dealer)
            break

        elif dealer.value > player.value:
            dealer_wins(dealer)
            break
      
            
        
    # Inform Player of their chips total 
    print(f'\n Player has {player_chips.total} left')

        
    # Ask to play again

    user_input = input("say 'YES' to play or 'NO' to stop").lower()
    print('\n', user_input)
    if user_input == 'yes' or 'y':
        playing = True

    if user_input == 'no' or 'n':
        game_on = False
        print('USER_INPUT', game_on)


      



  



                





# Rules:

# 1 - Player keeps hitting goes over 21, they bust and lost the bet. The game is then over and dealer collects the money. That happens even before the dealer start.

# 2 - The computer Dealer beats the Player. Computer sum higher than player sum and still under 21.  If Player is under 21, dealer then hits until they either beat the player or the dealer bust.

# 3 - Player wins after computer dealer goes over 21. If player is under 21, dealer then hits until they either beat the player or the dealer busts . receives double bet
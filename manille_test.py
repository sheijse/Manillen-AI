# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 12:57:07 2021

@author: Steven
"""


# self.card.len => len(self.card)
# if list -> list is not empty
# if not list -> list is empty

# to rotate objects in list efficiently
from collections import deque

# to sort efficiently using sorted
from operator import itemgetter, attrgetter

import random
import pygame

suitsNL2 = ["Pijken", "Harten", "Klaveren", "Koeken"]
suitsNL = ["Schoppen", "Harten", "Klaveren", "Ruiten"]

suitsENG = ["Pikes", "Hearts", "Clovers" , "Tiles"]
suitsENG2 = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

suitsSymbols = [u'\u2664', u'\u2665', u'\u2667', u'\u2666']

suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

point_values = {1:4, 7:0, 8:0, 9:0, 10:5, 11:1, 12:2, 13:3}

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def show(self):
        #print("{} of {}".format( self.value, self.suit))
        print(f"{self.val} of {self.suit}")
        
    def match(self, **kwargs):
        return all(getattr(self, key) == val for (key, val) in kwargs.items())
        
class playedCard(Card):
    def __init__(self, suit, val, player_name, first = False, highest = False):
        self.suit = suit
        self.val = val
        self.player = player_name
        self.first = first
        self.highest = highest
    
    def show(self):
        super().show(self)
        
    def get_player(self):
        return self.player
    
    def get_first(self):
        return self.first
    
    def get_highest(self):
        return self.highest   

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        for suit in suits:
            
            # in manielen only 7, 8, 9, 10, J, Q, K and 1 or A are used
            for val in range(7,14):                                 
                self.cards.append(Card(suit,val))
            self.cards.append(Card(suit,1))
            
            # for regular decks using 52 cards
            # for val in range(1,14):                                 
            #     self.cards.append(Card(suit,val))

    def show(self):
        for card in self.cards:
            card.show()
            
    def shuffle(self):
        for i in range(len(self.cards) -1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
            
    def drawCard(self):
        return self.cards.pop()
    
    
    
class Player:
    def __init__(self, player_name, number, team, first = False):
        self.name = player_name
        self.number = number #1-4
        self.team = team # 2 teams
        
        #generate unique ID
        self.id = random.randint(0 ,2**8)
        
        self.dealer = first
        self.hand = []
        
        # is updated in draw_hand() function
        self.param = {'suit': ['number of cards in hand of said suit', 'total points of these cars']}
        for suit in suits:
            self.param[suit] = [0,0]
            
    def checkTeam(self, player_name):
        pass
        
    def draw(self, deck):
        card = deck.drawCard()
        self.hand.append(card)
        amount, points = self.param[card.suit]
        self.param[card.suit] = [amount+1, points + point_values[card.val]]
        return self
    
    def draw_hand(self, deck):
        for i in range(0,8):
            self.draw(deck)
            
        self.sort_cards()
        
        self.param = {}

        for suit in suits:
            for card in self.hand:
                if card.suit == suit:
                    print(f"{card.suit} == {suit}")
                    [number_of_cards, number_of_points] = self.param[suit]
                    number_of_cards += 1
                    number_of_points += point_values[card.val] # only decent because tested for number of cards first
        
    def showHand(self):
        for card in self.hand:
            card.show()
            
    def get_dealer(self):
        return self.dealer
    
    def set_hand(self, hand): # deal player an array of 8 cards
        for card in hand:
            self.hand.append(card)
    
    # show might not be ideal
    def get_hand(self):
        self.show_hand()
        
    def all_cards_from_suit(self, **kwargs):
        return list(self.__iterCard(**kwargs))
    
    def __iterCard(self, **kwargs):
       return (card for card in self.hand if card.match(**kwargs))
 
# not finished, currently defined in subclas  
    def playCard(self, card):
        if card in self.hand:
            c = playedCard(card.suit, card.val, self.name)
            #roundNumber = len(rounds)+1
        else:
            raise Exception('No such card in hand')
            
######## doesn't work    
    def sort_cards(self):
        sorted_hand = []
        for suit in suits:
            l = [card.suit == suit for card in self.hand]
            print(l)
            l = sorted(l, key = attrgetter('suit'))
            sorted_hand.append(l)
            
    # players from team that did not choose trump_suit can decide to play this round for double points
# currently not used, needs fleshing out or decision made by AI
    def double_points(self, trump_suit):
        [number_of_cards, number_of_points] = self.param[trump_suit] 
        if number_of_cards >= 3:
            return True
        
        else:
            return False
    
    # if points are doubled then the player from the team that chose trump can decide to play for 4x points
# currently not used, needs fleshing out or decision made by AI
    def quadruple_points(self, trump_suit):
        [number_of_cards, number_of_points] = self.param[trump_suit] 
        if number_of_cards >= 3:
            return True
        
        else:
            return False
    
    # not the most ideal but pretty good
    # no trump is also a possible choice which is then palyed for double points (not iplemented yet)
    def chooseTrump(self): 
        
        ## is updated in draw_hand() instead so decision to play for double can be made
        # self.param = {}
        # for suit in suits:
        #     for card in self.hand:
        #         if card.suit == suit:
        #             [number_of_cards, number_of_points] = self.param[suit]
        #             number_of_cards += 1
        #             number_of_points += point_values[card.val] # only decent because tested for number of cards first
    
        highest_suit = self.param.keys[0]
        highest_number = 0
        highset_points_for_highest_number = 0
        
        for key, [amount, points] in self.param:
            if amount > highest_number:
                highest_suit = key
                highest_number = amount
                highset_points_for_highest_number = points
                
            elif ( amount == highest_number and points > highset_points_for_highest_number):
                highest_suit = key
                highest_number = amount
                highset_points_for_highest_number = points
        trump = highest_suit
        
        if True:
            pass
# geen troef kiezen
        
        
        return trump
                
       
class randomAI(Player):
    def __init__(self, name, number, team, first = False):
         super().__init__(name, number, team, first = False)
         
         
# work in progress
# test by making 1 player (first player), dealing him 8 cards (, sorting the cards), play card as if first player
    def playCard(self, played_suit, trump_suit, current_highest_card = None):  # includes trump if trump cards are played, current_highest_card is the card that is currently winning the round
        
        # checking variables
        if played_suit not in suits:
            raise Exception(f'argument played_suit not in {suits}') 
            
        if trump_suit not in suits:
            raise Exception(f'argument trump_suit not in {suits}') 
    
        if (current_highest_card != None) and not isinstance(current_highest_card, Card):
            raise TypeError("argument current_highest_card is not an instance of the class Card")
    
    
        # make empty list
        possibilities = []
    
        # play a random card if nothing has been played yet / this is the first player in a round
        if(current_highest_card == None):
            possibilities = self.hand
        
        # something has been played
        else:
### test if current_highest_card is played by player from the same team 
            if True: #both players are on the same team
                cards_from_suit = self.all_cards_from_suit(suit = played_suit)
                
                # no cards from played_suit to play -> play random card
                if not cards_from_suit: # checks if list is empty
                    possibilities = self.hand
                
                #play a random card from the played_suit
                else:
                    possibilities = cards_from_suit
                
            #both players are not on the same team -> have to play higher (trump) card
            else: 
                
                # played suit not overtaken by card from trump suit
                if played_suit == current_highest_card.suit: 
                    cards_from_suit = self.all_cards_from_suit(suit = played_suit)
                    
                    if cards_from_suit: # list contains card from played_suit (list not empty)
                    
                        #play a higher card from the same suit if possible
                        if current_highest_card.val != 10: # can't go higher than a 10 (manille)
                            
                            # cards with higher point values
                            possibilities = list(card for card in cards_from_suit if (point_values[card.val] > point_values[current_highest_card.val]))
                            # cards with equal point values but higher card values: 8 is highest 9 in hand
                            possibilities.append(list(card for card in cards_from_suit if (point_values[card.val] == point_values[current_highest_card.val] and card.val > current_highest_card.val)))

# houd geen rekening met 7 gespeeld en kan 8 leggen => solved (see above)
                    
                        #play a lower card from the same suit if possible
                        else: 
                            
                            # cannot play a higher card so any card from the suit will do
                            possibilities = cards_from_suit
                 
                    #no cards from played suit
                    else:
# moet overkopen indien mogelijk => solved (see below)

                        cards_from_trump_suit = list(card for card in self.hand if (card.suit == trump_suit))
                        
                        # if u have trump cards -> play 1
                        if cards_from_trump_suit:
                            possibilities = cards_from_trump_suit

                        # play a random card from hand
                        else:
                            possibilities = self.hand
                
                # highest card not from played_suit => trump card otherwise it would not be winning    
                else:
                    
                    if current_highest_card.suit != trump_suit:
                        raise Exception('trump suit does not equal suit of winning card nor that of the played suit')
                    
                    cards_from_suit = self.all_cards_from_suit(suit = played_suit)
                    cards_from_trump_suit = list(card for card in self.hand if (card.suit == trump_suit))
                    
                    #card is considere higher if it is worth more points or when they are worth equal (7,8,9) the one with the higher card.val
                    higher_cards_from_trump_suit = list(card for card in cards_from_trump_suit if (point_values[card.val] > point_values[current_highest_card.val] or (point_values[card.val] == point_values[current_highest_card.val] and card.val > current_highest_card.val)))

# mag niet onderkopen tenzij dat je niet kunt => solved ( see below)
                    # hand contains cards from played suit
                    if cards_from_suit: 
                        possibilities = cards_from_suit
                    
                    # in addition to no cards from the played suit, the hand contains no trump cards (list is empty)
                    elif not cards_from_trump_suit:
                        possibilities = self.hand
                    
                    # hand has trump cards higher than the winning card (cannot be higher than a 10)
                    elif (not higher_cards_from_trump_suit and current_highest_card.val != 10):
                        possibilities = higher_cards_from_trump_suit

                    # hand only has trump cards left lower than the winning card
                    elif len(cards_from_trump_suit) == len(self.hand):
                        possibilities = cards_from_trump_suit
                        
                    # no trump cards higher than the winning card but can still play other suits
                    else:
                        possibilities = list(card for card in self.hand if (card.suit != current_highest_card.suit))
                       
        
        if not possibilities:
            #play a random card
            possibilities = self.hand
            raise Exception('played a random card because there were no playable cards according to the if-else logic')

        chosen_card = random.choice(possibilities)
        played_card = playedCard(chosen_card.suit, chosen_card.val, self.name)
        return played_card
    
    

deck = Deck()
deck.shuffle()
deck.show()

#player_name, number, team, first = False
AI = randomAI( "random AI", "666", "0", False)
AI.draw_hand(deck)

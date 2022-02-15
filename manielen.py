# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 16:05:32 2021

@author: Steven
"""
# to rotate objects in list efficiently
from collections import deque

# to sort efficiently using sorted
from operator import itemgetter, attrgetter

import random
import pygame
import warnings

# cardgame using pygame
# https://www.askpython.com/python/examples/pygame-graphical-hi-lo-game

#combine pygame with discod bot?
#https://stackoverflow.com/questions/66732324/how-to-connect-discord-and-pygame

# implement a deck of cards
#http://www.mathcs.emory.edu/~cheung/Courses/170/Syllabus/10/deck-of-cards.html
#https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3

# info
# https://www.ibm.com/cloud/blog/ai-vs-machine-learning-vs-deep-learning-vs-neural-networks
# https://probablydance.com/2020/01/29/why-video-game-ai-does-not-use-machine-learning/
# https://www.quora.com/How-often-are-neural-networks-used-for-video-games-ML-or-AI-Why-is-this-the-case
# https://www.quora.com/What-real-life-data-science-skills-can-I-develop-in-order-to-get-my-first-data-science-job?encoded_access_token=d17a9c325af240eb848efd1f4881adea&expires_in=5183999&fb_uid=6164193376989469&force_dialog=1&provider=facebook&success=True#_=_
# https://deep-and-shallow.com/2020/02/02/the-gradient-boosters-i-the-math-heavy-primer-to-gradient-boosting-algorithm/

# tensorflow:
# https://www.tensorflow.org/tutorials
# https://ourcodeworld.com/articles/read/1433/how-to-fix-tensorflow-warning-could-not-load-dynamic-library-cudart64-110dll-dlerror-cudart64-110dll-not-found

# board game ai
# https://towardsdatascience.com/create-your-own-board-game-with-powerful-ai-from-scratch-part-1-5dcb028002b8

# AI of card game:

    # neural network cardgame
    #https://towardsdatascience.com/teaching-a-neural-network-to-play-cards-bb6a42c09e20
    
    # one hot encoding
    #https://machinelearningmastery.com/how-to-one-hot-encode-sequence-data-in-python/
    
    # general guide neural network
    #https://realpython.com/python-ai-neural-network/

    # forum post AI cardgame:
    # https://softwareengineering.stackexchange.com/questions/213870/best-techniques-for-an-ai-of-a-card-game#comment422433_213870
    # https://www.reddit.com/r/gameai/comments/42xu66/advice_on_building_a_card_game_ai/
    
    # AI for connect 4 game
    # https://www.youtube.com/watch?v=8392NJjj8s0

# --------------------

# STUPID AI IDEA:
    # makes the best decicion based on the winning card and the hand of the player
    # inputs:
        # played suit (4)
        # trump suit (4)
        # winning card (32/ 12) # 32 if u consider all possible cards, 12 (8+4) if u take a combination of suit and value (could be more efficient here)
        # hand (32)

# --------------------

# SMART AI IDEA:
# usefull information (Everything is one-hot encoded with either -1 or 1)

# only once:()
# trump suit (4) (5 if no trump is chosen)
# Current roundnumber (8)
# Cards already played in total (32)
# Cards in hand by active player (32)

#only for current round:
# Order of current player; equivalent to number of cards on table (4)

# for each round: ()
# first player/ player who won last round (4)
# cards played in round x (32)
# card played by player 1 in round x (32)
# card played by player 2 in round x (32)
# card played by player 3 in round x (32)
# card played by player 4 in round x (32)


# harvest data of random vs random
# harvest data of random vs current AI
# harvest data of user vs random
# harvest data of user vs current AI
# harvest data of random vs general if statements

# ----------------------

# finding object in array with certain attributes
# https://stackoverflow.com/questions/5180092/how-to-select-an-object-from-a-list-of-objects-by-its-attribute-in-python

    # #example for **kwargs
    # # Python program to illustrate 
    # # *kargs for variable number of keyword arguments
     
    # def myFun(**kwargs):
    #     for key, value in kwargs.items():
    #         print ("%s == %s" %(key, value))
     
    # # Driver code
    # myFun(first ='Geeks', mid ='for', last='Geeks')   

# extract sublist from list of objects
# https://stackoverflow.com/questions/49377878/python-fastest-way-to-extract-sublist-from-a-list-of-objects-given-an-attribute

# sort list based on object attributes
# https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes/4233482

# list comprehension example: newlist = [x for x in fruits if x != "apple"]
# https://www.w3schools.com/python/python_lists_comprehension.asp

# lambda functions
# https://www.w3schools.com/python/python_lambda.asp

# timing 
# https://stackoverflow.com/questions/2866380/how-can-i-time-a-code-segment-for-testing-performance-with-pythons-timeit

# increase performance
# https://stackify.com/20-simple-python-performance-tuning-tips/

# using Warnings
# https://docs.python.org/3/library/warnings.html#warnings.warn

# This gets the first item from the list that matches the condition, and returns None if no item matches.
# next((x for x in test_list if x.value == value), None)
# https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi?rq=1

# if x: #x is treated True except for all empty data types [],{},(),'',0 False, and None

# -------------------------


suitsNL2 = ["Pijken", "Harten", "Klaveren", "Koeken"]
suitsNL = ["Schoppen", "Harten", "Klaveren", "Ruiten"]

suitsENG = ["Pikes", "Hearts", "Clovers" , "Tiles"]
suitsENG2 = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds') #tuple because it's not allowed to be mutated by accident
suitOrder = {'Spades':1, 'Hearts':2, 'Clubs':3, 'Diamonds':4} #decides the order of sorting

point_values = {1:4, 7:0, 8:0, 9:0, 10:5, 11:1, 12:2, 13:3}

card_symbols_EN = {1:'A', 7:7, 8:8, 9:9, 10:10, 11:'J', 12:'Q', 13:'K'}
suitSymbols = [u'\u2664', u'\u2665', u'\u2667', u'\u2666']
suitSymbols_dict = {'Spades': u'\u2664', 'Hearts': u'\u2665', 'Clubs': u'\u2667', 'Diamonds': u'\u2666'}

# suits = {'S':'spades', 'H':'hearts', 'C': 'clubs', 'D':'diamonds'}
# values = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
#                'T':10, 'J':11, 'Q':12, 'K':13}

# cardpngs = {}
# for suit in suits:
#     for symbol in values.keys():
#         card_name = f"{suit}{symbol}"
#         folder_name = pygame.image.load(f'cards/{card_name}.png')
#         cardpngs[card_name] = folder_name

class Card:
    def __init__(self, suit, val):
        
        if suit not in suits:
            raise Exception(f'given suit is not in {suits}')
            
        if val not in range(1,14):
            raise Exception('Card value (val) must be 1 <= val <= 13, with 1 being the Ace and 13 being the King')
            
        # if val in range(2,7):
        #     warnings.warn("Warning: Card with value {val} is not used in the game Manille")
        
        self.suit = suit
        self.val = val
        
    def show(self):
        #print("{} of {}".format( self.value, self.suit))
        print(f"{self.val: <2} of {self.suit: >3} \t {card_symbols_EN[self.val]: >3} {suitSymbols_dict[self.suit]}")    
        
    def match(self, **kwargs):
        return all(getattr(self, key) == val for (key, val) in kwargs.items())
        
class playedCard(Card):
    def __init__(self, suit, val, Player, first = False, highest = False):
        self.suit = suit
        self.val = val
        self.player = Player
        self.first = first
        self.highest = highest
    
    def show(self):
        super().show()
        
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
    def __init__(self, player_name, number, teammate = None, first = False):
        self.name = player_name
        self.number = number #1-4
        self.teammate = teammate # 2 teams
        
        #generate unique ID
        self.id = random.randint(0 ,2**8)
        
        self.dealer = first
        self.hand = []
        
        # is updated in draw_hand() function
        # self.param = {'suit': ['number of cards in hand of said suit', 'total points of these cars']}
        self.param = {}
        for suit in suits:
            self.param[suit] = [0,0]
            
    def checkTeam(self, player_name):
        pass
    
    def get_dealer(self):
        return self.dealer
    
    def set_teammate(self, player):
        self.teammate = player
        
    def draw(self, deck):
        card = deck.drawCard()
        self.hand.append(card)
        amount, points = self.param[card.suit]
        self.param[card.suit] = [amount+1, points + point_values[card.val]]
        return self
    
    def draw_hand(self, deck):
        for i in range(0,8):
            self.draw(deck)
        
        #sort hand: first on suit, then on point value and last on card value
        self.hand.sort(key = lambda x: (suitOrder[x.suit], point_values[x.val], x.val))
        #self.sort_cards()
        
        for suit in suits:
            # reset values for every hand
            self.param[suit] = [0,0]
            
            for card in self.hand:
                if card.suit == suit:
                    # [number_of_cards, number_of_points] = self.param[suit]
                    # number_of_cards += 1
                    # number_of_points += point_values[card.val] # only decent because tested for number of cards first
                    # self.param[suit] = [number_of_cards, number_of_points]
                    
                    self.param[suit][0] += 1
                    self.param[suit][1] += point_values[card.val] # only decent because tested for number of cards first
                    
                    
    def set_hand(self, hand): # deal player an array of 8 cards
        self.hand = []
        for card in hand:
            self.hand.append(card)
            
        self.hand.sort(key = lambda x: (suitOrder[x.suit], point_values[x.val], x.val))
            
    def showHand(self):
        for card in self.hand:
            card.show()
    
    # show might not be ideal
    def get_hand(self):
        self.show_hand()
        
    def all_cards_from_suit(self, **kwargs):
        return list(self.__iterCard(**kwargs))
    
    def __iterCard(self, **kwargs):
       return (card for card in self.hand if card.match(**kwargs))
 
# not finished, currently defined in subclas  
    def playCard(self, card):
        if len(self.hand) > 8:
            raise Exception("more than 8 cards in hand")
            
        if len(self.hand) == 0:
            raise Exception("cards in hand = 0")
        
        if card in self.hand:
            c = playedCard(card.suit, card.val, self.name)
            #roundNumber = len(rounds)+1
        else:
            raise Exception('No such card in hand')
            
    def sort_cards(self):
        sorted_hand = []
        
        print('unsorted hand:')
        self.showHand()
        
        #sorted is slower because it creates a copy of the list, .sort is in place
        #self.hand = sorted(self.hand, key = lambda x: (x.suit, point_values[x.val])) #
        self.hand.sort(key = lambda x: (suitOrder[x.suit], point_values[x.val], x.val))
        print('\nsorted hand:')
        self.showHand()
        
        # is faster but only works if point_values is an attribute
        self.hand.sort(key = attrgetter('suit', 'val'))
        print('\nsorted hand (zttrgetter):')
        self.showHand()
            
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
        
        
        points_in_hand = 0
        
        for [amount, points] in self.param.values():
            points_in_hand += points
            
        print(f"total points in hand: {points_in_hand}")

        # if u have more than x points on hand play without trump -> points from this round are doubled
        x = 25
        if points_in_hand > x:
            trump = None
    
        # choose trump suit
        else:
            highest_suit = list(self.param.keys())[0]
            highest_number = 0
            highset_points_for_highest_number = 0
            
            for key in self.param.keys():
                [amount, points] = self.param[key]
                # only update if the suit has more cards or equal cards that are worth more points
                if (amount > highest_number or (amount == highest_number and points > highset_points_for_highest_number)):
                    highest_suit = key
                    highest_number = amount
                    highset_points_for_highest_number = points
                
            trump = highest_suit
            
        return trump
       
class randomAI(Player):
    def __init__(self, name, number, team, first = False):
         super().__init__(name, number, team, first = False)
         
         
    def chooseRandomTrump(self, must_be_in_hand = False):  
        
        chosen_suit = random.choice(suits)
        choose_different_suit = True
        make_copy = True

        while choose_different_suit:
            for card in self.hand: # could possibley be done in 1 line of code
                if card.suit == chosen_suit:
                    choose_different_suit = False
                    break
                else:
                    if make_copy:
                        possibilities = list(suits.copy)
                        make_copy = False
                    
                    possibilities.remove(chosen_suit)
                    random.choice(possibilities)
            
        return chosen_suit
         
# work in progress
# test by making 1 player (first player), dealing him 8 cards (, sorting the cards), play card as if first player
    def playCard(self, played_suit, trump_suit, current_highest_card):  # includes trump if trump cards are played, current_highest_card is the card that is currently winning the round
        
        # checking variables
        if played_suit not in suits:
            raise Exception(f'argument played_suit not in {suits}') 
            
        if trump_suit not in suits:
            raise Exception(f'argument trump_suit not in {suits}') 
    
        if (current_highest_card != None) and not isinstance(current_highest_card, Card):
            raise TypeError("argument current_highest_card is not an instance of the class Card")
            
        if len(self.hand) > 8:
            raise Exception("more than 8 cards in hand")
            
        if len(self.hand) == 0:
            raise Exception("cards in hand = 0")
            
        if self.teammate is None:
            raise Exception("no teammate set")
    
        # make empty list
        possibilities = []
    
        # play a random card if nothing has been played yet / this is the first player in a round
        if(current_highest_card is None): # == None vs is None
            possibilities = self.hand
        
        # something has been played
        # only 1 card in hand
        elif len(self.hand) == 1:
            possibilities = self.hand
            
        # more than 1 card in hand    
        else:
### test if current_highest_card is played by player from the same team 
            if self.teammate == current_highest_card.player: #both players are on the same team
                cards_from_suit = self.all_cards_from_suit(suit = played_suit)
                
                #play a random card from the played_suit
                if cards_from_suit: # checks if list is NOT empty
                    possibilities = cards_from_suit
                
                # no cards from played_suit to play -> play random card
                else:
                    possibilities =  self.hand
                
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
                    
                        #play a lower card from the same suit if possible
                        else: 
                            
                            # cannot play a higher card so any card from the suit will do
                            possibilities = cards_from_suit
                 
                    #no cards from played suit
                    else:
# could be a porblem is suit == None
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
        
        # choose card rondomly from possibilities
        chosen_card = random.choice(possibilities)
        # make the card a played card
        played_card = playedCard(chosen_card.suit, chosen_card.val, self)
        #delete card from hand
        self.hand.remove(chosen_card)
        return played_card
        
       
class Round:
    def __init__(self, dealer, roundNumber = 0):
        self.roundNumber = roundNumber #1-8
        
        self.dealer = dealer
        self.cardsPlayed = [] #max 4 per round
        self.disallowedPlayers = []
        self.trump = None
        
    def get_roundNumber(self):
        return self.roundNumber
    
    def set_roundNumber(self, roundNumber):
        self.roundNumber = roundNumber
        
    def inc_roundNumber(self):
        self.roundNumber += 1
        
    def get_cardsPlayed(self):
        return self.cardsPlayed
    
    def add_playedCard(self, playedCard):
# test player order
        if playedCard.player in self.disallowedPlayers:
            raise Exception('this player cannot play more than 1 card')
        self.cardsPlayed.append(playedCard)
        self.disallowedPlayers.append(playedCard.player)
        
    
    def set_dealer(self, player):
        self.dealer = player
        
class Team:
    def __init__(self, player1, player2, team_name = None):
        self.players = [player1, player2]
        self.name = team_name
        self.points = 0
        
    def get_points(self):
        print(self.points)
     
    # could check for 121 points here or before updating self.points
    def set_points(self, points): # total points not value added to it, needs to be incremented before hand
        self.points = points

class Game:
    def __init__(self, player1, player2, player3, player4):
        self.players = [player1, player2, player3, player4]
        self.teams = [Team(player1, player3), Team(player2, player4)]
        
        # variable containing information about the current and previous rounds
        self.rounds = []
        self.roundNumber = 1
        self.dealer = random.choice(self.players) #dealer and person choosing trump suit
        self.roundOrder = deque(self.players)
        
        #setup round 1
        self.setupNextRound()
    
    def setupNextRound(self):                           # all player and round variables should be set
        r = Round(self.dealer, self.roundNumber)
        self.rounds.append(r)
        
        #set roundorder
        index = self.players.index(self.dealer)
        self.roundOrder.rotate(-(index+1))      #person left of the dealer is allowed to start
        
        deck = Deck()
        deck.shuffle() # could be too good to mimic real games
        
        # deal cards
        # easy way: because shuffling is done very well
        for player in self.roundOrder:
            for i in range(0,8):
                player.draw()
                
        # human way: 
        # players = self.roundOrder
        # for player in players:
        #     for i in range(0,3):
        #         player.draw()
        # for player in players:
        #     for i in range(0,2):
        #         player.draw()
        # for player in players:
        #     for i in range(0,3):
        #         player.draw()
        
        r.trump = self.dealer.chooseTrump() # change to AI?
        
    def playRound(self):
        
        
        for player in self.roundOrder:
            player.playCard()               # change to AI?
        
        # after all 4 cards are played
        # increase points:
            
        # rotate dealer
        pass


print("\n------------------\nTest trump choice random hand: \n")    
deck = Deck()
deck.shuffle()
#deck.show()

#player_name, number, team, first = False
AI = randomAI( "random AI", "666", "0", False)
AI.draw_hand(deck)
AI.showHand()
print(f"chosen trump suit: {AI.chooseTrump()}")

print("\n------------------\nExample playCard: \n")
print("set player hand:")

hand = []
suit = suits[0]

for val in range(7, 14):
    hand.append(Card(suit,val))
hand.append(Card(suit, 1))

AI.set_hand(hand)
AI.showHand()

print("\nset round variables:")

played_suit = suits[0]
trump_suit = suits[0]

suit = suits[0]
value = 7
current_highest_card = Card(suit, value) # can be duplicate because generated seperatly from the Deck

print(f"played suit: \t{played_suit}")
print(f'trump suit: \t{trump_suit}')
print('current winning card of the round:')
current_highest_card.show()

played_card = AI.playCard(played_suit, trump_suit, current_highest_card)
print(f"\ncard played by player {AI.name}:")
played_card.show()
print("\nplayer hand after:")
AI.showHand()

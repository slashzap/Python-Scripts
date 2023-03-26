'''
Setup
* create a deck of cards
    * use a set to ensure uniqueness
* create a player
    * player has an empty set of cards
* create the house
    * house has an empty set of cards
* deal 1 card to the player then the house, then repeat

> check win conditions

Play Turn
* Player chooses:
    * Hit (take a card)
        * check win conditions
    * Stay (play goes to house)
* House turn
    * Hit (see house rules)
        * check win conditions
    * Stay

> check win conditions

Win conditions
* if 21, they win
* if over 21, they lose
* highest total wins

*** there are some other win / special conditions, but I need to look them up

'''
import random

def get_sum(hand):
  hand_sum = 0
  for card in hand:
    cval = values[card]
    hand_sum += cval
  return hand_sum

def check_win(hand_name, hand_sum):    
  if hand_sum == 21:
    print(f"{hand_name} blackjack")
    return 1
  elif hand_sum > 21:
    print(f"{hand_name} bust")
    return -1
  else:
    print(f"{hand_name} Total ={hand_sum}")
    return 0

def get_card():
  deck_list = list(deck)
  #print(deck_list)
  card = random.choice(deck_list)
  deck.remove(card)
  return card

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
winner = None
cards = "A234567890JQK"
deck = set(cards)
values = {"A":11, "0":10, "J":10, "Q":10, "K":10, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

#print(deck)
print("#" * 10)
player = set()
house = set()
table = [player, house]
hand_size = 2
deal_count = 0

while(deal_count < hand_size):
  for hand in table:
    hand.add(get_card())    
  deal_count += 1
  
print(player)
print(house)


winner = check_win("Player", get_sum(player))
winner = check_win("House", get_sum(house))

while( winner == 0):
  action = input("Player, do you want another card? (H)it, (S)tay >>").upper()
  if action == "S":
    break
  else:
    player.add(get_card())
    print(player)
    winner = check_win("Player", get_sum(player))
  
while( winner == 0):
  if get_sum(house) < 16:
    house.add(get_card())
    print(house)
    winner = check_win("House", get_sum(house))
  else:
    break

if winner == 0:  
  print(f"House has {get_sum(house)}, Player has {get_sum(player)}")
  if get_sum(house) >= get_sum(player):
    print("House wins")
  else:
    print("Player wins")  

      
print("game over")

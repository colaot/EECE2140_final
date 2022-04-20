import itertools
from itertools import permutations
from cards import Card, Deck

class Table:
  def __init__(self, players, deck, player_hand = [], community_cards = []):
    self.players = players
    self.num_players = len(players)
    self.deck = deck
    self.player_hand = player_hand
    self.community_cards = community_cards

  def get_num_players(self):
    return self.num_players

  def deal(self):
    for i in [1, 2]:
      for i in range(num_players):
        if (players[i] == None):
          self.deck.pop()
        else:
          self.player_hand.append(self.deck.pop())

  def get_player_hand(self):
    return self.player_hand

  def deal_comm_cards(self):
    self.deck.deal_card()
    self.community_cards = self.deck.dealt

  def get_comm_cards(self):
    return self.community_cards

  def get_hand(self):
    all_hands = list(itertools.combinations(self.community_cards + self.player_hand, 5))
    for hand in all_hands:

      freq = {}
      for card in hand:
        if card.get_rank() in freq:
          freq[card.get_rank()] += 1
        else:
          freq[card.get_rank()] = 1
      print(freq)

  @staticmethod
  def flush(hand):
    if len(set([card.get_suit() for card in hand])) == 1:
        return True
    return False
  @staticmethod
  def quads(freq):
    for num in freq.values():
      if num == 4:
        return True
    return False

  @staticmethod
  def trips(freq):
    for num in freq.values():
      if num == 3:
        return True
    return False

  @staticmethod
  def pair(freq):
    high_pair == 
    for num in freq.values():
      if num == 2:

      if num == 3:
        return True








c1 = Card("A", "s")
c2 = Card("K", "s")

b1 = Card("A", "c")
b2 = Card("A", "d")
b3 = Card("A", "h")
b4 = Card("Q", "s")
b5 = Card("J", "s")

d = Deck()
d.ordered_deck()
d.shuffle()
t = Table([], d, [c1, c2], [b1,b2,b3,b4,b5])
t.get_hand()

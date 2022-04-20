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
      if len(set([card.get_suit() for card in hand])) == 1:
        print(True)
        print(hand[0], hand[1], hand[2], hand[3], hand[4])
        return








c1 = Card("A", "s")
c2 = Card("K", "s")

b1 = Card("3", "c")
b2 = Card("8", "c")
b3 = Card("7", "c")
b4 = Card("Q", "s")
b5 = Card("J", "s")

d = Deck()
d.ordered_deck()
d.shuffle()
t = Table([], d, [c1, c2], [b1,b2,b3,b4,b5])
t.get_hand()

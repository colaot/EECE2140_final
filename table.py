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

  def get_deck(self):
    return self.deck

  def deal(self):
    for i in [1, 2]:
      for i in range(self.num_players):
        if (self.players[i] == None):
          self.deck.get_cards().pop()
        else:
          self.player_hand.append(self.deck.get_cards().pop())

  def get_player_hand(self):
    return self.player_hand

  def deal_comm_cards(self):
    self.deck.deal_card()
    self.community_cards = self.deck.dealt

  def get_comm_cards(self):
    return self.community_cards

  def get_hand(self):
    all_best_hand = []
    best_hand = []
    curr = []

    all_hands = list(itertools.combinations(self.community_cards + self.player_hand, 5))
    for hand in all_hands:
      freq = {}
      for card in hand:
        if card.get_rank() in freq:
          freq[card.get_rank()] += 1
        else:
          freq[card.get_rank()] = 1

      f = Table.flush(hand)
      s = Table.straight(hand)
      q = Table.quads(freq)
      t = Table.trips(freq)
      p = Table.pair(freq)
      
      if f and s and s not in curr:
        curr.append((9, s))
      if q and q not in curr:
        curr.append((8, q))
      if t and p and (t, p) not in curr:
        curr.append((7, (t, p)))
      if f and f not in curr:
        curr.append((6, f))
      if s and s not in curr:
        curr.append((5, s))
      if t and not p and t not in curr:
        curr.append((4, t))
      if p and len(p) == 2 and p not in curr:
        curr.append((3, p))
      if p and len(p) == 1 and p not in curr:
        curr.append((2, p))
      all_best_hand.append(curr)
      curr = []

    high = 0
    for hand in all_best_hand:
      if hand != []:
        if hand[0][0] > high:
          high = hand[0][0]
          best_hand = hand
    print(best_hand)


  @staticmethod
  def flush(hand):
    max = hand[0]
    if len(set([card.get_suit() for card in hand])) == 1:
        for card in hand:
          if card.get_value() > max.get_value():
            max = card
        return max.get_rank()
    return False

  @staticmethod
  def straight(hand):
    s = Card.card_sort(hand)
    prev = s[0]
    for i in range(1, 5):
      if s[i].get_value() - prev.get_value() != 1:
        return False
      prev = s[i]
    return s[4].get_rank()

  @staticmethod
  def quads(freq):
    for num in freq.values():
      if num == 4:
        return list(freq.keys())[list(freq.values()).index(num)]
    return False

  @staticmethod
  def trips(freq):
    for num in freq.values():
      if num == 3:
        return list(freq.keys())[list(freq.values()).index(num)]
    return False

  @staticmethod
  def pair(freq):
    output = []
    for num in freq.keys():
      if freq[num] == 2:
        output.append(num)
    if len(output) == 0:
      return False
    elif len(output) == 1:
      return output[0]
    return output

c1 = Card("A", "s")
c2 = Card("K", "s")

b1 = Card("A", "c")
b2 = Card("K", "d")
b3 = Card("10", "s")
b4 = Card("Q", "s")
b5 = Card("J", "s")

d = Deck()
d.ordered_deck()
d.shuffle()
t = Table([], d, [c1, c2], [b1,b2,b3,b4,b5])
t.get_hand()
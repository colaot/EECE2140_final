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

  def place_comm_cards(self, cards):
    self.deck.place_cards(cards)
    self.community_cards = self.deck.dealt

  def get_comm_cards(self):
    return self.community_cards

  def get_all_hands(self, freq = False):
    all_hands = list(itertools.combinations(self.community_cards, 3))
    a = []
    output = []
    output_freq = []
    for hand in all_hands:
      for card in hand:
        a.append(card)
      for card in self.player_hand:
        a.append(card)
      a = Card.card_sort(a)
      output.append(a)
      a = []

    if freq:
      for hand in output:
        freq = {}
        for card in hand:
          if card.get_rank() in freq:
            freq[card.get_rank()] += 1
          else:
            freq[card.get_rank()] = 1
        output_freq.append(freq)
      return output_freq
    return output


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
      
      if f and s and s == "Ace":
        curr.append((10, s))
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
    return best_hand


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
    return output

  def pockets(self):
    if self.player_hand[0].get_value() == self.player_hand[1].get_value():
      return 2

  def overcard(self):
    overs = 0
    for card in self.player_hand:
      if set([c.get_value() < card.get_value() for c in self.community_cards]) == {True}:
        overs += 1
    if overs == 1:
      return 3
    elif overs == 2:
      return 6

  def s_draw_in(self):
    sd = []
    draw_count = 0
    max_draw_count = 0
    if abs(self.player_hand[0].get_value() - self.player_hand[1].get_value()) < 5:
      all_hands = list(itertools.combinations(self.community_cards, 3))
      for comm_hand in all_hands:
        sd.append(self.player_hand[0])
        sd.append(self.player_hand[1])
        for card in comm_hand:
          sd.append(card)
        sd = Card.card_sort(sd)
        prev = sd[0]
        for i in range(1, 5):
          if sd[i].get_value() - prev.get_value() < 5:
            draw_count += 1
          prev = sd[i]
        if draw_count > max_draw_count:
          max_draw_count = draw_count
        for card in sd:
          print(card, end = " ")
        print(draw_count)
        draw_count = 0
        sd = []

      return max_draw_count

  def fh_draw(self):
    hands = self.get_all_hands(True)
    for hand in hands:
      if Table.pair(hand) and len(Table.pair(hand)) == 2:
        return 4

  def pair_draw(self):
    hands = self.get_all_hands(True)
    for hand in hands:
      if Table.pair(hand) and len(Table.pair(hand)) == 1:         
        return 5

  def no_pair(self):
    hands = self.get_all_hands(True)
    for hand in hands:
      if not Table.pair(hand):
        return 6

  def set(self):
    if self.pockets():
      for card in self.community_cards:
        if self.player_hand[0].get_value() == card.get_value():
          return 7

  def s_draw_open(self):
    hands = self.get_all_hands()
    for hand in hands:
      draw = list(itertools.combinations(hand, 3))
      for h in draw:
        if h[1].get_value() - h[0].get_value() == 1:
          if h[2].get_value() - h[1].get_value() == 1:
            return 8

  def flush_draw(self):
    if self.player_hand[0].get_suit() == self.player_hand[1].get_suit():
      for card in self.community_cards:
        if card.get_suit() == self.player_hand[0].get_suit():
          return 9












  def get_outs(self):
    outs = 0
    # open straight and flush draw
    if self.flush_draw():
      outs += self.flush_draw()
    elif self.s_draw_open():
      outs += self.s_draw_open()
    elif self.set():
      outs += self.set()
    elif self.overcard() == 6:
      outs += self.overcard()
    elif self.no_pair():
      outs += self.no_pair()
    elif self.pair_draw():
      outs += self.pair_draw()
    elif self.fh_draw():
      outs += self.fh_draw()
    elif self.overcard():
      outs += self.overcard()
    elif self.pockets():
      outs += self.pockets()
    return (outs * 4)- (outs - 8)



c1 = Card("K", "h")
c2 = Card("K", "d")

b1 = Card("Q", "h")
b2 = Card("8", "d")
b3 = Card("K", "c")
b4 = Card("3", "d")
b5 = Card("2", "s")

d = Deck()
d.ordered_deck()
d.shuffle()
t = Table([], d, [c1, c2], [b1,b2,b3,b4,b5])
# print(t.get_outs())
# for hand in t.get_all_hands():
#   print()
#   for card in hand:
#     print(card, end = " ")
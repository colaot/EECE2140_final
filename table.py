from cards import Card

class Table:
  def __init__(self, players, deck, player_hand = []):
    self.players = players
    self.num_players = len(players)
    self.deck = deck
    self.player_hand = player_hand
    self.community_cards = []
    
  def get_num_players(self):
    return self.num_players

  def deal(self):
    for i in [1, 2]:
      for i in range(num_players):
        if (players[i] == None):
          self.deck.pop()
        else:
          self.player_hand.append(self.deck.pop())

  def deal_comm_cards(self):
    self.deck.deal_card()
    self.community_cards = self.deck.dealt

  def get_comm_cards(self):
    for card in self.community_cards:
      print(card)
          

  
  

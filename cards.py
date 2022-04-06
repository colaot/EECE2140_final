class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def get_rank(self):
		if self.rank == "A":
			return 14
		elif self.rank == "K":
			return 13
		elif self.rank == "Q":
			return 12
		elif self.rank == "J":
			return 11
		else:
			return int(self.rank)

	def get_suit(self):
		if self.suit == "s":
			return "Spades"
		elif self.suit == "h":
			return "Hearts"
		elif self.suit == "c":
			return "Clubs"
		else
			return "Diamonds"

	def get_card(self):
		return self.rank + self.suit

	def __str__(self):
		return self.get_rank() + "of" + self.get_suit

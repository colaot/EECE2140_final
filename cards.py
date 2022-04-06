import random

class Deck:
	def __init__(self):
		self.cards = []
		self.dealt = []

	def ordered_deck(self):
		for s in Card.get_suits():
			for r in Card.get_ranks():
				self.cards.append(Card(r, s))

	def shuffle(self):
		for i in range(0,52):
			r = i + (random.randint(0,55) % (52 - i))
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def deal_card(self):
		if len(self.dealt) == 0:
			self.cards.pop()
			self.dealt.append(self.cards.pop())
			self.dealt.append(self.cards.pop())
			self.dealt.append(self.cards.pop())
			return
		if len(self.dealt) == 3:
			self.cards.pop()
			self.dealt.append(self.cards.pop())
			return
		if len(self.dealt) == 4:
			self.cards.pop()
			self.dealt.append(self.cards.pop())
			return

	def __str__(self):
		output = ""
		for card in self.cards:
			output += str(card) + "\n"
		return output


class Card:
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

	def get_value(self):
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


	def get_rank(self):
		if self.rank == "A":
			return "Ace"
		elif self.rank == "K":
			return "King"
		elif self.rank == "Q":
			return "Queen"
		elif self.rank == "J":
			return "Jack"
		else:
			return self.rank

	def get_suit(self):
		if self.suit == "s":
			return "Spades"
		elif self.suit == "h":
			return "Hearts"
		elif self.suit == "c":
			return "Clubs"
		else:
			return "Diamonds"

	def get_card(self):
		return self.rank + self.suit

	@staticmethod
	def get_ranks():
		return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

	@staticmethod
	def get_suits():
		return ["s", "c", "h", "d"]

	def __str__(self):
		return self.get_rank() + " of " + self.get_suit()

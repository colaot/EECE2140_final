import random

class Deck:
	"""
	A class to represent a Deck of Cards

	Attributes
	----------
	cards: list
	dealt: list
	"""
	def __init__(self):
		self.cards = []
		self.dealt = []

	def get_cards(self):
		"""
		Returns the list of cards

		Return
		------
		cards: list
		"""
		return self.cards

	def ordered_deck(self):
		"""
		Generates an ordered deck of cards
		"""
		for s in Card.get_suits():
			for r in Card.get_ranks():
				self.cards.append(Card(r, s))

	def shuffle(self):
		"""
		Shuffles a the cards
		"""
		for i in range(0,52):
			r = i + (random.randint(0,55) % (52 - i))
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def deal_card(self):
		"""
		Moves cards from the deck to dealt
		"""
			self.cards.pop()
			self.dealt.append(self.cards.pop())
			self.dealt.append(self.cards.pop())
			self.dealt.append(self.cards.pop())
			self.cards.pop()
			self.dealt.append(self.cards.pop())
			return

	def place_cards(self, placed_cards):
		"""
		Adds cards from user input

		Parameters
		----------
		placed_cards: list
		"""
		for placed_card in placed_cards:
			self.dealt.append(placed_card)
			self.cards.remove(placed_card)
		return

	def __str__(self):
		"""
		Represents a deck of cards as a string

		Return
		------
		String
		"""
		output = ""
		for card in self.cards:
			output += str(card) + "\n"
		return output


class Card:
	"""
	A class to represent a standard playing card

	Attributes
	----------
	suit: String
	rank: String
	"""
	def __init__(self, rank, suit):
		self.suit = suit
		self.rank = rank

	def get_value(self):
		"""
		Returns the value of the card

		Return
		------
		Integer
		"""
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
		"""
		Returns the rank of the card

		Return
		------
		String
		"""
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
		"""
		Returns the suit of the card

		Return
		------
		String
		"""
		if self.suit == "s":
			return "Spades"
		elif self.suit == "h":
			return "Hearts"
		elif self.suit == "c":
			return "Clubs"
		else:
			return "Diamonds"

	def get_card(self):
		"""
		Returns the attributes of the card

		Return
		------
		String
		"""
		return self.rank + self.suit

	@staticmethod
	def get_ranks():
		"""
		Returns the valid ranks of cards

		Return
		------
		List
		"""
		return ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

	@staticmethod
	def get_suits():
		"""
		Returns the valid suits of cards

		Return
		------
		List
		"""
		return ["s", "c", "h", "d"]

	@staticmethod
	def card_sort(h):
		"""
		Returns a sorted list of the given cards

		Parameters
		----------
		h: list

		Return
		------
		List
		"""
		h = list(h)
		h.sort(key = Card.get_value)
		return h

	def __eq__(self, other):
		"""
		Returns whether two cards are equal

		Parameters
		----------
		other: Card

		Return
		------
		Boolean
		"""
		if (self.rank == other.rank and self.suit == other.suit):
			return True
		else:
			return False

	def __str__(self):
		"""
		Formats a comprehensible representation of a card

		Return
		------
		String
		"""
		return self.get_rank() + " of " + self.get_suit()


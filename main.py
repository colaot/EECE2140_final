from cards import Card, Deck
from table import Table

def main():
	user_mode = input('Have you already been dealt cards? (Y/N): ')

	d = Deck()
	d.ordered_deck()
	d.shuffle()

	if user_mode == 'Y':
		rank1, rank2, suit1, suit2 = '0', '0', '0', '0'

		while (rank1 not in Card.get_ranks()):
			rank1 = input('What is the rank of your first card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit1 not in Card.get_suits()):
			suit1 = input('What is the suit of your first card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank2 not in Card.get_ranks()):
			rank2 = input('What is the rank of your second card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit2 not in Card.get_suits()):
			suit2 = input('What is the suit of your second card? (\'s\', \'c\', \'h\', \'d\')')
			
		card1 = Card(rank1, suit1)
		card2 = Card(rank2, suit2)

		t = Table([None, 'hero'], d, player_hand = [card1, card2])

		t.get_deck().get_cards().remove(card1)
		t.get_deck().get_cards().remove(card2)

	else:
		t = Table([None, 'hero'], d)
		t.deal()
	print()
	for card in t.get_player_hand():
		print(card)
	print()
	'''t.deal_comm_cards()
	for card in t.get_comm_cards():
		print(card)
	print()
	t.deal_comm_cards()
	for card in t.get_comm_cards():
		print(card)
	print()
	t.deal_comm_cards()
	for card in t.get_comm_cards():
		print(card)
	print()'''

	stage = input('Is this the flop, turn, or river? (F/T/R): ')

	if (stage == 'F'):
		rank1, rank2, rank3, suit1, suit2, suit3 = '0', '0', '0', '0', '0', '0'

		while (rank1 not in Card.get_ranks()):
			rank1 = input('What is the rank of the first card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit1 not in Card.get_suits()):
			suit1 = input('What is the suit of the first card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank2 not in Card.get_ranks()):
			rank2 = input('What is the rank of the second card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit2 not in Card.get_suits()):
			suit2 = input('What is the suit of the second card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank3 not in Card.get_ranks()):
			rank3 = input('What is the rank of the third card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit3 not in Card.get_suits()):
			suit3 = input('What is the suit of the third card? (\'s\', \'c\', \'h\', \'d\')')

		card1 = Card(rank1, suit1)
		card2 = Card(rank2, suit2)
		card3 = Card(rank3, suit3)

		t.place_comm_cards([card1, card2, card3])

	elif (stage == 'T'):
		rank1, rank2, rank3, rank4, suit1, suit2, suit3, suit4 = '0', '0', '0', '0', '0', '0', '0', '0'

		while (rank1 not in Card.get_ranks()):
			rank1 = input('What is the rank of the first card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit1 not in Card.get_suits()):
			suit1 = input('What is the suit of the first card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank2 not in Card.get_ranks()):
			rank2 = input('What is the rank of the second card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit2 not in Card.get_suits()):
			suit2 = input('What is the suit of the second card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank3 not in Card.get_ranks()):
			rank3 = input('What is the rank of the third card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit3 not in Card.get_suits()):
			suit3 = input('What is the suit of the third card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank3 not in Card.get_ranks()):
			rank3 = input('What is the rank of the third card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit3 not in Card.get_suits()):
			suit3 = input('What is the suit of the third card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank4 not in Card.get_ranks()):
			rank4 = input('What is the rank of the fourth card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit4 not in Card.get_suits()):
			suit4 = input('What is the suit of the fourth card? (\'s\', \'c\', \'h\', \'d\')')

		card1 = Card(rank1, suit1)
		card2 = Card(rank2, suit2)
		card3 = Card(rank3, suit3)
		card4 = Card(rank4, suit4)

		t.place_comm_cards([card1, card2, card3, card4])

	else:
		rank1, rank2, rank3, rank4, rank5, suit1, suit2, suit3, suit4, suit5 = '0', '0', '0', '0', '0', '0', '0', \
																			   '0', '0', '0'

		while (rank1 not in Card.get_ranks()):
			rank1 = input('What is the rank of the first card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit1 not in Card.get_suits()):
			suit1 = input('What is the suit of the first card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank2 not in Card.get_ranks()):
			rank2 = input('What is the rank of the second card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit2 not in Card.get_suits()):
			suit2 = input('What is the suit of the second card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank3 not in Card.get_ranks()):
			rank3 = input('What is the rank of the third card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit3 not in Card.get_suits()):
			suit3 = input('What is the suit of the third card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank3 not in Card.get_ranks()):
			rank3 = input('What is the rank of the third card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit3 not in Card.get_suits()):
			suit3 = input('What is the suit of the third card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank4 not in Card.get_ranks()):
			rank4 = input('What is the rank of the fourth card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit4 not in Card.get_suits()):
			suit4 = input('What is the suit of the fourth card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank5 not in Card.get_ranks()):
			rank5 = input('What is the rank of the fifth card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit5 not in Card.get_suits()):
			suit5 = input('What is the suit of the fifth card? (\'s\', \'c\', \'h\', \'d\')')

		card1 = Card(rank1, suit1)
		card2 = Card(rank2, suit2)
		card3 = Card(rank3, suit3)
		card4 = Card(rank4, suit4)
		card5 = Card(rank5, suit5)

		t.place_comm_cards([card1, card2, card3, card4, card5])

	players_best_hand = t.get_hand()

	pot = float(input('Enter the size of the pot: '))
	call = float(input('Enter the amount needed to call: '))

	lOdds = 1 - wOdds

	ev = (wOdds * pot) - (lOdds * call)

	print('Expected value of calling:', ev)

	if (ev >= 0):
		print('\nIt is profitable to call in this situation.')
	else:
		print('\nFolding is recommended')

if __name__ == '__main__':
	main()
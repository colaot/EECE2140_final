from cards import Card, Deck
from table import Table

def main():
	user_mode = input('Have you already been dealt cards? (Y/N)')

	d = Deck()
	d.ordered_deck()
	d.shuffle()

	if user_mode == 'Y':
		rank1, rank2, suit1, suit2 = '0', '0', '0', '0'

		while (rank1 not in Cards.get_ranks()):
			rank1 = input('What is the rank of your first card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit1 not in Cards.get_suits()):
			suit1 = input('What is the suit of your first card? (\'s\', \'c\', \'h\', \'d\')')
		while (rank2 not in Cards.get_ranks()):
			rank2 = input('What is the rank of your first card? (Number or \'J\', \'Q\', \'K\', \'A\')')
		while (suit2 not in Cards.get_suits()):
			suit2 = input('What is the suit of your first card? (\'s\', \'c\', \'h\', \'d\')')
			
		card1 = Card(rank1, suit1)
		card2 = Card(rank2, suit2)

		t = Table([], d, player_hand = [card1, card2])

	else:
		t = Table([], d)
	t.deal_comm_cards()
	t.deal_comm_cards()
	t.deal_comm_cards()
	t.get_comm_cards()

if __name__ == '__main__':
	main()
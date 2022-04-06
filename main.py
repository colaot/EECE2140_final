from cards import Card, Deck
from table import Table

def main():
	d = Deck()
	d.ordered_deck()
	d.shuffle()
	t = Table([], d)
	t.deal_comm_cards()
	t.deal_comm_cards()
	t.deal_comm_cards()
	t.get_comm_cards()

if __name__ == '__main__':
	main()
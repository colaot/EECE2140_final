from cards import Card, Deck

def main():
	d = Deck()
	d.ordered_deck()
	print(d)
	d.shuffle()
	print(d)

if __name__ == '__main__':
	main()
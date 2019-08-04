# python 3.7.4
from lib.Deck import Deck
from lib.Card import Card
from lib.Dealer import Dealer

#
if __name__ == "__main__":
    dealer = Dealer()

    a = dealer.cards_left
    b = dealer.number_of_deck
    c = dealer.pool_dimension

    d = dealer.pop_card()

    for i in range(100):
        d = dealer.pop_card()

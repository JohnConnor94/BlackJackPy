# python 3.7.4
from lib.Card import Card
from lib.Dealer import Dealer
from lib.Hand import Hand

if __name__ == "__main__":
    dealer = Dealer()

    dealer.shuffle()

    dealer_hand = [Card(10, ""), Card("A", "")]
    player_hand = []

    dealer_hand = Hand(dealer_hand)
    player_hand = Hand()

    player_hand.add_card(dealer.pop_card())
    player_hand.add_card(dealer.pop_card())

    pass

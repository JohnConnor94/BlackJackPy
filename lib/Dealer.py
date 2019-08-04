import random
from lib.Deck import Deck


class Dealer:

    def __init__(self, number_of_decks = 8):
        deck = Deck()
        self._deck_size = len(deck)
        self._number_of_decks = number_of_decks
        self._pool = deck.all_cards() * self._number_of_decks
        del deck

    @property
    def cards_left(self) -> int:
        return len(self._pool)

    @property
    def pool_dimension(self) -> int:
        return self._deck_size * self._number_of_decks

    @property
    def number_of_deck(self) -> int:
        return self._number_of_decks

    def shuffle(self, times = 1000):
        if times <= 0:
            return

        remaining_cards = len(self)

        # switch 2 random cards n times
        for i in range(times):
            a = random.randint(0, remaining_cards - 1)
            b = random.randint(0, remaining_cards - 1)
            self._pool[a], self._pool[b] = self._pool[b], self._pool[a]

    def pop_card(self):
        """
        Get the card and removes it from the deck
        :return (value,seed) if position is valid else it returns None
        """
        position = 0
        card = self._watch_card(position)
        if card:
            self._pool.pop(position)  # using list method to remove the first one
        return card

    def _watch_card(self, position = 0):
        """
        Get the card and don't removes it from the deck
        :param position: get the card from the top of the deck
        :return: (value,seed) if position is valid else it returns None
        """
        if 0 <= position < self.cards_left:
            return self._pool[position]
        else:
            return None

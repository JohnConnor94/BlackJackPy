import random
from lib.Card import Card


class Deck:
    _seeds = ("Hearts", "Diamonds", "Clubs", "Spades")
    _values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, jolly = False):
        self._cards = [Card(v, s) for s in Deck._seeds for v in Deck._values]

        if jolly:
            self._cards += [("Joker", "Red"), ("Joker", "Black")]

    def __len__(self) -> int:
        return len(self._cards)

    def __str__(self) -> str:
        temp = f"Deck {super().__str__()}:\n"
        index = 0
        while index < len(self):
            temp += f"{index + 1} - {self._cards[index]}\n"
            index += 1
        return temp

    def shuffle(self, times = 50):
        if times <= 0:
            return

        remaining_cards = len(self)

        # switch 2 random cards n times
        for i in range(times):
            a = random.randint(0, remaining_cards - 1)
            b = random.randint(0, remaining_cards - 1)
            self._cards[a], self._cards[b] = self._cards[b], self._cards[a]

    def pop_card(self, position = 0):
        """
        Get the card and removes it from the deck
        :param position : get the card from the top of the deck
        :return (value,seed) if position is valid else it returns None
        """

        card = self.watch_card(position)
        if card:
            self._cards.pop(position)  # using list method to remove the first one
        return card

    def watch_card(self, position = 0):
        """
        Get the card and don't removes it from the deck
        :param position: get the card from the top of the deck
        :return: (value,seed) if position is valid else it returns None
        """
        if 0 <= position < len(self):
            return self._cards[position]
        else:
            return None

    def all_cards(self) -> []:
        """
        Create a copy lit of all cards contained in this deck and returns it
        :return: copy list with all cards in deck
        """
        # return self._cards.copy()
        return self._cards[:]  # faster copy list

from lib.Card import Card


class Hand:
    def __init__(self, initial_hand = None):
        if initial_hand is None:
            initial_hand = []
        self._cards = initial_hand

    def add_card(self, card: Card):
        self._cards.append(card)

    @property
    def number_of_cards(self):
        return len(self._cards)

    @property
    def points(self) -> int:
        value = 0
        for card in self._cards:
            if card.value == "K" or card.value == "Q" or card.value == "J":
                value += 10
                continue
            elif card.value == "A":
                # Ace value is 11 when added the total hand is minor or equal to 21
                value += 11
                # remove 10 points if overflow with an Ace
                if value > 21:
                    value -= 10
                    continue
            else:
                value += int(card.value)

        return value

    @property
    def is_black_jack(self) -> bool:
        if self.number_of_cards == 2 and self.points == 21:
            return True
        else:
            return False

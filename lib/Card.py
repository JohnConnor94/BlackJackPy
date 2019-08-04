class Card:

    def __init__(self, value: str, seed: str):
        self._value = value
        self._seed = seed

    def __str__(self):
        return f"{self._value} of {self._seed}"

    @property
    def value(self) -> str:
        return self._value

    @property
    def seed(self) -> str:
        return self._seed

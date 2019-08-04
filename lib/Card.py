class Card:

    def __init__(self, value: str, seed: str):
        self.value = value
        self.seed = seed

    def __str__(self):
        return f"{self.value} of {self.seed}"

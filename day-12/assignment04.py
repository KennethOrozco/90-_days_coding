class Player:
    def __init__(self, name, score=0):
        self.name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, new_score):
        if new_score <= 0:
            raise ValueError("Score cannot be negative")
        self._score = new_score
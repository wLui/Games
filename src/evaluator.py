"""
evaluator.py: Provides an evaluator class to judge the
strength of a two-person game
"""

# Note - must run the test script from top level
from game import Game, Move
from player import Player

class Evaluator():
    """
    Evaluator should be able to be "plugged into" an existing/new game,
    so we'll perform composition with a Game instance
    """
    class Evaluation():
        def __init__(self, score, move):
            self._score = score
            self._move = move

        @property
        def score(self):
            return self._score

        @score.setter
        def score(self, score):
            self._score = score

        @property
        def move(self):
            return self._move

        @move.setter
        def move(self, move):
            self._move = move

    def __init__(self, game: Game):
        """ 
        Should pass in a derived Game object to the evaluator object.
        """
        self._game = game

    def evaluate(self) -> Evaluation:
        pass

    def recommend(self) -> Move:
        """
        Recommend a move at the current board state.
        The player is derived by looking at the game's player
        """
        pass


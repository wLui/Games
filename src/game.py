"""
game.py: Defines an interface/abstract class for a (board?) game
"""
from abc import ABC, abstractmethod

Move = tuple

class Game(ABC):
    class Move(ABC):
        @abstractmethod
        def __hash__(self):
            pass

    class Board(ABC):
        @abstractmethod
        def __hash__(self):
            pass

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def can_play(self, move):
        pass

    @property
    @abstractmethod
    def winner(self):
        pass

    @abstractmethod
    def find_winner(self):
        pass

    @property
    @abstractmethod
    def player(self):
        pass

    @property
    @abstractmethod
    def available_moves(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @property
    @abstractmethod
    def board(self):
        pass

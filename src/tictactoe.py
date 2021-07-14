"""
tictactoe.py: Specific instance of the Tic Tac Toe game
"""
from functools import reduce
from game import Game, Move
from player import Player, BLANK

SPACING = 4

class TicTacToe(Game):
    class Board(list): # could very well define on its own...
        def __hash__(self):
            return hash(
                tuple(
                    reduce(
                        lambda x, y: x + y,
                        tuple(tuple(elm) for elm in self),
                        tuple()
                    )
                )
            )

        def set(self, move, val):
            self[move[0]][move[1]] = val
            return

        def get(self, move):
            return self[move[0]][move[1]]

    def __init__(self, dim, cnt = 2):
        self._board = TicTacToe.Board([BLANK] * dim for _ in range(dim))
        self._dim = dim
        self._available_moves = set(Move((i, j)) for i in range(dim) for j in range(dim))
        self._moves = []
        self._player, self._winner = Player(cnt), BLANK

    def __str__(self):
        res = []
        for idx, line in enumerate(self._board):
            if idx > 0:
                res.append(("-" * SPACING + "+") * (self._dim - 1) + ("-" * SPACING))

            res.append("|".join([f"{self.convert(elm):{SPACING}}" for elm in line]))

        return "\n".join(res)

    @property
    def available_moves(self):
        return self._available_moves

    @property
    def player(self):
        """
        Note the player returned is that who is expected to make a move
        """
        return self._player

    @property
    def winner(self):
        return self._winner

    def play(self, move: Move):
        """
        Attempt to play the specified move.
        """
        if self.can_play(move):
            return
        return

    def undo(self):
        return

    @property
    def board(self):
        return self._board

    def convert(self, c):
        return Player.val_to_char(c)

    @property
    def moves(self):
        return self._moves

def main():
    game = TicTacToe(3, 2)
    print(game)

if __name__ == "__main__":
    main()

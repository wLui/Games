
BLANK = 0
PLAYER_MAP = {
    0: ' ',
    1: 'X',
    2: 'O',
    3: 'A',
    4: 'Z'
}

REV_MAP = {
    v: k for (k, v) in PLAYER_MAP.items()
}

MIN_PLAYERS, MAX_PLAYERS = 1, len(PLAYER_MAP) - 1

class Player():
    def __init__(self, cnt):
        if cnt < MIN_PLAYERS or cnt > MAX_PLAYERS:
            raise ValueError("Cannot have number of players is out of range !")

        self._cnt = cnt
        self._player = 1

    def __eq__(self, other):
        return self._cnt == other._cnt and self._player == other._player

    @property
    def player(self):
        return self._player

    @property
    def __str__(self):
        return PLAYER_MAP[self._player]

    def val_to_char(c):
        return PLAYER_MAP[c]

    def _next_player(self):
        player = (self._player + 1) % (self._cnt + 1)
        if player == BLANK:
            player = (player + 1) % (self._cnt + 1)

        return player

    def advance(self):
        self._player = self._next_player()

    def _prev_player(self):
        player = (self._player - 1) % (self._cnt + 1)
        if player == BLANK:
            player = (player - 1) % (self._cnt + 1)

        return player

    def previous(self):
        self._player = self._prev_player()


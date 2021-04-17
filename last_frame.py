from frame import Frame


class LastFrame(Frame):
    def __init__(self, pins_knocked_down, game):
        super().__init__(pins_knocked_down, game, False)

    def is_maximum_rolls_reached(self):
        return self._has_played_three_rolls()

    def _has_played_three_rolls(self):
        return len(self.rolls) == 3

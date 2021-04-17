from frame import Frame


class LastFrame(Frame):
    def __init__(self, pins_knocked_down, game):
        super().__init__(pins_knocked_down, game, False)

    def set_next_roll_score(self, pins_knocked_down):
        if not self.is_strike() and len(self.rolls) == 2:
            raise Exception("Frame was not a strike, cant add more rolls")
        else:
            super().set_next_roll_score(pins_knocked_down)

    def is_maximum_rolls_reached(self):
        return self._has_played_three_rolls()

    def _has_played_three_rolls(self):
        return len(self.rolls) == 3

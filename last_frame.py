from frame import Frame


class LastFrame(Frame):
    def __init__(self, pins_knocked_down, game):
        super().__init__(pins_knocked_down, game, False)

    def set_next_roll_score(self, pins_knocked_down):
        self.rolls.append(pins_knocked_down)

    def is_maximum_rolls_reached(self):
        if self.is_strike():
            return self._has_played_three_rolls()
        else:
            return self._has_played_two_rolls()

    def _has_played_three_rolls(self):
        return len(self.rolls) == 3

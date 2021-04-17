from observable import Observable
from observer import Observer


class Frame(Observer):
    TOTAL_NUMBER_PINS = 10
    MAX_NUMBER_OF_FRAMES = 10

    def __init__(self, pins_knocked_down, game):
        self.rolls = [pins_knocked_down]
        self.additional_points = []
        self.observable = game
        if self.is_strike():
            self.observable.register_observer(self)

    @property
    def first_roll_score(self):
        return self.rolls[0]

    @property
    def second_roll_score(self):
        if self._has_played_two_rolls():
            return self.rolls[1]

    def get_frame_score(self):
        return sum(self.rolls) + sum(self.additional_points)

    def set_next_roll_score(self, pins_knocked_down):
        self.rolls.append(pins_knocked_down)
        if self.is_spare():
            self.observable.register_observer(self)

    def is_spare(self):
        if self._are_all_pins_knocked_down():
            return self._has_played_two_rolls()
        return False

    def is_strike(self):
        if self._are_all_pins_knocked_down():
            return self.first_roll_score == self.TOTAL_NUMBER_PINS
        return False

    def is_maximum_rolls_reached(self, number_of_frames):
        is_last_frame = number_of_frames == self.MAX_NUMBER_OF_FRAMES
        if is_last_frame and self.is_strike():
            return self._has_played_three_rolls()

        return (
            self._are_all_pins_knocked_down() or
            self._has_played_two_rolls()
        )

    def _are_all_pins_knocked_down(self):
        return self.total_pins_knocked_down == self.TOTAL_NUMBER_PINS

    @property
    def total_pins_knocked_down(self):
        return sum(self.rolls)

    def _has_played_two_rolls(self):
        return len(self.rolls) == 2

    def _has_played_three_rolls(self):
        return len(self.rolls) == 2

    def update(self, pins_knocked_down):
        if self.is_spare():
            self.additional_points.append(pins_knocked_down)
            self.observable.remove_observer(self)

    def __repr__(self):
        representation = "|"
        for roll in self.rolls:
            representation += f" {roll} -"

        representation = representation[:-1] + " ;"
        for additional in self.additional_points:
            representation += f" {additional} -"

        if self.additional_points:
            representation = representation[:-1] + f" ; T: {self.get_frame_score()} "
        else:
            representation = representation + f" T: {self.get_frame_score()} "
        representation += "|"

        return representation

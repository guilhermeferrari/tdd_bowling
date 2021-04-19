from observable import Observable
from observer import Observer


class Frame(Observer):
    TOTAL_NUMBER_PINS = 10
    MAX_NUMBER_OF_FRAMES = 10

    def __init__(self, pins_knocked_down, game, should_register_observer=True):
        self.rolls = [pins_knocked_down]
        self.additional_points = []
        self.observable = game
        if self.is_strike() and should_register_observer:
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
        return self._are_all_pins_knocked_down() and self._has_played_two_rolls()

    def is_strike(self):
        return self.first_roll_score == self.TOTAL_NUMBER_PINS

    def is_maximum_rolls_reached(self):
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

    def update(self, pins_knocked_down):
        self.additional_points.append(pins_knocked_down)
        if self._should_stop_observing_rolls:
            self.observable.remove_observer(self)

    @property
    def _should_stop_observing_rolls(self):
        return (
            self.is_spare() or
            (self.is_strike() and len(self.additional_points) == 2)
        )

    def __add__(self, other):
        if isinstance(other, Frame):
            return self.get_frame_score() + other.get_frame_score()
        else:
            return self.get_frame_score() + other

    def __radd__(self, other):
        if other == 0:
            return self.get_frame_score()
        else:
            return self.__add__(other)

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

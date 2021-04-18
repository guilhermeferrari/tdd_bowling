from frame import Frame
from game_observable import GameObservable
from last_frame import LastFrame
from observable import Observable


class Game(GameObservable):
    def __init__(self):
        self.all_frames = []
        self.observable = Observable()

    def roll(self, pins_knocked_down):
        self.notify_observers(pins_knocked_down)
        if self._should_create_new_frame():
            self._create_frame(pins_knocked_down)
        else:
            self._add_roll_latest_frame(pins_knocked_down)

    def _should_create_new_frame(self):
        number_of_frames = len(self.all_frames)
        is_first_frame = (number_of_frames == 0)
        if is_first_frame:
            return True

        last_frame: Frame = self.all_frames[-1]
        return last_frame.is_maximum_rolls_reached()

    def _create_frame(self, pins_knocked_down):
        if self._has_reached_max_number_of_frames:
            raise Exception("10 frames is the limit")
        elif self._next_frame_should_be_last:
            frame = LastFrame
        else:
            frame = Frame

        self.all_frames.append(frame(pins_knocked_down, self))

    def _add_roll_latest_frame(self, pins_knocked_down):
        last_frame: Frame = self.all_frames[-1]
        last_frame.set_next_roll_score(pins_knocked_down)

    @property
    def _next_frame_should_be_last(self):
        return len(self.all_frames) == 9

    @property
    def _has_reached_max_number_of_frames(self):
        return len(self.all_frames) == 10

    def score(self):
        if self.all_frames:
            return sum(self.all_frames).get_frame_score()
        else:
            return 0

    def remove_observer(self, observer):
        self.observable.remove_observer(observer)

    def register_observer(self, observer):
        self.observable.register_observer(observer)

    def notify_observers(self, pins_knocked_down):
        self.observable.notify_observers(pins_knocked_down)



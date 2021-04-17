from frame import Frame


class Game:
    def __init__(self):
        self.all_frames = []

    def roll(self, pins_knocked_down):
        if self._should_create_new_frame():
            frame = Frame(pins_knocked_down)
            self.all_frames.append(frame)
        else:
            self.all_frames[-1].set_next_roll_score(pins_knocked_down)

    def score(self):
        score = 0
        for frame in self.all_frames:
            score += frame.total_pins_knocked_down
            if frame.is_spare():
                score += self.sum_next_roll(frame)

            elif frame.is_strike():
                score += self.sum_next_two_rolls(frame)

        return score

    def sum_next_roll(self, frame):
        if self.has_next_frame(frame):
            index_next_frame = self.all_frames.index(frame) + 1
            next_frame: Frame = self.all_frames[index_next_frame]
            return next_frame.first_roll_score
        else:
            return 0

    def sum_next_two_rolls(self, frame):
        if self.has_next_frame(frame):
            index_next_frame = self.all_frames.index(frame) + 1
            next_frame: Frame = self.all_frames[index_next_frame]
            if next_frame.is_strike() and self.has_next_frame(next_frame):
                return next_frame.total_pins_knocked_down + self.sum_next_roll(next_frame)

            return next_frame.total_pins_knocked_down
        else:
            return 0

    def has_next_frame(self, frame):
        index_current_frame = self.all_frames.index(frame)
        return len(self.all_frames) > index_current_frame + 1

    def _should_create_new_frame(self):
        number_of_frames = len(self.all_frames)
        is_first_frame = (number_of_frames == 0)
        if is_first_frame:
            return True

        last_frame: Frame = self.all_frames[-1]
        return last_frame.is_maximum_rolls_reached(number_of_frames)



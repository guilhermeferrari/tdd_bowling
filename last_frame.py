from frame import Frame


class LastFrame(Frame):
    def __init__(self, pins_knocked_down, game):
        super().__init__(pins_knocked_down, game, False)

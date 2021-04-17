from frame import Frame
from game import Game
from tests.test_bowling import roll_many


def test_frame_spare_score():
    game = Game()
    spare = [4, 6]
    complete_frame = [4, 3, 1, 2, *spare, 7, 1, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3]
    roll_many(game, complete_frame)
    spare_frame: Frame = game.all_frames[2]
    assert spare_frame.get_frame_score() == 17

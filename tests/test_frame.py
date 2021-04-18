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


def test_frame_strike_score():
    game = Game()
    strike = [10]
    complete_frame = [4, 3, 1, 2, *strike, 2, 4, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3]
    roll_many(game, complete_frame)
    spare_frame: Frame = game.all_frames[2]
    assert spare_frame.get_frame_score() == 16


def test_add_frames():
    game = Game()
    frame1 = Frame(1, game)
    frame1.set_next_roll_score(2)
    frame2 = Frame(2, game)
    frame1.set_next_roll_score(3)
    assert frame1 + frame2 == 8

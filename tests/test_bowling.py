from frame import Frame
from game import Game
import pytest


def test_game_start():
    game = Game()
    assert game.score() == 0


def test_simple_frame_no_strikes_no_spares():
    game = Game()
    roll_many(game, [4, 3, 1, 2, 4, 5, 7, 1, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3])
    assert game.score() == 61


def test_simple_exceeding_row():
    game = Game()
    with pytest.raises(Exception):
        roll_many(game, [4, 3, 1, 2, 4, 5, 7, 1, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3, 2])


def test_frame_single_spare():
    game = Game()
    spare = [4, 6]
    complete_frame = [4, 3, 1, 2, *spare, 7, 1, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3]
    roll_many(game, complete_frame)
    assert game.score() == 69


def test_frame_double_spare():
    game = Game()
    spare = [4, 6]
    complete_frame = [4, 3, 1, 2, *spare, *spare, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3]
    roll_many(game, complete_frame)
    assert game.score() == 71


def test_spare_at_start():
    game = Game()
    roll_many(game, [6, 4])
    assert game.score() == 10


def test_spare_at_start_followed_by_simple_roll():
    game = Game()
    roll_many(game, [6, 4, 3])
    assert game.score() == 16


def test_frame_single_strike():
    game = Game()
    strike = [10]
    complete_frame = [4, 3, 1, 2, *strike, 2, 4, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 3, 3]
    roll_many(game, complete_frame)
    assert game.score() == 66


def test_frame_single_strikee():
    game = Game()
    strike = [10]
    complete_frame = [4, 3, 1, 2, *strike, 2, 4, 3, 3, 4, 3, 1, 2, 3, 1, 7, 1, 1, 9]
    roll_many(game, complete_frame)
    assert game.score() == 70


def test_strike_at_start():
    game = Game()
    roll_many(game, [10])
    assert game.score() == 10


def test_strike_at_start_followed_by_simple_roll():
    game = Game()
    roll_many(game, [10, 2])
    assert game.score() == 14


def test_double_strike_at_start_followed_by_simple_roll():
    game = Game()
    roll_many(game, [10, 10, 2])
    assert game.score() == 36


def test_triple_strike_at_start():
    game = Game()
    roll_many(game, [10, 10, 10])
    assert game.score() == 60


def test_mixed_rolls():
    game = Game()
    roll_many(game, [10, 10, 10, 7, 2, 8, 2, 0, 9, 10, 7, 3, 9, 0])
    assert game.score() == 152


def test_mixed_rolls_end_with_strike():
    game = Game()
    roll_many(game, [10, 10, 10, 7, 2, 8, 2, 0, 9, 10, 7, 3, 9, 0, 10, 10, 8])
    assert game.score() == 180


def test_max_score():
    game = Game()
    roll_many(game, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
    assert game.score() == 300


def test_spares_and_strikes():
    game = Game()
    strike = 10
    spare_nine = [9, 1]
    spare_eight = [8, 2]
    roll_many(game, [*spare_nine, *spare_eight, *spare_nine, 6, 3, *spare_eight, strike, strike, strike, strike, strike, *spare_nine]) # NOQA
    assert game.score() == 221


def roll_many(game, frames):
    for frame in frames:
        game.roll(frame)

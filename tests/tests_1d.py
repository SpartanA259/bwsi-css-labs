import pytest
from labs.lab_1.lab_1d import two_sum

def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]     # 2 + 7 = 9

def test_non_adjacent():
    assert two_sum([1, 4, 6], 7) == [0, 2]          # 1 + 6 = 7

def test_negative_numbers():
    assert two_sum([-5, -2, -19, -9], -14) == [0, 3]    # -5 + -9 = -14

def test_duplicates():
    assert two_sum([3, 3, 4], 6) == [0, 1]           # 3 + 3 = 6

def test_single_pair():
    assert two_sum([2, 5], 7) == [0, 1]
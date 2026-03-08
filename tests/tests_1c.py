import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_all_negative():
    assert max_subarray_sum([-5, -1, -9]) == -1     # Best single element

def test_all_positive():
    assert max_subarray_sum([5, 1, 10]) == 16       # Entire Array

def test_single_element():
    assert max_subarray_sum([5]) == 5

def test_empty_list():
    with pytest.raises(ValueError, match="List cannot be empty."):
        max_subarray_sum([])
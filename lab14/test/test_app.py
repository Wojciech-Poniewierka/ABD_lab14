import pytest
from app import bubblesort
# tests for file app.py

testdata = [([0, 4, 2, 7, 14], [0, 2, 4, 7, 14]),
([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
([6, 2, 0, 4, 1, 0, 0, 3], [0, 0, 0, 1, 2, 3, 4, 6]),
([1, 2, 3, 4], [1, 2, 3, 4])]


@pytest.mark.parametrize('input, expected_output', testdata)
def test_bubblesort(input, expected_output):
	assert bubblesort(input) == expected_output

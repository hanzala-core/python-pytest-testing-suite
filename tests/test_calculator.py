
import pytest
from calculator import add, divide, is_even


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -4) == -5


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="divide by zero"):
        divide(5, 0)


def test_float_addition():
    assert add(0.1, 0.2) == pytest.approx(0.3)


@pytest.mark.parametrize("n, expected", [
    (2, True),
    (7, False),
    (0, True),
    (-3, False),
])
def test_is_even(n, expected):
    assert is_even(n) == expected

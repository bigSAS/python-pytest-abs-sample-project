import pytest
from libs.funcs.math import add


@pytest.mark.unit
def test_unit_one():
    assert add(1, 1) == 2


@pytest.mark.unit
@pytest.mark.math
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 2, 4),
    (3, 3, 6)
])
def test_unit_two(a: int, b: int, expected: int):
    assert add(a, b) == expected

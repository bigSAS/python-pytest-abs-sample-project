import pytest

from src.funcs import add


@pytest.mark.unit
def test_unit_one():
    assert add(1, 1) == 2


@pytest.mark.unit
def test_unit_two():
    assert add(2, 2) == 4

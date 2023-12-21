import pytest
@pytest.mark.parametrize("input,expected", [
    ("3+5", 8),
    ("2+4", 6),
     pytest.mark.xfail(("6*9", 42)),  # sta raditi sa testovima koji uvijek padaju?
])
def test_eval(input, expected):
    assert eval(input) == expected

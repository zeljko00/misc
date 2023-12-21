import pytest
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def f():
    raise SystemExit(1)
# testing exceptions
def test_mytest():
    with pytest.raises(SystemExit):
        f()

# creating fixture - function responsible for creating initial state for every test
@pytest.fixture
def setup_database():
    return ["a","b",3,4,"e"]

def test_database(setup_database):
    assert "aa" in setup_database


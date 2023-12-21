import pytest

@pytest.fixture
def setup_widget():
    from widget.widget import Widget
    return Widget("testni podaci")

def test_widget(setup_widget):
    assert setup_widget.name == "testni podaci"
    assert 50 == setup_widget.x
    assert setup_widget.y == setup_widget.x
    assert False
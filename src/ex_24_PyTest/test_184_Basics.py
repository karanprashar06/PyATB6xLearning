import pytest

@pytest.mark.smoke
def test_basic():
    print("Basic test")
    assert 5==6

@pytest.mark.smoke
def test_basic2():
    print("Basic test2")
    assert 6==6
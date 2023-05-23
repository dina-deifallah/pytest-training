import pytest

# fixtures/test_fixture.py
@pytest.fixture
def answer():
    return 42

def test_universe(answer):
    assert answer == 42

@pytest.fixture
def hello_msg():
    return "Hello!"

def test_hello_msg(hello_msg):
    assert hello_msg == "Hello!"
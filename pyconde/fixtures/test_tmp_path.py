import pytest

# fixtures/test_tmp_path.py

@pytest.fixture
def input_file(tmp_path):
    path = tmp_path / "input.txt"
    path.write_text("Hello World")
    return path

#def test_things(input_file):
    #assert False, str(input_file)


def test_second(input_file):
    text = input_file.read_text()
    assert text == "Hello World"
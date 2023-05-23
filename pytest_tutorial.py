import pytest

def division(x, y):
    return (x/y)
    
def test_division():
    print("testing division function")
    assert division(1, 1)

#def test_raises():
    #with pytest.raises(ZeroDivisionError):
        #division(3, 2)

@pytest.mark.parametrize("a, b", [(1, 5), (3, 2), (7, 2)])
def test_division_multiple(a, b):
    assert division(a, b)
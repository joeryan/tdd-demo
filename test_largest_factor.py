import pytest
from largest_factor import largest_factor

def test_largest_factor_2():
    assert largest_factor(2) == 2

def test_largest_factor_3():
    assert largest_factor(3) == 3

def test_largest_factor_5():
    assert largest_factor(5) == 5

def test_largest_factor_52():
    assert largest_factor(52) == 13

def test_largest_factor_72():
    assert largest_factor(72) == 3

def test_largest_factor_5_7_11():
    assert largest_factor(5*7*11) == 11

def test_largest_factor_5_7_11_11():
    assert largest_factor(5*7*11*11) == 11

def test_largest_factor_minus1():
    with pytest.raises(ValueError):
        largest_factor(-1)

def test_largest_factor_0():
    with pytest.raises(ValueError):
        largest_factor(0)

def test_largest_factor_1():
    with pytest.raises(ValueError):
        largest_factor(1)

def test_largest_factor_pi():
    with pytest.raises(ValueError):
        largest_factor(3.1415926)

def test_largest_factor_hello():
    with pytest.raises(TypeError):
        largest_factor('hello')


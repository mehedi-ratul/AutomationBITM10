import pytest
import math

@pytest.fixture()
def input_value1():
    number1=10
    return number1
@pytest.mark.order(2)
def test_tc1_multiply1(input_value1):
    number2=20
    assert input_value1*number2==200

@pytest.mark.order(1)
def test_tc2_multiply2(input_value1):
    number2=20
    assert input_value1*number2==200

@pytest.mark.order(4)
def test_tc3_multiply3(input_value1):
    number2=20
    assert input_value1*number2==200

@pytest.mark.order(3)
def test_tc4_multiply4(input_value1):
    number2=20
    assert input_value1*number2==200
import pytest
import math


@pytest.yield_fixture()
def setup():
    print("Browsesr Launch Successfully")
    yield
    print("Browser closed successfully")


def test_tc1_login(setup):
    print("Login valid test passed")


def test_tg2_login(setup):
    print("Login Invalid test passed")

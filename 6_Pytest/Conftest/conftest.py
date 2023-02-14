import pytest

@pytest.yield_fixture()
def setup():
    print("Browsesr Launch Successfully")
    yield
    print("Browser closed successfully")


@pytest.yield_fixture(scope='module')
def oneTimeSetup():
    print("Running conftest oneTimeSetup start")
    yield
    print("Running conftest oneTimeSetup tearDown")

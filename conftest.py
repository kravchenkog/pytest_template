import pytest
from fixture.app_manager import AppManager

fixture = None


def get_global_variables():
    global_variables = {
        "local": 1,  # can be 1 or 0
        "browser": 'chrome',  # realized chrome only
        "env": "prod",  # stg or prod
        'test_suite': "",  # will be set automatically
    }

    return global_variables


@pytest.fixture(scope='function')
def app(request):
    variables = get_global_variables()
    global fixture
    variables['test_suite'] = "test1"
    if fixture is None:
        fixture = AppManager(var=variables)
    return fixture

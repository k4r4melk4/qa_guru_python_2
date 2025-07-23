import pytest


@pytest.fixture(scope="session")
def browser():
    print('Браузер открыт')
    yield
    print('Браузер закрыт')
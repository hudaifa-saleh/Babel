import pytest


@pytest.fixture(autouse=True)
def setup_module(db):
    pass

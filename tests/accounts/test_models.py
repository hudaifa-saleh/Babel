import pytest

from tests.accounts.factories import AccountFactory


@pytest.mark.django_db
def test_factory():
    """The factory produces a valid Account"""
    user = AccountFactory()

    assert user is not None


def test_str():
    user_instance = AccountFactory()
    result = str(user_instance)
    assert result == "user_1"

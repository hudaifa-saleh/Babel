import pytest

from powerhouse.accounts.models import User
from powerhouse.moments.models import Moment


@pytest.mark.django_db
def test_moment_str_method():
    user = User.objects.create(username="test-user")
    moment_instance = Moment.objects.create(user=user)
    assert str(moment_instance) == "test-user"

import pytest
from django.test import RequestFactory

from powerhouse.accounts.views import HomePageView


@pytest.fixture
def rf():
    return RequestFactory()


@pytest.fixture
def home_page_view(rf):
    return HomePageView.as_view()


def test_renders_home_template_successfully(client, home_page_view, rf):
    request = rf.get('/')
    response = home_page_view(request)

    assert response.status_code == 200
    assert response.template_name == ["home.html"]

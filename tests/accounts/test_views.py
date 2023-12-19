import pytest

from powerhouse.accounts.views import HomePageView


@pytest.fixture
def test_renders_home_template_successfully(self):
    view = HomePageView()
    response = view.get(request=None)
    assert response.status_code == 200
    assert response.template_name == "home.html"

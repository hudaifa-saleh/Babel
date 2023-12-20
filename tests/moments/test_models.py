from babel.accounts.models import User
from babel.moments.models import Moment


class TestMoment:
    #  Moment instance can be created with required fields
    def test_create_moment_with_required_fields(self):
        user = User.objects.create(username="test-user")
        moment_instance = Moment.objects.create(user=user)
        assert isinstance(moment_instance, Moment)

    #  Moment instance can be created with optional fields
    def test_create_moment_with_optional_fields(self):
        user = User.objects.create(username="test-user")
        moment_instance = Moment.objects.create(user=user, content="test content", image="test.jpg")
        assert isinstance(moment_instance, Moment)

    #  Moment instance can be converted to string
    def test_moment_instance_to_string(self):
        user = User.objects.create(username="test-user")
        moment_instance = Moment.objects.create(user=user)
        assert str(moment_instance) == "test-user"

    #  Moment instance content can be set to maximum length
    def test_set_content_to_maximum_length(self):
        user = User.objects.create(username="test-user")
        content = "a" * 150
        moment_instance = Moment.objects.create(user=user, content=content)
        assert moment_instance.content == content

    #  Moment instance can be created without content and image
    def test_create_moment_without_content_and_image(self):
        user = User.objects.create(username="test-user")
        moment_instance = Moment.objects.create(user=user)
        assert isinstance(moment_instance, Moment)

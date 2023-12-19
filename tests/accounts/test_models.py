from powerhouse.accounts.models import User


class TestUser:
    #  User instance can be created with required fields
    def test_create_user_with_required_fields(self):
        user = User.objects.create(username="test-user")
        assert isinstance(user, User)

    #  User instance can be created with optional fields
    def test_create_user_with_optional_fields(self):
        user = User.objects.create(username="test-user", email="test@example.com")
        assert isinstance(user, User)

    #  User instance can be updated with new fields
    def test_update_user_with_new_fields(self):
        user = User.objects.create(username="test-user")
        user.email = "test@example.com"
        user.save()
        assert user.email == "test@example.com"

    #  User instance can be created with empty fields
    def test_create_user_with_empty_fields(self):
        user = User.objects.create()
        assert isinstance(user, User)

    #  User instance can be created with fields exceeding maximum length
    def test_create_user_with_fields_exceeding_maximum_length(self):
        username = "a" * 150
        user = User.objects.create(username=username)
        assert user.username == username

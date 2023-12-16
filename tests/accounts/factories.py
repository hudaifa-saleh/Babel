import factory

from powerhouse.accounts.models import User


class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"user_{n}@example.com")
    username = factory.Sequence(lambda n: f"user_{n}")

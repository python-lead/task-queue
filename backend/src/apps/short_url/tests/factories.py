import factory

from src.apps.short_url.models import ShortURL


class ShortURLFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ShortURL

    name = factory.Faker("sentence", nb_words=2, variable_nb_words=True)
    url = factory.Faker("url")
